from django.core.management.base import BaseCommand
from pages.models import ResearchInterests, TeacherMany
import pandas as pd


class Command(BaseCommand):
    """
    Class that handles populate_db argument.

    This class handles the command populate_db when we run 'python3 manage.py populate_db'. 
    """
    args = 'No arguments needed'
    help = 'Use python3 manage.py populate_db'

    # def _create_tags(self):
    #     pass
    # def save_iithyd():


    def handle(self, *args, **options):
        """
        Function that loads data into database.

        This function will use the web-scrapped data and will do data cleaning before saving it in the database.
        """
        iitm_final = pd.read_pickle("./pages/management/commands/web_scraping/iitm_final")
        iitk_final = pd.read_pickle("./pages/management/commands/web_scraping/iitk_final")
        iitd_final = pd.read_pickle("./pages/management/commands/web_scraping/iitd_final")
        iitkgp_final = pd.read_pickle("./pages/management/commands/web_scraping/iitkgp_final")
        iitb_final = pd.read_pickle("./pages/management/commands/web_scraping/iitb_final")
        print(list(iitm_final))
        print(list(iitk_final))
        print(list(iitd_final))
        print(list(iitkgp_final))
        print(list(iitb_final))


        # Gather all research areas first
        research_areas = set()

        for index, row in iitm_final.iterrows():
            # Split Logic
            this_row = row["Research Interests"]
            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            

            for area in areas:
                research_areas.add(area)
        print("IIT Madras reserach areas extracted")
        
        for index, row in iitk_final.iterrows():
            # Split Logic
            this_row = row["Research Interests"]
            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            

            for area in areas:
                research_areas.add(area)
        
        print("IIT Kanpur reserach areas extracted")

        for index, row in iitd_final.iterrows():
            # Split Logic
            this_row = row["Research Interests"]
            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            

            for area in areas:
                research_areas.add(area)
        
        print("IIT Delhi reserach areas extracted")

        for index, row in iitkgp_final.iterrows():
            # Split Logic
            this_row = row["Research Interests"]
            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            

            for area in areas:
                research_areas.add(area)
        
        print("IIT Kharagpur reserach areas extracted")

        for index, row in iitb_final.iterrows():
            # Split Logic
            this_row = row["Research Interests"]
            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            

            for area in areas:
                research_areas.add(area)
        
        print("IIT Bombay reserach areas extracted")


        # Saving research_areas set in database
        for area in research_areas:
            # print(area)
            research_table_row = ResearchInterests(name = area, info = "")
            research_table_row.save()
        # print(research_areas)

        print("Research Areas saved")

        # Storing all the teachers data in the database
        research_table = ResearchInterests.objects.all()
        for index, rows in iitm_final.iterrows():
            this_row = rows["Research Interests"]

            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")

            rows["EmailId"] = rows["EmailId"].replace(" [at] ","@")
            rows["EmailId"] = rows["EmailId"].replace(" [dot] ",".")

            teacher_table_row = TeacherMany(
                name=rows["Prof"],
                email=rows["EmailId"],
                citations_all=rows["citations_all"],
                citations_since_2016=rows["citations_since_2016"],
                hindex_all=rows["hindex_all"],
                hindex_since_2016=rows["hindex_since_2016"],
                i10index_all=rows["i10index_all"],
                i10index_since_2016=rows["i10index_since_2016"],
                links=rows["Google Scholar"],
                all_research_areas=rows["Research Interests"],
                college=rows["College"])
            teacher_table_row.save()

            for area in areas:
                research_table_row = research_table.get(name=area)
                # print(research_table_row)
                teacher_table_row.research_areas.add(research_table_row)
            # teacher_table_row.save()

        print("IIT Madras data saved")

        for index, rows in iitk_final.iterrows():
            this_row = rows["Research Interests"]

            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            # rows["EmailId"] = rows["EmailId"].replace(" [at] ","@")
            # rows["EmailId"] = rows["EmailId"].replace(" [dot] ",".")

            teacher_table_row = TeacherMany(
                name=rows["Prof"],
                email=rows["EmailId"],
                citations_all=rows["citations_all"],
                citations_since_2016=rows["citations_since_2016"],
                hindex_all=rows["hindex_all"],
                hindex_since_2016=rows["hindex_since_2016"],
                i10index_all=rows["i10index_all"],
                i10index_since_2016=rows["i10index_since_2016"],
                links=rows["Google Scholar"],
                all_research_areas=rows["Research Interests"],
                college=rows["College"])
            teacher_table_row.save()

            for area in areas:
                research_table_row = research_table.get(name=area)
                # print(research_table_row)
                teacher_table_row.research_areas.add(research_table_row)
            # teacher_table_row.save()
        print("IIT Kanpur data saved")

        for index, rows in iitd_final.iterrows():
            this_row = rows["Research Interests"]

            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            # rows["EmailId"] = rows["EmailId"].replace(" [at] ","@")
            # rows["EmailId"] = rows["EmailId"].replace(" [dot] ",".")

            teacher_table_row = TeacherMany(
                name=rows["Prof"],
                email=rows["EmailId"],
                citations_all=rows["citations_all"],
                citations_since_2016=rows["citations_since_2016"],
                hindex_all=rows["hindex_all"],
                hindex_since_2016=rows["hindex_since_2016"],
                i10index_all=rows["i10index_all"],
                i10index_since_2016=rows["i10index_since_2016"],
                links=rows["Google Scholar"],
                all_research_areas=rows["Research Interests"],
                college=rows["College"])
            teacher_table_row.save()

            for area in areas:
                research_table_row = research_table.get(name=area)
                # print(research_table_row)
                teacher_table_row.research_areas.add(research_table_row)
            # teacher_table_row.save()
        print("IIT Delhi data saved")

        for index, rows in iitkgp_final.iterrows():
            this_row = rows["Research Interests"]

            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            # rows["EmailId"] = rows["EmailId"].replace(" [at] ","@")
            # rows["EmailId"] = rows["EmailId"].replace(" [dot] ",".")

            teacher_table_row = TeacherMany(
                name=rows["Prof"],
                email=rows["EmailId"],
                citations_all=rows["citations_all"],
                citations_since_2016=rows["citations_since_2016"],
                hindex_all=rows["hindex_all"],
                hindex_since_2016=rows["hindex_since_2016"],
                i10index_all=rows["i10index_all"],
                i10index_since_2016=rows["i10index_since_2016"],
                links=rows["Google Scholar"],
                all_research_areas=rows["Research Interests"],
                college=rows["College"])
            teacher_table_row.save()

            for area in areas:
                research_table_row = research_table.get(name=area)
                # print(research_table_row)
                teacher_table_row.research_areas.add(research_table_row)
            # teacher_table_row.save()
        print("IIT Kharagpur data saved")

        for index, rows in iitb_final.iterrows():
            this_row = rows["Research Interests"]

            this_row = this_row.replace(", and", " and")
            this_row = this_row.replace(".", "")
            this_row = this_row.replace(";", ",")
            this_row = this_row.replace(" (a)",",")
            this_row = this_row.replace(" (b)",",")
            this_row = this_row.replace(" (c)",",")
            this_row = this_row.replace(" (d)",",")
            this_row = this_row.replace(" (e)",",")
            this_row = this_row.replace(" (f)",",")
            this_row = this_row.replace("(","")
            this_row = this_row.replace(")","")
            this_row = this_row.replace("latest:","")
            this_row = this_row.replace("especially ", "")
            areas = this_row.split(", ")
            # rows["EmailId"] = rows["EmailId"].replace(" [at] ","@")
            # rows["EmailId"] = rows["EmailId"].replace(" [dot] ",".")

            teacher_table_row = TeacherMany(
                name=rows["Prof"],
                email=rows["EmailId"],
                citations_all=rows["citations_all"],
                citations_since_2016=rows["citations_since_2016"],
                hindex_all=rows["hindex_all"],
                hindex_since_2016=rows["hindex_since_2016"],
                i10index_all=rows["i10index_all"],
                i10index_since_2016=rows["i10index_since_2016"],
                links=rows["Google Scholar"],
                all_research_areas=rows["Research Interests"],
                college=rows["College"])
            teacher_table_row.save()

            for area in areas:
                research_table_row = research_table.get(name=area)
                # print(research_table_row)
                teacher_table_row.research_areas.add(research_table_row)
            # teacher_table_row.save()
        print("IIT Bombay data saved")