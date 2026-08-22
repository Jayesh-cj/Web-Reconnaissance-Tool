import argparse

from modules.dns_enum import dns_records
from modules.domain import check_target
from modules.headers import get_security_headers
from modules.ip_info import get_ip_info
from modules.ssl import ssl_certificate
from modules.whois_lookup import get_whois_data

def main():
    # Parser initialization
    parser = argparse.ArgumentParser(
        description="Web Reconnaissance Framework"
    )

    # Target group initialization.
    target_group = parser.add_argument_group("Target")
    # Target
    target_group.add_argument(
        '-t', '--target', help="Target domain."
    )

    # Recon group initialization.
    recon_group = parser.add_argument_group("Reconnaissance options")


    # All modules.
    recon_group.add_argument(
        '-A', '--all', action='store_true', help="To run all reconnaissance modules."
    )
    # Whois lookup
    recon_group.add_argument(
        '-w', '--whois', action='store_true', help="To check whois information."
    )
    # DNS information
    recon_group.add_argument(
        '-d', '--dns', action='store_true', help="To check DNS records."
    )
    # IP information
    recon_group.add_argument(
        '-i', '--ip', action='store_true', help="To check ip information."
    )
    # Security headers 
    recon_group.add_argument(
        '-H', '--headers', action='store_true', help="To check HTTP headers."
    )
    # SSL information
    recon_group.add_argument(
        '-s', '--ssl', action='store_true', help="To check SSL/TLS information."
    )
    # robots.txt file
    recon_group.add_argument(
        '-r', '--robots', action='store_true', help="To check robots.txt file."
    )
    # sitemap.xml file
    recon_group.add_argument(
        '-m', '--sitemap', action='store_true', help="To check sitemap.xml file."
    )

    # Parse and use arguments
    args = parser.parse_args()

    modules_selected = (
        args.all or
        args.whois or 
        args.dns or
        args.ip or
        args.headers or
        args.ssl or
        args.robots or
        args.sitemap
    )

    if not modules_selected:
    
        if not args.target:
            parser.print_help()
            parser.error("Target domain must be provided using -t/--target")

            return
        
        else:
            check_target(args.target)
            print()

            parser.print_usage()

    else:
        if not args.target:
            parser.error("Target domain must be provided using -t/--target")

            return
        
        if args.whois:
            check_target(args.target)
            print()

            get_whois_data(args.target)

        elif args.dns:
            check_target(args.target)
            print()

            dns_records(args.target)

        elif args.ip:
            check_target(args.target)
            print()

            get_ip_info(args.target)

        elif args.headers:
            check_target(args.target)
            print()

            get_security_headers(args.target)

        elif args.ssl:
            check_target(args.target)
            print()

            ssl_certificate(args.target)

        elif args.robots:
            print("robots.txt")

        elif args.sitemap:
            print("Sitemap.xml")

        elif args.all:
            print("All modules")

        else:
            parser.print_help()


if __name__ == "__main__":
    main()
