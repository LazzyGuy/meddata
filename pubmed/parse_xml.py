import xml.dom.minidom as xmldom
import xml.etree.ElementTree as ET  
import re
import csv
class CoAuthor:
    def __init__(self,name,affiliation):
        self.name = name
        self.affiliation= affiliation



# Things required

#tree = ET.parse('xml/1.xml') 
#root = tree.getroot()
tree=None
root=None
page_num = 1
csvfile= None
article_count = 0
def main():
    for i in range(1,2000):
        print('--->'+str(i))
        global tree,root,article_count, csvfile
        csvfile = open('outpus.csv','a')
        tree = ET.parse('xml/'+str(i)+'.xml')
        article_count+=1
        root = tree.getroot()
        checkAuthor()
        #checkEmailId()
    csvfile.close()    


# Check contains email or not
#AUTHOR_LIST = root.findall('./MedlineCitation/Article/AuthorList/Author')


def checkEmailId():
    for elem in root.iter(tag='Affiliation'):
        email_list = re.findall('\S+@\S+', elem.text) 
        if(len(email_list)>0):
            fetchRemainData(email_list[0])


def checkAuthor():
    for elem in root.iter(tag='Author'):
        affiliation_info = elem.find('AffiliationInfo')
        if affiliation_info is None:
            continue
        else:
            email_text= affiliation_info.find('Affiliation').text
            email_list = re.findall('\S+@\S+', email_text)
            if(len(email_list)>0):
                firstName=""
                lastName=""
                if elem.find('ForeName').text is not None:
                    firstName = elem.find('ForeName').text
                if elem.find('LastName').text is not None:
                    lastName = elem.find('LastName').text
                fetchRemainData(email_list[0],firstName+lastName,email_text)

#for author in AUTHOR_LIST: 
#    AFFILATION = ET.SubElement(author,'AffiliationInfo/Affiliation')
    

# PMID
def getPMID():
    PMID = root.findall('./MedlineCitation/PMID')
    for id in PMID:
        pmid = id.text
        return pmid


# Article title
def getArticleTitle():
    ARTICLE_TITLE = root.findall('./MedlineCitation/Article/ArticleTitle')
    for article in ARTICLE_TITLE:
        articleTitle= article.text
        return articleTitle


def getArticle():
    abstract_text= ""
    for elem in root.iter(tag='AbstractText'):
        if elem.text is not None:
            abstract_text+=elem.text +" "
    return abstract_text

def getCoAuthorList():
    coauthor = []
    for elem in root.iter(tag='Author'):
        firstName=""
        lastName=""
        foreName = elem.find('ForeName')
        if foreName is not None:
            firstName = foreName.text
        LastName = elem.find('LastName')
        if LastName is not None:
            lastName = LastName.text
        affiliation=""
        affiliationinfo = elem.find('AffiliationInfo')
        if affiliationinfo is not None:
            affiliation = affiliationinfo.find('Affiliation').text
        coauthor.append(CoAuthor(firstName+lastName,affiliation))
    return coauthor    


def getArticlePubDate():
    pub =""
    for elem in root.iter(tag='PubDate'):
        if elem is not None:
            if elem.find('Day') is not None:
                pub+=elem.find('Day').text + '/'
            if elem.find('Month') is not None: 
                pub+=elem.find('Month').text + '/'
            if elem.find('Year') is not None: 
                pub+=elem.find('Year').text  
            break
    return pub


def getArticleJournal():
    pub =""
    for elem in root.iter(tag='Title'):
        if elem is not None:
            pub = elem.text
            break
    return pub




def fetchRemainData(email_id,authorName,authorAffiliation):
    global article_count, page_num
    if article_count > (page_num*100):
        page_num+=1
    email = email_id
    authorName = authorName
    authoraffiliation = authorAffiliation
    pmid = getPMID()
    articletitle = getArticleTitle() 
    article = getArticle()  
    coauthor = getCoAuthorList()
    page = page_num
    articleUrl = 'https://www.ncbi.nlm.nih.gov/pubmed/'+pmid 
    articlePubDate = getArticlePubDate()
    articleJournal = getArticleJournal()
   

    # Writing In Csv
    row = [pmid,page,email,authorName,authoraffiliation]
    for i in range(8):
        try:
            row.append(coauthor[i].name)
            row.append(coauthor[i].affiliation)
        except:
            row.append(" ")
            row.append(" ")
    row.append(articletitle)
    row.append(articlePubDate)
    row.append(articleJournal)
    row.append(articleUrl)
    row.append(article)
   
    if article_count==1:
        header = ['PMID','Page Num','Email','Author Name','Author Affiliation','Co Author 1','Co Author 1 Affiliation','Co Author 2','Co Author 2 Affiliation','Co Author 3','Co Author 3 Affiliation','Co Author 4','Co Author 4 Affiliation','Co Author 5','Co Author 5 Affiliation','Co Author 6','Co Author 6 Affiliation','Co Author 7','Co Author 7 Affiliation','Co Author 8','Co Author 8 Affiliation','Article Title','Publish Date','Article Journal','URL','Article']
        #csvfile =  open('output.csv','a')
        writer = csv.writer(csvfile)
        writer.writerow(header)
        #csvfile.close()


    #csvfile = open('output.csv','a')
    writer = csv.writer(csvfile)
    writer.writerow(row)
    #csvfile.close()

    row=[]
    print("-------------------------------------") 
    print(article_count)
    print(page_num)
    print("-------------------------------------")


if __name__ == '__main__':
    main()


    
