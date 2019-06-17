import requests

url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%222018%22[Date+-+Publication]+:+%223000%22[Date+-+Publication])+AND+Journal+Article[ptyp]+AND+hasabstract[text]&retmax=1618112"

res = requests.get(url)
f = open('all.xml', 'w')
f.write(res.text)


