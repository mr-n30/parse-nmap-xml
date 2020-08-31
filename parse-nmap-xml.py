#!/usr/bin/env python3 
import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
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
