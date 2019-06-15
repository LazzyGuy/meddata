import json
import sys
import csv
import requests
from bs4 import BeautifulSoup
import re

js = json.load(open("./2000.json", 'r'))
ids = js['IdList']
mega_count = 1

def get_url(id):
    return "https://www.ncbi.nlm.nih.gov/pubmed/"+id+"?report=xml&format=text"

urls = [ get_url(id) for id in ids ]

TITLE= "Page number,Author Name,Author affiliation,Email,Co-author 1 Name,Co-author 1 Affiliation,Co-author 1 Email,Co-author 2 Name,Co-author 2 Affiliation,Co-author 2 Email,Co-author 3 Name,Co-author 3 Affiliation,Co-author 3 Email,Co-author 4 Name,Co-author 4 Affiliation,Co-author 4 Email,Co-author 5 Name,Co-author 5 Affiliation,Co-author 5 Email,Co-author 6 Name,Co-author 6 Affiliation,Co-author 6 Email,Co-author 7 Name,Co-author 7 Affiliation,Co-author 7 Email,Co-author 8 Name,Co-author 8 Affiliation,Co-author 8 Email,Co-author 9 Name,Co-author 9 Affiliation,Co-author 9 Email,Article 1 Title,Article 1 URL,Article 1 Journal,Article 1 Pub Date,Article 1 Abstract,Article 2 Title,Article 2 URL,Article 2 Journal,Article 2 Pub Date,Article 2 Abstract,Article 3 Title,Article 3 URL,Article 3 Journal,Article 3 Pub Date,Article 3 Abstract,Article 4 Title,Article 4 URL,Article 4 Journal,Article 4 Pub Date,Article 4 Abstract,Article 5 Title,Article 5 URL,Article 5 Journal,Article 5 Pub Date,Article 5 Abstract,Article 6 Title,Article 6 URL,Article 6 Journal,Article 6 Pub Date,Article 6 Abstract,Article 7 Title,Article 7 URL,Article 7 Journal,Article 7 Pub Date,Article 7 Abstract,Article 8 Title,Article 8 URL,Article 8 Journal,Article 8 Pub Date,Article 8 Abstract,Article 9 Title,Article 9 URL,Article 9 Journal,Article 9 Pub Date,Article 9 Abstract,Article 10 Title,Article 10 URL,Article 10 Journal,Article 10 Pub Date,Article 10 Abstract"

TITLE_LIST = TITLE.split(",")


with open('out.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(TITLE_LIST)
csvFile.close()

def getEmail(aff):
    mail = []
    if aff == None:
        return ""
    else:
        af = aff.findAll('affiliation')
        for a in af:
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", a.text)
            if len(emails ) != 0:
                for _ in emails:
                    mail.append(_)
    if len(mail) == 0:
        return ""
    else:
        return ','.join(mail)

def getAff(aff):
    aff_all = []
    if aff == None:
        return ""
    else:
        af = aff.findAll('affiliation')
        for a in af:
            aff_all.append(a.text)

    if len(aff_all) == 0:
        return ""
    else:
        return ','.join(aff_all)

def get_uri(str):
    return "https://www.ncbi.nlm.nih.gov/pubmed/{}".format(str)


def convert_data(soup_list, page_no):
    # (email, name, aff)
    authors = []
    for soup in soup_list:
        auth_all = soup.findAll('author')
        for auth in auth_all:
            try:
                aff = auth.find('affiliationinfo')
                email = getEmail(aff)
                name = auth.find('forename').text + auth.find('lastname').text
                aff = getAff(aff)
            except:
                continue

            authors.append((name, aff, email))

    # (title , url, journal, pub_date, abstract)
    articles = []
    for soup in soup_list:
        try:
            title = soup.find('articletitle').text
            url = get_uri(soup.find('pmid').text)
            _journal = soup.find('journal')
            journal = _journal.find('title').text
            _pub_date = soup.find('pubdate')
            pub_date = _pub_date.find('medlinedate').text
            abs = soup.find('abstract')
            abstract = abs.find('abstracttext').text
        except:
            continue

        articles.append((title, url, journal, pub_date, abstract))

    print("Converting batch....")


    new_row = []

    new_row.append(page_no)
    x_count = 1
    temp_auth = []
    for aut in authors:
        if x_count == 10:
            break
        else:
            for x_ in aut:
                temp_auth.append(x_)
            x_count += 1

    x_count = 1
    temp_ar= []
    for aut in articles:
        if x_count == 10:
            break
        else:
            for x_ in aut:
                temp_ar.append(x_)
            x_count += 1

    if len(temp_auth) != 30:
        how = 30 - len(temp_auth)
        for __ in range(0, how):
            temp_auth.append("")

    if len(temp_ar) != 50:
        how = 50 - len(temp_ar)
        for __ in range(0, how):
            temp_ar.append("")

    print(len(temp_auth))
    print(len(temp_ar))


    new_row = new_row + temp_auth + temp_ar

    print(len(new_row))
    with open('out.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_row)

    csvFile.close()

    #End


COUNT = 0
BATCH=20
xml_soup_list = []
page_no = 0
for url in urls:
    print("strting with ", COUNT )
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    xml = soup.find('pre').text
    soupxml = BeautifulSoup(xml, 'lxml')

    COUNT += 1
    xml_soup_list.append(soupxml)

    if COUNT == BATCH:
        convert_data(xml_soup_list, page_no)
        xml_soup_list = []
        COUNT = 0
        page_no += 1


