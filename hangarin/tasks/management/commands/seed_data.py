from django.core.management.base import BaseCommand
from faker import Faker
from tasks.models import Task, Category, Priority
from django.utils import timezone
import random

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake categories, priorities, and tasks"

    def handle(self, *args, **kwargs):
        # --- Create priorities if not existing ---
        priority_names = ["Low", "Medium", "High"]
        for name in priority_names:
            Priority.objects.get_or_create(name=name)

        priorities = list(Priority.objects.all())

        # --- Create categories ---
        for _ in range(5):
            Category.objects.get_or_create(
                name=fake.word().capitalize(),
                defaults={'created_at': timezone.now()}
            )

        categories = list(Category.objects.all())

        # --- Create tasks ---
        for _ in range(20):
            Task.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                deadline=fake.future_datetime(end_date="+30d", tzinfo=timezone.utc),
                priority=random.choice(priorities),
                category=random.choice(categories),
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully added fake data!"))
