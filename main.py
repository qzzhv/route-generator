from itertools import chain
from pathlib import Path
from socket import getaddrinfo


GATEWAY_IP = "10.7.27.210"
DOMAINS_PATH = r"hostname.txt"
OUTPUT_PATH = r"static_rules.bat"
       
with open(Path(DOMAINS_PATH), encoding="utf-8") as inp, \
     open(Path(OUTPUT_PATH), "w") as out:
    
    domains = (domain.strip() for domain in inp if len(domain.strip()) > 0 and not domain.startswith("#"))
    ips = chain(*((ai[-1][0] for ai in getaddrinfo(domain, 0, 0, 0, 0) if "." in ai[-1][0]) for domain in domains))
    rules = (f"ROUTE ADD {ip} MASK 255.255.255.255 {GATEWAY_IP}" for ip in sorted(ips))
    print(*rules, sep="\n", file=out)
