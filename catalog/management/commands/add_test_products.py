from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории, затем добавляет тестовые данные'

    def handle(self, *args, **kwargs):
        self.stdout.write('Очищаем базу данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('База данных очищена!'))

        self.stdout.write('Добавляем тестовые категории...')
        cat_electronics = Category.objects.create(
            name='Электроника',
            description='Гаджеты, телефоны, ноутбуки и другая техника'
        )
        cat_books = Category.objects.create(
            name='Книги',
            description='Художественная и техническая литература'
        )
        cat_home = Category.objects.create(
            name='Товары для дома',
            description='Всё для уюта и комфорта'
        )
        self.stdout.write(self.style.SUCCESS(f'Создано {Category.objects.count()} категорий'))

        self.stdout.write('Добавляем тестовые продукты...')
        Product.objects.create(
            name='Смартфон Alpha X1',
            description='Флагманский смартфон с AMOLED-экраном 6.7"',
            category=cat_electronics,
            price=59999.00
        )
        Product.objects.create(
            name='Ноутбук ProBook 15',
            description='Ноутбук для профессионалов: 16 ГБ ОЗУ, SSD 512 ГБ',
            category=cat_electronics,
            price=84999.00
        )
        Product.objects.create(
            name='Беспроводные наушники SoundMax',
            description='Наушники с активным шумоподавлением, 30 ч работы',
            category=cat_electronics,
            price=7999.00
        )
        Product.objects.create(
            name='Django для профессионалов',
            description='Полное руководство по веб-разработке на Django',
            category=cat_books,
            price=2500.00
        )
        Product.objects.create(
            name='Python. Сборник рецептов',
            description='Практические примеры и готовые решения на Python',
            category=cat_books,
            price=1800.00
        )
        Product.objects.create(
            name='Умная лампа LightUp',
            description='LED-лампа с управлением через приложение',
            category=cat_home,
            price=3499.00
        )
        Product.objects.create(
            name='Органайзер для рабочего стола',
            description='Бамбуковый органайзер с отделениями',
            category=cat_home,
            price=1299.00
        )

        self.stdout.write(self.style.SUCCESS(f'Создано {Product.objects.count()} продуктов'))
        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены!'))