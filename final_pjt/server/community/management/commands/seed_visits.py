import random
from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed

from community.models import Review, Visit

class Command(BaseCommand):
    help= '커맨드를 통한 랜덤한 조회수 데이터 생성'
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=100,
            type=int,
            help=''
        )
    
    def handle(self, *args, **options):
        reviews = Review.objects.all()
        review_cnt = Review.objects.count()

        for review in reviews:
            Visit.objects.create(review=review, count=0)
        self.stdout.write(self.style.SUCCESS(f'{review_cnt} visits created!'))
