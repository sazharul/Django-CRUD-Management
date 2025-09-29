from django.core.management.base import BaseCommand
from store.models import Category, Subcategory, Brand, Product

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        # Seed Categories
        category_1 = Category.objects.create(name="Electronics", description="Devices and gadgets")
        category_2 = Category.objects.create(name="Clothing", description="Fashion and apparel")

        # Seed Subcategories
        subcategory_1 = Subcategory.objects.create(name="Mobile Phones", category=category_1, description="Smartphones and accessories")
        subcategory_2 = Subcategory.objects.create(name="Laptops", category=category_1, description="Laptops and accessories")
        subcategory_3 = Subcategory.objects.create(name="Men", category=category_2, description="Men's clothing")
        subcategory_4 = Subcategory.objects.create(name="Women", category=category_2, description="Women's clothing")

        # Seed Brands
        brand_1 = Brand.objects.create(name="Apple", description="Technology company specializing in smartphones and computers")
        brand_2 = Brand.objects.create(name="Samsung", description="Global leader in mobile and consumer electronics")
        brand_3 = Brand.objects.create(name="Nike", description="Sportswear and fashion brand")
        brand_4 = Brand.objects.create(name="Adidas", description="Sportswear and athletic gear")

        # Seed Products
        Product.objects.create(
            name="iPhone 13",
            description="Latest iPhone model with A15 Bionic chip",
            price=999.99,
            stock_quantity=100,
            brand=brand_1,
            subcategory=subcategory_1
        )
        Product.objects.create(
            name="Samsung Galaxy S21",
            description="Flagship smartphone with 5G support",
            price=799.99,
            stock_quantity=200,
            brand=brand_2,
            subcategory=subcategory_1
        )
        Product.objects.create(
            name="MacBook Pro 16-inch",
            description="High-performance laptop with M1 Pro chip",
            price=2499.99,
            stock_quantity=50,
            brand=brand_1,
            subcategory=subcategory_2
        )
        Product.objects.create(
            name="Nike Air Max 2021",
            description="Comfortable and stylish running shoes",
            price=129.99,
            stock_quantity=300,
            brand=brand_3,
            subcategory=subcategory_3
        )
        Product.objects.create(
            name="Adidas Ultraboost 21",
            description="Premium performance running shoes with Boost technology",
            price=179.99,
            stock_quantity=150,
            brand=brand_4,
            subcategory=subcategory_4
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
