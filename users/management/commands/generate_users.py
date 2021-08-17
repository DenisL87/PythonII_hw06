from faker import Faker

from django.core.management.base import BaseCommand, CommandError

from users.models import User


class Command(BaseCommand):
    help = 'Creates users'
    def add_arguments(self, parser):
        parser.add_argument('no_of_users', nargs='+', type=int)

    def handle(self, *args, **options):
        if options['no_of_users'][0] > 0 and options['no_of_users'][0] < 11:
            fake = Faker()
            count = 0
            while count < options['no_of_users'][0]:
                User.objects.create(username=fake.name(), email=fake.email(), password=fake.password())
                count += 1
        else:
            raise CommandError
