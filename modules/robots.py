import requests


def check_robots(target):
    print("\n[+] robots.txt")
    print("─" * 50)

    url = f"https://{target}/robots.txt"

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)

        print(f"URL           : {response.url}")
        print(f"Status Code   : {response.status_code}")

        if response.status_code == 200:

            print(f"\nContents: ")
            print("-" * 50)

            print(response.text)

        elif response.status_code == 404:
            print("[-] robots.txt not found")

        else:
            print(f"[!] robots.txt returned ")
            print(f"HTTP {response.status_code}")

    except requests.RequestException as e:

        print(f"[-] Request failed: {e}")
        print("-" * 50)