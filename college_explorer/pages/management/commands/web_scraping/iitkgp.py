from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import re
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

def iitkgp():
    """
    Finds all teachers in CSE IIT Kharagpur

    This function scrapes teacher name and other relevant information from IIT Kharagpur CSE website.
    """
    iitkgp_gs_url={'Abhijit Das':'https://scholar.google.com/citations?user=b_SfaMUAAAAJ&hl=en&oi=ao',
    'Abir Das':'https://scholar.google.com/citations?hl=en&user=L4yEk2UAAAAJ',
    'Animesh Mukherjee':'https://scholar.google.com/citations?user=lf7-deEAAAAJ&hl=en&oi=ao',
    'Anupam Basu':'https://scholar.google.com/citations?hl=en&user=AMidPUMAAAAJ',
    'Aritra Hazra':'https://scholar.google.com/citations?hl=en&user=nYazw20AAAAJ',
    'Arobinda Gupta':'https://scholar.google.com/citations?hl=en&user=vAiphMEAAAAJ',
    'Bhargab Bikram Bhattacharya':'https://scholar.google.com/citations?user=udxFQnwAAAAJ&hl=en&oi=ao',
    'Bivas Mitra':'https://scholar.google.com/citations?hl=en&user=mQ57itUAAAAJ',
    'Chittaranjan Mandal':'https://scholar.google.com/citations?hl=en&user=jkoZD_MAAAAJ',
    'Debasis Samanta':'',
    'Debdeep Mukhopadhyay':'https://scholar.google.com/citations?hl=en&user=lfhvrhYAAAAJ',
    'Dipanwita Roychaudhury':'https://scholar.google.com/citations?hl=en&user=F_MRaWYAAAAJ',
    'Indranil Sengupta':'https://scholar.google.com/citations?hl=en&user=Nf46wucAAAAJ',
    'Jayanta Mukhopadhyay':'',
    'K Sreenivas Rao':'https://scholar.google.com/citations?hl=en&user=TATEL2EAAAAJ',
    'Mainack Mondal':'https://scholar.google.com/citations?hl=en&user=AUllGoAAAAAJ',
    'Niloy Ganguly':'https://scholar.google.com/citations?hl=en&user=hCbFmUUAAAAJ',
    'Pabitra Mitra':'https://scholar.google.com/citations?hl=en&user=5bXSZPYAAAAJ',
    'Palash Dey':'https://scholar.google.com/citations?hl=en&user=BkDCPiIAAAAJ',
    'Pallab Dasgupta':'https://scholar.google.com/citations?hl=en&user=Pw4jS9sAAAAJ',
    'Partha Bhowmick':'https://scholar.google.com/citations?hl=en&user=ExC8yMUAAAAJ',
    'Partha Pratim Chakrabarti':'',
    'Pawan Goyal':'https://scholar.google.com/citations?hl=en&user=F14FHsIAAAAJ',
    'Pralay Mitra':'https://scholar.google.com/citations?hl=en&user=LPzuRBUAAAAJ',
    'Rajat Subhra Chakraborty':'https://scholar.google.com/citations?hl=en&user=ITIg9kkAAAAJ',
    'Rajib Mall':'https://scholar.google.com/citations?hl=en&user=dt2fhqYAAAAJ',
    'Sandip Chakraborty':'https://scholar.google.com/citations?hl=en&user=pQ6C8YAAAAAJ',
    'Saptarshi Ghosh':'https://scholar.google.com/citations?hl=en&user=7TmKZv0AAAAJ',
    'Shamik Sural':'https://scholar.google.com/citations?hl=en&user=zmtaYLIAAAAJ',
    'Somindu Chaya Ramanna':'',
    'Soumya K Ghosh':'https://scholar.google.com/citations?hl=en&user=wTtdGd4AAAAJ',
    'Soumyajit Dey':'https://scholar.google.com/citations?hl=en&user=XJI3nYIAAAAJ',
    'Sourangshu Bhattacharya':'https://scholar.google.com/citations?hl=en&user=IixRsP0AAAAJ',
    'Sudebkumar Prasant Pal':'https://scholar.google.com/citations?hl=en&user=NLt-RjAAAAAJ',
    'Sudeshna Sarkar':'https://scholar.google.com/citations?hl=en&user=AwP_bbsAAAAJ',
    'Sudeshna Kolay':'https://scholar.google.com/citations?hl=en&user=TIz3qpUAAAAJ',
    'Sudip Misra':'https://scholar.google.com/citations?hl=en&user=h33l-A8AAAAJ',
    'Sujoy Ghose':'https://scholar.google.com/citations?hl=en&user=Qrakjb8AAAAJ',
    'Swagato Sanyal':'https://scholar.google.com/citations?hl=en&user=fpwM8D8AAAAJ'}

    iitkgp_url='https://cse.iitkgp.ac.in/?faculty.html'
    prof_list_iitkgp=[]
    research_iitkgp=[]
    mail_iitkgp=[]
    s=HTMLSession()
    r=s.get(iitkgp_url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, "html.parser")
    for details in soup.find_all('font',attrs={'color':'#A52A2A'}):
        prof=details.find('a').find('b').text
        prof=re.sub(' +', ' ',prof)
        prof_list_iitkgp.append(prof)

    for details in soup.find_all('font',attrs={'size':'2.0em'}):
        text=details.text
        #print(text)
        #print("####################################")
        if(text.find('Research')>=0):
            research_iitkgp.append(text)
        if (text.find('Email')>=0):
            index=text.find('Email')+6
            mail=text[index:].strip()
            mail=mail.replace("[at]","@")
            mail_iitkgp.append(mail)    	

    prof_research_mail_iitkgp=[]
    for i in range(len(prof_list_iitkgp)):
        data=[prof_list_iitkgp[i],research_iitkgp[i].replace('Research Areas:',''),mail_iitkgp[i]]
        prof_research_mail_iitkgp.append(data)

    #f = open("profname.txt", "a")
    #for prof in prof_list_iitkgp:
    #	f.write(prof+"\n")
    #f.close()


    iitkgp_df = pd.DataFrame(prof_research_mail_iitkgp, columns = ['Prof', 'Research Interests','EmailId'])
    print(iitkgp_df.head())


    iitkgp_gs=get_prof_stats(iitkgp_gs_url)

    iitkgp_final=pd.merge(iitkgp_df,iitkgp_gs,on='Prof')
    #print(iitkgp_final)
    iitkgp_final['College']='IIT Kharagpur'
    gs_links=[]
    for index in iitkgp_final.index:
        prof=iitkgp_final['Prof'][index]
        gs_links.append(iitkgp_gs_url[prof])
    iitkgp_final['Google Scholar']=gs_links
    iitkgp_final.to_pickle("./iitkgp_final")
    return iitkgp_final




