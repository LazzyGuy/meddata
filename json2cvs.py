import os
import json
import csv


data_dir = "./data/top100Json/"
file_paths = [ (os.path.join(data_dir, f), int(f[0:-5])) for f in os.listdir(data_dir)] 

def _(__):
    if __ == None:
        return " "
    else:
        return __


all_rows = []
main_row = ["PMID","DATE","MedlineJournalInfo(Country MedlineTA NlmUniqueID ISSNLinking)","Article Title","AbstractText","Author:Affiliations"]

last_row = []

last_row.append(main_row)

for f in file_paths:
    with open(f[0], 'r') as _f:
        data = json.load(_f)
        #-----------------
        pmid = data['PubmedArticle']['MedlineCitation']['PMID']['#text']
        #-----------------

        # date--------------
        date = data['PubmedArticle']['MedlineCitation']['DateRevised']

        date_year = date['Year']
        date_month = date['Month']
        date_day = date['Day']
        #-----------------

        #-----------------
        mji = data['PubmedArticle']['MedlineCitation']['MedlineJournalInfo']

        country = mji['Country']
        med_line_ta = mji['MedlineTA']
        ml_m_unique_id = mji['NlmUniqueID']
        issn_linking = mji.get('ISSNLinking')
        #-----------------

        #-----------------
        article = data['PubmedArticle']['MedlineCitation']['Article']
        author_list = article['AuthorList']['Author']
        authors = []

        print("====================", f[1])
        try:
            for ath in author_list:
                temp_auth = {}
                if ath.get('ForeName') == None:
                    temp_auth['Name'] = None
                else:
                    temp_auth['Name'] = ath.get('ForeName', None)+" "+ ath.get('LastName')
                try:
                    if ath.get('AffiliationInfo') == None:
                        temp_auth['Affiliation'] = None
                    else:
                        temp_auth['Affiliation'] = [ wtf['Affiliation'] for wtf in ath['AffiliationInfo']]
                except:
                    temp_auth['Affiliation'] = ath['AffiliationInfo']['Affiliation']

                authors.append(temp_auth)
        except:
            temp_auth_2 = {}
            ath = author_list
            temp_auth_2['Name'] = ath['ForeName']+" "+ath['LastName']
            try:
                temp_auth_2['Affiliation'] = [ wtf['Affiliation'] for wtf in ath['AffiliationInfo']]
            except:
                temp_auth_2['Affiliation'] = ath['AffiliationInfo']['Affiliation']

            authors.append(temp_auth_2)


        abstract_text = article['Abstract']['AbstractText']
        article_title = article['ArticleTitle']
        #-----------------


        # main_row = "PMID,DATE,MedlineJournalInfo(Country MedlineTA NlmUniqueID ISSNLinking),Article Title,Authers, Affiliation,AbstractText"
        print_date = _(date_year) +"-"+ _(date_month) +"-"+ _(date_day)
        print_mj = _(country) + " " + _(med_line_ta) + " " + _(ml_m_unique_id) + " " + _(issn_linking)

        # print("Auhters", authors)
        ab_text = ""
        if type(abstract_text) == type([]):
            temp_str = ""
            for qa in abstract_text:
                temp_str += qa['@NlmCategory']
                temp_str += ":"
                temp_str += qa['#text']
            ab_text= temp_str
        else:
            temp_str += qa['@NlmCategory']
            temp_str += ":"
            temp_str += qa['#text']
            ab_text= temp_str



        auth = ""

        print(auth)
        for aaa in authors:
            auth += _(aaa['Name']) + ":"
            aff = ""
            if type(aaa['Affiliation']) == type([]):
                for afg in aaa['Affiliation']:
                    aff += afg + ":"
            else:
                aff = aaa['Affiliation']

            print(aff)
            auth += _(aff)




        curr_row =[pmid,print_date,print_mj,article_title, ab_text, auth]
        last_row.append(curr_row)


with open('final.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(last_row)

csvFile.close()


