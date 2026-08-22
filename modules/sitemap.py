import requests
import xml.etree.ElementTree as ET


def check_sitemap(target):
    print("\n[+] sitemap.xml")
    print("─" * 50)

    url = f"https://{target}/sitemap.xml"

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)

        print(f"URL         : {response.url}")
        print(f"Status Code : {response.status_code}")

        if response.status_code != 200:

            print(f"[-] sitemap.xml unavailable: ")
            print(f"HTTP {response.status_code}")

            return

        print("\nSitemap URLs:")
        print("─" * 50)

        try:
            root = ET.fromstring(response.content)

            namespace = {
                "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
            }

            urls = root.findall("sm:url/sm:loc", namespace)

            if urls:
                for url in urls:
                    print(f"    {url.text}")

            else:
                print("    No URLs found")

        except ET.ParseError:
            print("[-] Invalid XML sitemap")
            
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

    print("─" * 50)