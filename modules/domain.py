import socket
from urllib.parse import urlparse

import requests


# Sanitize and extract domain name
def sanitize_domain(target):
    target = target.strip()

    if "://" not in target:
        target = "https://" + target

    parsed = urlparse(target)

    if not parsed.hostname:
        raise ValueError("Invalid target")

    domain = parsed.hostname.lower().rstrip(".")

    return domain



# Check domain is alive or not
def is_domain_resolvable(target):
    try:
        ip = socket.gethostbyname(target)

        return ip
    
    except socket.gaierror as e:
        return None



# Check http details
def check_http(target):
    for scheme in ['https', 'http']:
        url = f"{scheme}://{target}"

        try:
            response = requests.get(
                url, timeout=5, allow_redirects=True
            )

            return {
                "protocol" : scheme.upper(),
                "status_code" : response.status_code,
                "url" : response.url,
                "response_time" : response.elapsed.total_seconds(),
                "server" : response.headers.get('Server', 'Not Found')
            }
        
        except requests.RequestException:
            continue

    return None



# Finalize target info
def check_target(target):
    try:
        domain = sanitize_domain(target)

    except Exception as e:
        print(f"[+] {str(e)}")

        return None
    
    ip = is_domain_resolvable(domain)

    if not ip:
        print("[-] Domain does not resolve")

        return False

    http_info = check_http(domain)

    if check_http(domain):
        print("\n[+] Target Details")
        print("-" * 50)

        print(f"Target          : {domain}")
        print(f"URL             : {http_info['url']}")
        print(f"IP Address      : {ip}")
        print(f"Protocol        : {http_info['protocol']}")
        print(f"HTTP Status     : {http_info['status_code']}")
        print(f"Response Time   : {http_info['response_time']:.2f}s")
        print(f"Server          : {http_info['server']}")

        if http_info:
            print(f"Web Accessible  : {True}")

        else:
            print(f"Web Accessible  : {False}")

        print("-" * 50)

    else:
        print("[!] Domain exists, but web server is not accessible")

        return False