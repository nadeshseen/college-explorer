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


def iitb():
    """
    Finds all teachers in CSE IIT Bombay

    This function scrapes teacher name and other relevant information from IIT Bombay CSE website.
    """
    url='https://www.cse.iitb.ac.in/people/faculty.php'
    prof_name=[]
    interests=[]
    email=[]
    gs_links=[]

    s=HTMLSession()
    r=s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, "html.parser")
    current=soup.find('div',attrs={'id':'current'})
    for profs in current.find_all('div',attrs={'class':'info'}):
        for name in profs.find_all('div',attrs={'class':'name'}):
            prof_name.append(name.text.strip())
        for i,info in enumerate(profs.find_all('div',attrs={'class':'email'})):
            for data in info.find_all('div',attrs={'class':'body'}):
                if (i ==0):
                    interests.append(data.text.strip())
                elif (i==1):
                    email.append(data.text.strip())	
        links=profs.find_all('a')
        if (len(links))<3:
            gs_url=''
            gs_links.append(gs_url)
            
        else:
            gs_url=links[2].get('href')
            gs_links.append(gs_url)
            #print(gs_links)
    

    for i,mail in enumerate(email):
        components=mail.split(",")[0].split(" ")
        email_final=components[0]+"@cse.iitb.ac.in" 
        email[i]=email_final.strip()	
    prof_research_mail_iitb=[]
    iitb_gs_url={}
    #print(len(prof_name))
    #print(len(interests))
    #print(len(gs_links))


    for i in range (len(email)):
        if (prof_name[i].find('Umesh Bellur')>=0):
            prof_name[i]='Umesh Bellur'
        dummy=[prof_name[i],interests[i],email[i],gs_links[i]]
        iitb_gs_url[prof_name[i]]=gs_links[i]
        prof_research_mail_iitb.append(dummy)
    ### END CODE HERE ###
    #assert(isinstance(details,list) and isinstance(details[0],list))
    #print(details)
    iitb_df = pd.DataFrame(prof_research_mail_iitb, columns = ['Prof', 'Research Interests','EmailId','Google Scholar'])
    #print(iitb_df.head())
    #print(iitb_gs_url)
    iitb_gs=get_prof_stats(iitb_gs_url)
    iitb_final=pd.merge(iitb_df,iitb_gs,on='Prof')
    iitb_final['College']='IIT Bombay'
    print(iitb_final)
    iitb_final.to_pickle("./iitb_final")
    return iitb_final





