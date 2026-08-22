# Web Reconnaissance Tool 🔎

A Python-based web reconnaissance tool designed to automate the initial information-gathering phase of web application security assessments.

The tool collects publicly accessible information about a target domain through multiple reconnaissance modules and provides the results through a simple command-line interface.

## Features

- IP Address Information
- WHOIS / RDAP Information
- DNS information
- HTTP Response Header Analysis
- Security Header Analysis
- SSL/TLS Certificate Information
- robots.txt Enumeration
- sitemap.xml Enumeration 
- Run Individual Modules
- Run All Modules with a Single Command

## Requirements

- Python 3.9+
- Internet connection

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Jayesh-cj/Web-Reconnaissance-Tool.git
cd Web-Reconnaissance-Tool
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage
```bash
./recon.py -t <target> [options]
```

## Display Help
```bash
python recon.py -h
```
```bash
usage: recon.py [-h] [-t TARGET] [-A] [-w] [-d] [-i] [-H] [-s] [-r] [-m]

Web Reconnaissance Framework

options:
  -h, --help            show this help message and exit

Target:
  -t, --target TARGET   Target domain.

Reconnaissance options:
  -A, --all             To run all reconnaissance modules.
  -w, --whois           To check WHOIS/RDAP information.
  -d, --dns             To check DNS records.
  -i, --ip              To check IP information.
  -H, --headers         To check HTTP headers.
  -s, --ssl             To check SSL/TLS information.
  -r, --robots          To check robots.txt file.
  -m, --sitemap         To check sitemap.xml file.
```