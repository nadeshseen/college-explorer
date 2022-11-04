# College Explorer

Team Details:  
Team Name: RunTime Terror  
Team Members:  
* Shashank Prasad(21Q05R002)  
* Nadesh Seen(21Q050003)  
* Priyanshi Gupta(213050035)  

### Problem Statement/Motivation:  
Students pursuing Masters in a subject have some idea about the topics that they are interested in but do not know who will be the best professor to work with.  

### User Pain Points:  
1. A student must visit the faculty website of each college and filter across Research topics of every professor to finalize someone  
2. The faculty websites generally do not tell anything about the quality of research by the professor. For the student, it means going to another website (e.g: Google Scholar) to look at metrics like h-index and number of citations to assess the quality of research  

### College Explorer:  
College Explorer website is one-stop solution which solves both the mentioned problems. Given a research area by the student, it collates the list of faculties and their research quality statistics across multiple colleges. This single point of view helps a student decide quickly and saves hundreds of browsing hours.  

### Features:  
*  Details of faculty and their research quality statistics available to a student for 5 Top Engineering colleges just by entering the research keyword  
* Colleges Covered:  
    * IIT Bombay  
    * IIT Delhi  
    * IIT Kanpur  
    * IIT Madras  
    * IIT Kharagpur  
* In order to assess the quality of research, a student can sort list of teachers in 3 ways:  
    * Citations: Total number of citations received across all papers authored by the faculty  
    * h-index:  Maximum value of h such that the given author has published at least h papers that have each been cited at least h times  
    * i-10 index: Number of papers with at least 10 citations  

* A high value in any of the 3 metrics is considered good but a stand-alone value will not make sense to a student. These values need to be compared across faculties working on same research topic. This is where College Explorer’s single view feature adds value to the student  
* Based upon keyword entered, the final result also displays new /related fields of research that the teacher is working on. It is possible that the student was completely unaware about a research area and discovers it during browsing College Explorer.  
* The Google Scholar link of the teacher can be accessed by clicking on faculty’s name (in case the student is interested to explore a teacher’s work in more detail)  
* The email ID of the faculty provided is a quick and formal way to reach out to the faculty.  

### Technology Stack  
    * HTML/CSS/BootStrap for Front End-Design  
    * Django for Back-end development  
    * Python for web scraping  

### Deliverables:  
As discussed during mid-term review, we have developed a fully function user interface which displays details about faculty and their research quality statistics (for 5 colleges) based upon user’s input of research topic.  

### Software Requirements:
* HTML
* CSS
* BootStrap
* Django
* Python Libraries: BeautifulSoup, requests, pandas, regex
 
### How to Operate:  
1. On landing upon the home page, click on “Features” to know more about College Explorer  
2. Click on “Research Interest” . This will take you to another web-page.  
3. You can see a search-bar and a drop down at the top.   
4. Search for any research topic of your choice and select one of the 3 options from the drop-down menu: citations, h-index, i-10 index.  
5. Press Enter. You can see list of all teachers from the Top5 colleges whose research interests are similar to the key-word entered by you.  
6. Each teacher would be displayed as a card. These cards will be arranged in the descending order of the criteria selected by you from the drop-down.  
7. If you like the profile of a teacher and want to know more about them, click on their name mentioned at top of card.  
8. This would take you to the Google Scholar page of the teacher. Here you can explore in depth about the research papers published by the teacher.   

### Stakeholders of product:  
Students of C.S. Department who have completed their B.Tech and are looking for an appropriate guide for M.Tech/PhD based upon their research interests.  

### Team Contribution:  
1. Priyanshi Gupta:  
    * Front End Development  
    * PPT Slides  
2. Nadesh Seen:  
    * Back End Development  
    * Integration of back-end with front end  
    * Code Documentation using Sphinx  
3. Shashank Prasad  
    * Web Scraping logic from college websites and Google Scholar pages  
    * PPT Slides  
    * ReadMe document  

### Path to documentation:  
docs>_build>html>index.html  

### References - 

https://www.udemy.com/  
https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
https://www.educba.com/dropdown-list-in-html/