import socket
import ssl
from datetime import datetime, timezone


def get_name(cert_part):
    """Convert subject/issuer tuple into readable text"""
    values = {}

    for item in cert_part:
        for key, value in item:
            values[key] = value

    return values


def ssl_certificate(target):

    print("\n[+] SSL/TLS Certificate Information")
    print("-" * 50)

    try:
        context = ssl.create_default_context()

        with socket.create_connection((target, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:

                cert = ssock.getpeercert()

                subject = get_name(cert.get("subject", ()))
                issuer = get_name(cert.get("issuer", ()))

                valid_from = cert.get("notBefore")
                valid_until = cert.get("notAfter")

                expiry = datetime.strptime(
                    valid_until,
                    "%b %d %H:%M:%S %Y %Z"
                ).replace(tzinfo=timezone.utc)

                now = datetime.now(timezone.utc)

                days_remaining = (expiry - now).days

                print(f"Target          : {target}")
                print(f"TLS Version     : {ssock.version()}")

                cipher = ssock.cipher()
                print(f"Cipher Suite    : {cipher[0]}")

                print(f"Subject CN      : {subject.get('commonName')}")
                print(f"Issuer CN       : {issuer.get('commonName')}")
                print(f"Organization    : {issuer.get('organizationName')}")

                print(f"Serial Number   : {cert.get('serialNumber')}")
                print(f"Valid From      : {valid_from}")
                print(f"Valid Until     : {valid_until}")
                print(f"Days Remaining  : {days_remaining}")

                print("\nSubject Alternative Names:")

                for san in cert.get("subjectAltName", []):
                    print(f"    {san[1]}")

    except socket.timeout:
        print("[-] Connection timed out")

    except ssl.SSLError as e:
        print(f"[-] SSL error: {e}")

    except socket.gaierror:
        print("[-] Unable to resolve hostname")

    except Exception as e:
        print(f"[-] Error: {e}")

    print("─" * 55)