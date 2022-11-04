from django.core.management.base import BaseCommand
from pages.models import ResearchInterests, TeacherMany

class Command(BaseCommand):
    """
    This class handles the command clear_db when we run 'python3 manage.py clear_db' which deletes all the data in database
    """
    args = 'No arguments needed'
    help = 'Use python3 manage.py clear_db'

    def handle(self, *args, **options):
        ResearchInterests.objects.all().delete()
        TeacherMany.objects.all().delete()
        