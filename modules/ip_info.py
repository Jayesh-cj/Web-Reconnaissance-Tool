import socket


# Get ip information
def get_ip_info(target):
    print("\n[+] IP Address Information")
    print("-" * 50)

    try:
        data = socket.getaddrinfo(target, None, socket.AF_UNSPEC, socket.SOCK_STREAM)

        ipv4 = set()
        ipv6 = set()

        for result in data:

            family = result[0]
            address = result[4][0]

            if family == socket.AF_INET:
                ipv4.add(address)

            elif family == socket.AF_INET6:
                ipv6.add(address)

        print("IPv4 addresses:")

        if ipv4:
            for ip in ipv4:
                print(f"    {ip}")

        else:
            print("    None")

        print("\nIPv6 addresses:")

        if ipv6:
            for ip in ipv6:
                print(f"    {ip}")

        else:
            print("    None")

    except socket.gaierror:
        print("[-] Unable to resolve IP address")