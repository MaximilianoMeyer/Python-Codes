#!/usr/bin/python3
#coding: utf-8

import requests
from spyse import spyse

s = spyse('key')

def request(url):
        try:
                return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
                pass

url = raw_input("[*] Enter url: ")

wordlist = raw_input("[*] Enter wordlist to use: ")

file = open(wordlist,"r")

for line in file:
        word = line.strip()
        full_url = word + "." + url
	subdomains = open("subdomains-found.txt","w")
	for item in full_url:
		subdomains.write("".join(item.strip()))
	subdomains.close()

        response = request(full_url)
        if(response):
                print("[+] Subdomain found: " + full_url)

	else:
		print("[-] Testing with: " + word)
