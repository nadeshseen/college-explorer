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






def iitd():
    """
    Finds all teachers in CSE IIT Delhi

    This function scrapes teacher name and other relevant information from IIT Delhi CSE website.
    """
    iitd_gs_url={'Prem Kalra': '',
    'Aaditeshwar Seth': 'https://scholar.google.com/citations?hl=en&user=XpOIYBoAAAAJ',
    'Abhijnan Chakraborty': 'https://scholar.google.com/citations?hl=en&user=21oQO9oAAAAJ',
    'Abhilash Jindal': 'https://scholar.google.com/citations?hl=en&user=_af8suQAAAAJ',
    'Amit Kumar': '',
    'Amitabha Bagchi': 'https://scholar.google.com/citations?hl=en&user=U4g_OxEAAAAJ',
    'S. Arun-Kumar': '',
    'Ashish Chiplunkar': '',
    'M. Balakrishnan': 'https://scholar.google.com/citations?hl=en&user=e_749FUAAAAJ',
    'Chetan Arora': 'https://scholar.google.com/citations?hl=en&user=Q8cTLNMAAAAJ',
    'Huzur Saran': '',
    'Kolin Paul': 'https://scholar.google.com/citations?hl=en&user=6TWEO3IAAAAJ',
    'Mausam': 'https://scholar.google.com/citations?user=5y4YmFcAAAAJ&hl=en&oi=ao',
    'Maya Ramanath': 'https://scholar.google.com/citations?hl=en&user=y6BXzxIAAAAJ',
    'Naveen Garg': 'https://scholar.google.com/citations?user=wNRE148AAAAJ&hl=en&oi=ao',
    'Nikhil Balaji': 'https://scholar.google.com/citations?hl=en&user=TluJpDYAAAAJ',
    'Parag Singla': 'https://scholar.google.com/citations?hl=en&user=V49BsgMAAAAJ',
    'Preeti R. Panda': 'https://scholar.google.com/citations?hl=en&user=4Q2DOC4AAAAJ',
    'Ragesh Jaiswal': '',
    'Rahul Garg': 'https://scholar.google.com/citations?hl=en&user=1B4UlwUAAAAJ',
    'Rahul Narain': 'https://scholar.google.com/citations?hl=en&user=YUuWoPgAAAAJ',
    'Rijurekha Sen': 'https://scholar.google.com/citations?hl=en&user=yTPVlzgAAAAJ',
    'Rohan Paul': 'https://scholar.google.com/citations?hl=en&user=Cgp-L2UAAAAJ',
    'Sandeep Sen': 'https://scholar.google.com/citations?hl=en&user=GK7JUpkAAAAJ',
    'Sanjiva Prasad': '',
    'Sayan Ranu': 'https://scholar.google.com/citations?hl=en&user=K4w5qYUAAAAJ',
    'Smruti Ranjan Sarangi': '',
    'Sorav Bansal': 'https://scholar.google.com/citations?hl=en&user=VgCn1s4AAAAJ',
    'Srikanta Bedathur': 'https://scholar.google.com/citations?hl=en&user=ngfF2oAAAAAJ',
    'Subhashis Banerjee': '',
    'Subodh Kumar': '',
    'Subodh Vishnu Sharma': 'https://scholar.google.com/citations?hl=en&user=Xas65uoAAAAJ',
    'Vireshwar Kumar': 'https://scholar.google.com/citations?hl=en&user=E3PiJ4cAAAAJ',
    'Anshul Kumar': '',
    'Gautam Shroff': '',
    'Manik Varma': 'https://scholar.google.com/citations?hl=en&user=2efybZkAAAAJ',
    'Rajeev Shorey': 'https://scholar.google.com/citations?hl=en&user=X_KVUr8AAAAJ',
    'Yogish Sabharwal': '',
    'Anish Arora': '',
    'Gopalan Nadathur': '',
    'Karthikeyan Bhargavan': '',
    'Sanjeev Khanna': '',
    'B.N. Jain': '',
    'Deepak Kapur': '',
    'S.N. Maheshwari': '',
    'Umesh Vazirani': '',
    'S.C. Gupta': '',
    'Subhash Bhalla': ''}

    iitd_url='https://www.cse.iitd.ac.in/index.php/2011-12-29-23-14-30/faculty'
    prof_list_iitd=[]
    research_iitd=[]
    req = requests.get(iitd_url)
    soup = BeautifulSoup(req.text, "html.parser")
    for details in soup.find_all('td', attrs={'class':'pic', 'align':'left' ,'valign':"top"}):
        try:
            prof_list_iitd.append(details.find('a').text.strip())
            for i,p in enumerate(details.find_all('p')):
                if (i==1):
                    research_iitd.append(p.text)
                #print("p=",i," ",p.text)    
        except:
            continue

    prof_and_research_iitd=[]
    for i in range(len(research_iitd)):
        prof_and_research_iitd.append([prof_list_iitd[i],research_iitd[i]])
    emailids=['pkalra@cse.iitd.ac.in',
    'aseth@cse.iitd.ac.in',
    'abhijnan@cse.iitd.ac.in',
    'ajindal@cse.iitd.ac.in',
    'amitk@cse.iitd.ac.in',
    'bagchi@cse.iitd.ac.in',
    'sak@cse.iitd.ac.in',
    'ashishc@cse.iitd.ac.in',
    'mbala@cse.iitd.ernet.in',
    'chetan@cse.iitd.ac.in',
    'saran@cse.iitd.ac.in',
    'kolin@cse.iitd.ac.in',
    'mausam@cse.iitd.ac.in',
    'ramanath@cse.iitd.ac.in',
    'naveen@cse.iitd.ac.in',
    'nbalaji@cse.iitd.ac.in',
    'parags@cse.iitd.ac.in',
    'panda@cse.iitd.ac.in',
    'rjaiswal@cse.iitd.ac.in',
    'rahulgarg@cse.iitd.ac.in',
    'narain@cse.iitd.ac.in',
    'riju@cse.iitd.ac.in',
    'rohan@cse.iitd.ac.in',
    'ssen@cse.iitd.ac.in',
    'sanjiva@cse.iitd.ac.in',
    'sayanranu@cse.iitd.ac.in',
    'srsarangi@cse.iitd.ac.in',
    'sbansal@cse.iitd.ac.in',
    'srikanta@cse.iitd.ac.in',
    'suban@cse.iitd.ac.in',
    'subodh@cse.iitd.ac.in',
    'svs@cse.iitd.ac.in',
    'viresh@cse.iitd.ac.in',
    'anshul@cse.iitd.ac.in']
    prof_and_research_iitd=prof_and_research_iitd[:34]
    for i,elem in enumerate(prof_and_research_iitd):
        elem.append(emailids[i])
    prof_research_mail_iitd=prof_and_research_iitd
    iitd_df = pd.DataFrame(prof_research_mail_iitd, columns = ['Prof', 'Research Interests','EmailId'])
    iitd_gs=get_prof_stats(iitd_gs_url)
    iitd_final=pd.merge(iitd_df,iitd_gs,on='Prof')
    iitd_final['College']='IIT Delhi'
    gs_links=[]
    for index in iitd_final.index:
        prof=iitd_final['Prof'][index]
        gs_links.append(iitd_gs_url[prof])
    iitd_final['Google Scholar']=gs_links
    iitd_final.to_pickle("./iitd_final")
    return iitd_final





    