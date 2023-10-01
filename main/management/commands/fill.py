from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        category_list = [
            {'name': 'Фрукты', 'description': 'растут на деревьях', 'id': '1'},
            {'name': 'Овощи', 'description': 'растут на земле', 'id': '2'},
            {'name': 'Ягоды', 'description': 'растут и на земле, и на деревьях', 'id': '3'}

        ]
        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

