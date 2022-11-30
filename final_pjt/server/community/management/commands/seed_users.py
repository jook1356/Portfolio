import random
from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed

from django.contrib.auth import get_user_model
from community.models import Review
from movies.models import Movie

class Command(BaseCommand):
    help= '커맨드를 통한 랜덤한 유저 데이터 생성'
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=20,
            type=int,
            help='몇 명의 유저 데이터를 만들 것인가'
        )
    
    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()

        User = get_user_model()

        seeder.add_entity(
            User,
            total,
        )
        
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} users created!'))
