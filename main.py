from pathlib import Path
from socket import gethostbyname_ex


GATEWAY_IP = "10.7.27.210"
DOMAINS_PATH = r"hostname.txt"
OUTPUT_PATH = r"static_rules.bat"
RULE = "ROUTE ADD {ip} MASK 255.255.255.255 {gateway} REM {domain}"
       
with open(Path(DOMAINS_PATH), encoding="utf-8") as inp, \
     open(Path(OUTPUT_PATH), "w") as out:

    for line in inp:
        domain = line.split("#", 1)[0].strip()
        if len(domain) == 0:
            continue
            
        ips = gethostbyname_ex(domain)[-1]
        for ip in ips:
            rule = RULE.format(
                ip=ip,
                gateway=GATEWAY_IP,
                domain=domain
            )
            out.write(f"{rule}\n")
        