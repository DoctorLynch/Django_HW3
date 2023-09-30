from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        category_list = [
            {'name': 'Фрукты', 'description': 'растут на деревьях', 'id': '1'},
            {'name': 'Овощи', 'description': 'растут на земле', 'id': '2'},
            {'name': 'Ягоды', 'description': 'растут и на земле, и на деревьях', 'id': '3'}

        ]

        for category_item in category_list:
            Category.objects.create(**category_item)
