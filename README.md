# Parse Nmap XML
A program to parse Nmap XML output files and print: Protocol + Hostname + Port

## Installation:
```bash
git clone https://github.com/mr-n30/parse-nmap-xml.git \
&& cd parse-nmap-xml/ \
&& pip install -r requirements.txt \
&& ./parse-nmap-xml.py --help;
```

## Usage:
```bash
./parse-nmap-xml.py --file nmap-scan.xml
```
## Example output:
```bash
# ./parse-nmap-xml.py --file nmap-scan.xml
...
http://localhost:22/
http://localhost:80/
https://localhost:443/
http://localhost:8080/
...
```
