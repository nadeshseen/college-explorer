from bs4 import BeautifulSoup
import requests
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

def iitm():
    """
    Finds all teachers in CSE IIT Madras

    This function scrapes teacher name and other relevant information from IIT Madras CSE website.
    """
    iitm_gs_url={'Mitesh Khapra':'https://scholar.google.com/citations?user=DV8z8DYAAAAJ&hl=en&oi=ao',
    'Balaraman Ravindran':'https://scholar.google.com/citations?user=nGUcGrYAAAAJ&hl=en&oi=ao',
    'Shweta Agrawal':'https://scholar.google.com/citations?user=uLkJ5_4AAAAJ&hl=en&oi=ao',
    'L A Prashanth':'https://scholar.google.com/citations?user=Q1YXWpoAAAAJ&hl=en&oi=ao',
    'Harish Guruprasad':'',
    'Arun Rajkumar':'https://scholar.google.com/citations?user=gytfaaoAAAAJ&hl=en&oi=ao',
    'Akanksha Agrawal':'https://scholar.google.com/citations?hl=en&user=V_2z1BEAAAAJ',
    'John Augustine':'https://scholar.google.com/citations?hl=en&user=en94k70AAAAJ',
    'Sutanu Chakraborti':'https://scholar.google.com/citations?hl=en&user=tosR5XgAAAAJ',
    'Ayon Chakraborty':'https://scholar.google.com/citations?hl=en&user=xKrkM1EAAAAJ',
    'Sukhendu Das':'https://scholar.google.com/citations?hl=en&user=nqDmEHUAAAAJ',
    'D. Janakiram':'',
    'V. Kamakoti':'',
    'Deepak Khemani':'https://scholar.google.com/citations?hl=en&user=lrcXaOkAAAAJ',
    'Nishad Kothari':'https://scholar.google.com/citations?hl=en&user=qnp2XGoAAAAJ',
    'P. Sreenivasa Kumar':'https://scholar.google.com/citations?hl=en&user=FbCn7fkAAAAJ',
    'Chandrashekar Lakshminarayanan':'',
    'Anurag Mittal':'https://scholar.google.com/citations?hl=en&user=mB9AZSAAAAAJ',
    'C. Siva Ram Murthy':'https://scholar.google.com/citations?hl=en&user=VjJFBjcAAAAJ',
    'Hema A. Murthy':'https://scholar.google.com/citations?hl=en&user=AQ8w2uEAAAAJ',
    'Madhu Mutyam':'https://scholar.google.com/citations?hl=en&user=HS4VEdYAAAAJ',
    'Kartik Nagar':'https://scholar.google.com/citations?hl=en&user=KiT5oNUAAAAJ',
    'V. Krishna Nandivada':'https://scholar.google.com/citations?hl=en&user=kbgu7ccAAAAJ',
    'Manikandan Narayanan':'https://scholar.google.com/citations?hl=en&user=f5gTDzAAAAAJ',
    'N.S. Narayanaswamy':'https://scholar.google.com/citations?hl=en&user=nGUg9VUAAAAJ',
    'Rupesh Nasre':'https://scholar.google.com/citations?hl=en&user=kfUNJb8AAAAJ',
    'Meghana Nasre':'https://scholar.google.com/citations?hl=en&user=zOFnkeMAAAAJ',
    'B. V. Raghavendra Rao':'https://scholar.google.com/citations?hl=en&user=jFu4ljYAAAAJ',
    'Chester Rebeiro':'https://scholar.google.com/citations?hl=en&user=ctxSQrwAAAAJ',
    'Jayalal Sarma':'https://scholar.google.com/citations?hl=en&user=OzXbU7kAAAAJ',
    'C. Chandra Sekhar':'https://scholar.google.com/citations?hl=en&user=rO5ZgW4AAAAJ',
    'Krishna Moorthy Sivalingam':'https://scholar.google.com/citations?hl=en&user=mn54pyMAAAAJ',
    'K. C. Sivaramakrishnan':'https://scholar.google.com/citations?hl=en&user=Kc2cHqYAAAAJ',
    'Aishwarya Thiruvengadam':'',
    'Yadu Vasudev':'https://scholar.google.com/citations?hl=en&user=CkNu_zAAAAAJ'}

    iitm_url='http://www.cse.iitm.ac.in/listpeople.php?arg=MSQwJCQ='
    prof_list_iitm=[]
    research_iitm=[]
    mail_iitm=[]
    req = requests.get(iitm_url)
    soup = BeautifulSoup(req.text, "html.parser")
    table=soup.find_all('table')[1]
    details=table.find_all('span')
    for info in details:
        li=list(info.stripped_strings)
        if(li[1]) in ['(Associate Professor)','(Professor)','(Assistant Professor)']:
            prof_list_iitm.append(li[0])
            research=li[-1].replace('Research Interests :','').strip()
            research_iitm.append(research)
            if len(li)==5:    
                mail_iitm.append(li[3].replace('Email :','').strip())
            elif len(li)==4:
                mail_iitm.append('NA')
            elif len(li)==6:
                mail_iitm.append(li[4].replace('Email :','').strip())

    prof_research_mail_iitm=[]
    for i in range(len(prof_list_iitm)):
        prof_research_mail_iitm.append([prof_list_iitm[i],research_iitm[i],mail_iitm[i]])
    #print(prof_research_mail_iitm)
    iitm_df = pd.DataFrame(prof_research_mail_iitm, columns = ['Prof', 'Research Interests','EmailId'])
    iitm_gs=get_prof_stats(iitm_gs_url)
    iitm_final=pd.merge(iitm_df,iitm_gs,on='Prof')
    gs_links=[]
    for index in iitm_final.index:
        prof=iitm_final['Prof'][index]
        gs_links.append(iitm_gs_url[prof])
    iitm_final['Google Scholar']=gs_links
    iitm_final.to_pickle("./iitm_final")
    return iitm_final


