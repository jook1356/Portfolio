import random
from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed

from django.contrib.auth import get_user_model
from community.models import Review
from movies.models import Movie

class Command(BaseCommand):
    help= '커맨드를 통한 랜덤한 리뷰 데이터 생성'
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=100,
            type=int,
            help='몇 개의 리뷰 데이터를 만들 것인가'
        )
    
    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()

        User = get_user_model()
        users = User.objects.all()

        movies = Movie.objects.all()
        fake = Faker(["ko-KR"])

        seeder.add_entity(
            Review,
            total,
            {   
                'vote':  lambda x: random.randint(0, 6),
                'user':  lambda x: random.choice(users),
                'movie':  lambda x: random.choice(movies),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} reviews created!'))
