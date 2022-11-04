from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

def get_prof_stats(gs_url):
    """
    Get professor details

    This function scrapes data of each professor for various fields on google scholar
    """
    all_prof_stats=[]
    count=0
    for prof in gs_url.keys():
        prof_stats=[]
        url=gs_url[prof]
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            for i,details in enumerate(soup.find_all('td',attrs={'class':'gsc_rsb_std'})):
                if (i==0):
                    citations_all=int(details.text)
                    #prof_stats.append(('citations_all',citations_all))
                elif (i==1):
                    citations_since_2016=int(details.text)
                    #prof_stats.append(('citations_since_2016',citations_since_2016))
                elif (i==2):
                    hindex_all=int(details.text)
                    #prof_stats.append(('hindex_all',hindex_all))
                elif (i==3):
                    hindex_since_2016=int(details.text)
                    #prof_stats.append(('hindex_since_2016',hindex_since_2016))
                elif (i==4):
                    i10index_all=int(details.text)
                    #prof_stats.append(('i10index_all',i10index_all))
                elif (i==5):
                    i10index_since_2016=int(details.text)
                    #prof_stats.append(('i10index_since_2016',i10index_since_2016))    

            data=[prof,citations_all,citations_since_2016,hindex_all,hindex_since_2016,i10index_all,i10index_since_2016]
            #print(data)
            all_prof_stats.append(data)    
            count=count+1
            print(count,"done")
        except:
            continue

    df = pd.DataFrame(all_prof_stats, columns = ['Prof', 'citations_all','citations_since_2016','hindex_all','hindex_since_2016','i10index_all','i10index_since_2016'])
    return df



def iitk():
    """
    Finds all teachers in CSE IIT Kanpur

    This function scrapes teacher name and other relevant information from IIT Kanpur CSE website.
    """
    iitk_gs_url={'Amey Karkare':'https://scholar.google.com/citations?user=WPLq_rQAAAAJ&hl=en&oi=ao',
    'Amitangshu Pal':'',
    'Anil Seth':'',
    'Arnab Bhattacharya':'https://scholar.google.com/citations?hl=en&user=Sk-JV9QAAAAJ',
    'Ashutosh Modi':'https://scholar.google.com/citations?hl=en&user=AWu6f60AAAAJ',
    'Debadatta Mishra':'https://scholar.google.com/citations?hl=en&user=tU4qk00AAAAJ',
    'Hamim Zafar':'https://scholar.google.com/citations?hl=en&user=4LeNas8AAAAJ',
    'Indranil Saha':'https://scholar.google.com/citations?hl=en&user=F6QSFGkAAAAJ',
    'Mainak Chaudhuri':'',
    'Manindra Agrawal':'https://scholar.google.com/citations?hl=en&user=UBXqggoAAAAJ',
    'Nisheeth Srivastava':'https://scholar.google.com/citations?hl=en&user=2dgYRikAAAAJ',
    'Nitin Saxena':'https://scholar.google.com/citations?hl=en&user=1Yl1h_YAAAAJ',
    'Piyush Rai':'https://scholar.google.com/citations?hl=en&user=D50grEgAAAAJ',
    'Preeti Malakar':'https://scholar.google.com/citations?hl=en&user=7HlDLQMAAAAJ',
    'Priyanka Bagade':'',
    'Purushottam Kar':'https://scholar.google.com/citations?user=MNXz0AoAAAAJ&hl=en&oi=ao',
    'Raghunath Tewari':'https://scholar.google.com/citations?hl=en&user=Ks3QdEUAAAAJ',
    'Rajat Mittal':'https://scholar.google.com/citations?hl=en&user=MMtSl4cAAAAJ',
    'Rajat Moona':'',
    'Sandeep Kumar Shukla':'https://scholar.google.com/citations?user=SKqctYsAAAAJ&hl=en&oi=ao',
    'Sanjeev Saxena':'',
    'Satyadev Nandakumar':'https://scholar.google.com/citations?hl=en&user=lMAxggwAAAAJ',
    'Subhajit Roy':'',
    'Sumit Ganguly':'https://scholar.google.com/citations?hl=en&user=XwNzJl0AAAAJ',
    'Sunil Simon':'',
    'Surender Baswana':'https://scholar.google.com/citations?hl=en&user=U42j5MkAAAAJ',
    'Swaprava Nath':'https://scholar.google.com/citations?hl=en&user=TlpsH9cAAAAJ',
    'Swarnendu Biswas':'https://scholar.google.com/citations?hl=en&user=1DTBPfcAAAAJ',
    'Urbi Chatterjee':'https://scholar.google.com/citations?hl=en&user=tb-hEXAAAAAJ',
    'Vinay P. Namboodiri':'https://scholar.google.com/citations?user=JyHi9OoAAAAJ&hl=en&oi=ao',
    }
    iitk_url='https://www.cse.iitk.ac.in/pages/Faculty.html'
    req = requests.get(iitk_url)
    soup = BeautifulSoup(req.text, "html.parser")
    prof_list_iitk=[]
    research_iitk=[]
    mail_iitk=[]
    for details in soup.find_all('div',attrs={'class':'col-md-9 team-w3ls-txt'}):
        prof=details.find('h5').text
        mail=details.find('h6').text
        email=mail[1:-1]+"@cse.iitk.ac.in"
        prof_list_iitk.append(prof)
        mail_iitk.append(email)
        try:
            research= details.find_all('p')[2].text
            if (research.find("+91")!=-1 or research.find("Leave")!=-1):
                research=details.find_all('p')[3].text
            if (research.find("Leave")!=-1):
                research=details.find_all('p')[4].text
            #print(research)
        except:
            research="NA"
        research_iitk.append(research)
    prof_research_mail_iitk=[]
    for i in range(len(prof_list_iitk)):
        prof_research_mail_iitk.append([prof_list_iitk[i],research_iitk[i],mail_iitk[i]])
    #print(prof_research_mail_iitk)
    iitk_df = pd.DataFrame(prof_research_mail_iitk, columns = ['Prof', 'Research Interests','EmailId'])
    iitk_gs=get_prof_stats(iitk_gs_url)
    iitk_final=pd.merge(iitk_df,iitk_gs,on='Prof')
    gs_links=[]
    for index in iitk_final.index:
        prof=iitk_final['Prof'][index]
        gs_links.append(iitk_gs_url[prof])
    iitk_final['Google Scholar']=gs_links
    iitk_final.to_pickle("./iitk_final")
    return iitk_final


