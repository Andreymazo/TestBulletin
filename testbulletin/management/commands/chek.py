
from django.core.management import BaseCommand

from config.settings import BASE_DIR

def ch():
   print(BASE_DIR)
      
class Command(BaseCommand):
   
    def handle(self, *args, **options):
    
      ch()
      
    