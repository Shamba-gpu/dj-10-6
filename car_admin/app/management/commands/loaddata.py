import json, os

from django.core.management.base import BaseCommand
from app.models import Car, Review
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'app.json'), 'r') as json_file:
            data = json.load(json_file)

            for fields in data:
                model = fields['model']
                pk = fields['pk']
                field = fields['fields']

                if (model == 'app.car'):
                    brand = field['brand']
                    model = field['model']
                    Car.objects.create(id=pk, brand=brand, model=model)

                elif (model == 'app.review'):
                    title = field['title']
                    text = field['text']
                    car = field['car']

                    Review.objects.create(id=pk, title=title,text=text, car_id=car)
