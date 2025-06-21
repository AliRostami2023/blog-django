import random
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.text import slugify
from faker import Faker
from article.models import Article, Category, Tag
from django.contrib.auth import get_user_model


User = get_user_model()


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
IMAGE_DIR = BASE_DIR / 'media' / 'fake-images'


class Command(BaseCommand):
    help = 'Generate fake articles with images, tags, and categories.'

    def handle(self, *args, **options):
        fake = Faker('en_US')

        default_categories = [
            {"title": "Technology", "slug": "technology"},
            {"title": "Lifestyle", "slug": "lifestyle"},
            {"title": "Health", "slug": "health"},
            {"title": "Economy", "slug": "economy"},
            {"title": "Arts & Culture", "slug": "arts-culture"},
        ]

        for cat in default_categories:
            obj, created = Category.objects.get_or_create(
                url_title=cat["slug"],
                defaults={"title": cat["title"], "published": True}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Category created: {cat['title']}"))

        image_list = [f"article-{i}.jpg" for i in range(1, 6)]
        categories = list(Category.objects.all())
        tags = ["science", "politics", "coding", "space", "design", "psychology"]

        # Create tags if they don't exist
        for t in tags:
            Tag.objects.get_or_create(tag=t, url_title=slugify(t))

        all_tags = list(Tag.objects.all())
        user = User.objects.filter(is_superuser=True).first()

        if not user:
            self.stdout.write(self.style.WARNING("❌ No superuser found. Please create one."))
            return

        for _ in range(15):
            title = fake.sentence(nb_words=4)
            slug = slugify(title, allow_unicode=True)
            body = fake.paragraph(nb_sentences=10)
            category = random.choice(categories)
            selected_image = random.choice(image_list)
            image_path = IMAGE_DIR / selected_image

            if not image_path.exists():
                self.stdout.write(self.style.WARNING(f"⚠️ Image not found: {image_path}"))
                continue

            with open(image_path, "rb") as img_file:
                image_file = File(img_file, name=selected_image)

                article = Article.objects.create(
                    author=user,
                    category=category,
                    title=title,
                    slug=slug,
                    body=body,
                    image=image_file,
                    published=True,
                    views=random.randint(0, 500),
                )

                article.tags.set(random.sample(all_tags, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS("✅ Fake articles created successfully."))
