#!/usr/bin/env python3 
import sys
import argparse
import xml.etree.ElementTree as ET

# argparse
parser = argparse.ArgumentParser(description="Parse an Nmap XML file and print: Protocol + Hostname + Port")
parser.add_argument("-f", "--file", type=str, help="Nmap XML scan file", required=True)
args = parser.parse_args()

# Parse command line arguments
in_file = args.file
tree = ET.parse(in_file)
root = tree.getroot()

#print(root[3].attrib['task'])
for x in root:
  for y in x:
    for z in y:
      if z.tag == "hostname":
        #print(z.attrib["name"])
        host = z.attrib["name"]
      if z.tag == "port":
        #print(z.attrib["portid"])
        port = z.attrib["portid"]
        #print(host + ":" + port)
        if port == "80":
          print("http://" + host + ":" + port + "/")
        elif port == "443":
          print("https://" + host + ":" + port + "/")
        else:
          print("http://" + host + ":" + port + "/")
