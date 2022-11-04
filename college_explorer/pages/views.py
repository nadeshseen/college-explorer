from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import ResearchInterests, TeacherMany

# Create your views here.
def index(request):
    """
    Renders index.html

    This function renders index.html when user is on homepage.
    """
    return render(request, 'pages/index.html')

def contact(request):
        
    return render(request, 'pages/contact.html')
    
def research(request) :
    """
    Renders research.html

    This function renders research.html when user is on '/research' path. This also handles the search and sort functionality of this page.   
    """
    teachers_many = TeacherMany.objects.all().order_by('name')
    research_areas = ResearchInterests.objects.all().order_by('name')
    if request.method == "GET":
        form_value = request.GET
        form_research_area = form_value.get('form_research_area')
        form_sort = form_value.get('form_sort')
        if form_research_area != None:
            teachers_searched = teachers_many.filter(all_research_areas__icontains=form_research_area).order_by(form_sort)
            # teachers_searched = set()

            # for row in teachers_searched_entries:
            #     teachers_searched.add(row)
            # print(teachers_searched)
            return render(request, "pages/research.html", {
                "teachers_many_var": teachers_many,
                "teachers_searched_var": teachers_searched,
                "research_areas_var": research_areas,
            })
    
    return render(request, "pages/research.html", {
        "teachers_many_var": teachers_many,
        "research_areas_var": research_areas,
    })