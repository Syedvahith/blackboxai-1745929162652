from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seed the database with dummy categories and products'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        best_sellers = Category.objects.create(name='Best Sellers', slug='adilqadri-best-sellers')
        combos = Category.objects.create(name='Combos', slug='combo-offers')
        light = Category.objects.create(name='Light', slug='adilqadri-light-fragrance')
        oudh = Category.objects.create(name='Oudh', slug='adilqadri-oudh-collection')
        strong = Category.objects.create(name='Strong', slug='adilqadri-strong-fragrances')

        # Create products for Best Sellers
        Product.objects.create(
            category=best_sellers,
            name='Shanaya Luxury Attar Perfume',
            slug='shanaya-luxury-attar-perfume',
            description='Premium quality concentrated attar perfume.',
            price=399,
            discount_price=599,
            image_url='https://www.adilqadri.com/cdn/shop/files/SHANAYABOXandbottle5.5MLwhite.jpg?v=1731340134&width=400',
            rating=4.7,
            num_reviews=13762
        )

        # Create products for Combos
        Product.objects.create(
            category=combos,
            name='Perfume Discovery Set - Pack of 10 (5ml Each)',
            slug='perfume-discovery-set-10x5ml',
            description='A set of 10 premium perfume sprays.',
            price=999,
            discount_price=1999,
            image_url='https://www.adilqadri.com/cdn/shop/files/hero-img.jpg?v=1740055361&width=400',
            rating=4.6,
            num_reviews=100
        )

        self.stdout.write(self.style.SUCCESS('Database seeded with dummy categories and products'))
