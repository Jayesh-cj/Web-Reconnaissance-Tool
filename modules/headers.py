import requests
from icecream.icecream import ic


def get_security_headers(target):
    url = f"http://{target}"

    security_headers = [
        "Content-Length",
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy",
        "Permissions-Policy",
        "Cross-Origin-Opener-Policy",
        "Cross-Origin-Resource-Policy",
        "Cross-Origin-Embedder-Policy",
    ]

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)

    except requests.RequestException as e:
        print(f"[-] HTTP request failed: {e}")

    print("\n[+] HTTP Headers")
    print("-" * 50)

    print(f"URL             : {response.url}")
    print(f"Status Code     : {response.status_code}")
    print(f"Server          : {response.headers.get('Server', 'Not Found')}")
    print(f"Content-Type    : {response.headers.get('Content-Type', 'Not Found')}")
    print(f"Content-Length  : {response.headers.get('Content-Length', 'Not Found')}")

    print("\n[+] Security Headers")
    print("-" * 50)

    for header in security_headers:
        value = response.headers.get(header)

        if value:
            print(f"\n[+] {header:<10}: Present")
            print(f"    Value: {value}")

        else:
            print(f"\n[-] {header:<10}: Missing")

    print("-" * 50)