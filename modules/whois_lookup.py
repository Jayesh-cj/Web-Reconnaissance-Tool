import requests

# Get whois information
def get_whois_data(target):
    try:
        if target.startswith('www'):
            domain = target[4:]

        else:
            domain = target

        url = f"https://rdap.org/domain/{domain}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        registrar = None
        
        for entity in data.get("entities", []):
            if "registrar" in entity.get("roles", []):
        
                vcard = entity.get("vcardArray", [])
        
                if len(vcard) > 1:
                    for item in vcard[1]:
                        if item[0] == "fn":
                            registrar = item[3]
        
        # Extract dates
        registration_date = None
        expiration_date = None
        last_updated = None
        
        for event in data.get("events", []):
        
            action = event.get("eventAction")
            date = event.get("eventDate")

            if action == "registration":
                registration_date = date

            elif action == "expiration":
                expiration_date = date

            elif action == "last changed":
                last_updated = date
        
        # Extract nameservers
        name_servers = []
    
        for nameserver in data.get("nameservers", []):
            hostname = nameserver.get("ldhName")
    
            if hostname:
                name_servers.append(hostname)
    
        # DNSSEC
        dnssec = data.get("secureDNS", {}).get("delegationSigned")

        # Print information
        print("\n[+] WHOIS / RDAP Information")
        print("-" * 50)

        print(f"Domain Name     : {data.get('ldhName')}")
        print(f"Registrar       : {registrar}")
        print(f"Registration    : {registration_date}")
        print(f"Expiration      : {expiration_date}")
        print(f"Last Updated    : {last_updated}")
        print(f"DNSSEC          : {dnssec}")

        print("Status          :")
        for status in data.get("status", []):
            print(f"                  {status}")

        print("Name Servers    :")
        for nameserver in name_servers:
            print(f"                  {nameserver}")

        print("-" * 50)
    
    except requests.RequestException as e:
        print(f"[-] RDAP lookup failed!")

