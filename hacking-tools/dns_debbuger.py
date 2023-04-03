#!/usr/bin/python
#coding: utf-8

import dns.zone
import dns.resolver

def dns_debugger(domain):
    try:
        zone = dns.zone.from_xfr(dns.resolver.resolve(domain, 'AXFR'))
        print('Zone Transfer successful!')
        records = []
        for name, node in zone.nodes.items():
            rdatasets = node.rdatasets
            for rdata in rdatasets:
                if rdata.rdtype == 1:
                    records.append({"host": name.to_text(True), "ip": rdata.address})
        return records
    except:
        print('Zone Transfer failed!')
        return []

domain = input("Enter the domain name to scan: ")
records = dns_debugger(domain)
if records:
    print("IP Addresses and Hosts found in the database:")
    for record in records:
        print("Host:", record["host"], "IP:", record["ip"])
else:
    print("No records found.")
