import sys
import argparse

def get_urls_append(url, payload):
    try:
        base_url, querys = url.split("?")
        for query in range(len(querys.split("&"))):
            q = querys.split("&")[query]
            urls.add(f"{base_url}?{q}{payload}{''.join(['&'+querys.split('&')[i] for i in range(len(querys.split('&'))) if i != query])}")
    except:
        pass
    
def get_urls_replace(url, payload):
    try:
        base_url, querys = url.split("?")
        for query in range(len(querys.split("&"))):
            q = querys.split("&")[query].split("=")[0]
            urls.add(f"{base_url}?{q}={payload}{''.join(['&'+querys.split('&')[i] for i in range(len(querys.split('&'))) if i != query])}")
    except:
        pass
parser = argparse.ArgumentParser()
parser.add_argument("--output", required=False, default="output.txt", help="Output file name")
args = parser.parse_args()

urls = set()

for url in sys.stdin.readlines():
    for payload in ["'0utlaw'", '"0utlaw"', '<b/0utlaw', "<b>0utlaw"]:
        get_urls_append(url=url.strip(), payload=payload)
        get_urls_replace(url=url.strip(), payload=payload)

with open(args.output, "w") as f:
    f.write("\n".join(urls))
