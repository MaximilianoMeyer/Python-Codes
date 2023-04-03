#!/usr/bin/python3
#coding: utf-8

import requests
from certspotter.api import CertSpotter
import json
import sys

version = 1.2

token = 'token_telegram'
userID = 'chat_id'

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True, help='Target domain, without www.')
    parser.add_argument('-o', '--output', type=str, help='Output file')
    return parser.parse_args()


def banner():
    global version
    b = '''
    ####################
    #                  #
    # Subdomain finder #
    #                  #
    ####################
    '''.format(v=version)
    print(b)


def save_subdomains(subdomain,output_file):
    with open(output_file,"a") as f:
        f.write(subdomain + '\n')
        f.close()

    token = 'token_telegram'
    userID = 'chat_id'

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': userID, 'text': subdomain}
    requests.post(url, data)


def hackertarget():
    banner()
    args = parse_args()

    target = args.domain
    output = args.output

    hackertarget = requests.get("https://api.hackertarget.com/hostsearch/?q={d}".format(d=target))
    if(hackertarget.status_code != 200):
        print(":( Information not found")
        sys.exit()

    print("\n[!] ---- TARGET: {d} ---- [!] \n".format(d=target))

    print("[-] {s}".format(s=hackertarget.text))



hackertarget()


def certsh():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    certsh = requests.get("https://crt.sh/?q={d}&output=json".format(d=target))

    if(certsh.status_code != 200):
        print(":( Information not found")
        sys.exit()

    for (key,value) in enumerate(certsh.json()):
        subdomains.append(value['name_value'])

    subdomains = sorted(set(subdomains))

    for subdomain in subdomains:
        print("[-]  {s}".format(s=subdomain))
        if output is not None:
            save_subdomains(subdomain,output)


certsh()


def certspotter():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    api = CertSpotter("your_api_key")
    url = api.getdomains(target)

    subdomains.append(url)
    for i in subdomains:
        print(i)

    for subdomain in subdomains:
        print("[-] {s}".format(s=subdomains))
        if output is not None:
            save_subdomains(subdomain,output)


certspotter()


def urlscan():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    urlscan = requests.get("https://urlscan.io/api/v1/search/?q={d}".format(d=target))
    
    if(urlscan.status_code != 200):
        print(":( Information not found")
        sys.exit()

    print("[-] {s}".format(s=urlscan.text))


urlscan()


def threatcrowd():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    threatcrowd = requests.get("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={d}".format(d=target))

    if(threatcrowd.status_code != 200):
        print(":( Information not found")
        sys.exit()

    print("[-] {s}".format(s=threatcrowd.text))


threatcrowd()


def virustotal():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':'your_api_ket','domain':target}

    response = requests.get(url, params=params)

    print("[-] {s}".format(s=response.json()))


virustotal()


def wayback():
    args = parse_args()

    subdomains = []
    target = args.domain
    output = args.output

    wayback = requests.get('http://web.archive.org/cdx/search/cdx?url={d}&output=json&collapse=urlkey'.format(d=target))

    print(wayback.text)

wayback()
