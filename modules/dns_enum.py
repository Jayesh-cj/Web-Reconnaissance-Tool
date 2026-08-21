import dns.resolver


# DNS records
def dns_records(target):
    record_types = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME",
        "SOA",
    ]

    print("\n[+] DNS Records")
    print("─" * 50)

    for type in record_types:

        try:
            records = dns.resolver.resolve(target, type)

            if type == "SOA":
                soa = records[0]

                print(f"\n{type} : ")
                
                print(f"    Primary NS : {soa.mname}")
                print(f"    Email      : {soa.rname}")
                print(f"    Serial     : {soa.serial}")
                print(f"    Refresh    : {soa.refresh}")
                print(f"    Retry      : {soa.retry}")
                print(f"    Expire     : {soa.expire}")
                print(f"    Minimum    : {soa.minimum}")

            else:

                print(f"\n{type} : ")

                for record in records:
                    print(f"    {record.to_text()}")

        except dns.resolver.NoAnswer:
            print(f"\n{type} Records : None")

        except dns.resolver.NXDOMAIN:
            print("\n[-] Domain does not exist")
            return

        except dns.resolver.NoNameservers:
            print(f"\n[-] No nameservers available for {type}")

        except dns.exception.DNSException as e:
            print(f"\n[-] {type} lookup failed: {e}")

    print("\n" + "─" * 50)
