from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Blog!") # Простое представление, возвращающее текстовый ответ

def about(request):
    return HttpResponse('Новости блога')

def contact(request):
    return HttpResponse('Мои контакты')

def old_home(request):
    return HttpResponse('Старая главная страница блога')


# Подрубаем html файлы
def old_home_it_ansar(request):
    return render(request, 'old_home.html')

# Основное меню
def new_home_it_ansar(request):
    return render(request, 'new_ansar.html')

# Проекты компании
def project_ansar(request):
    data = {
        'intro': {
            'title': 'Проекты IT Ansar', 'lead': 'Мы создаём практичные решения для вашего бизнеса',
            'projects': [
                {
                    'title': 'Ansarium',
                    'description': 'Учебная платформа для разработчиков',
                    'features': ['Курсы', 'Автотесты', 'Сертификаты'],
                    'href': '/projects/ansarium/'
                },
                {
                    'title': 'Ansar_Biznes',
                    'description': 'Автоматизация бизнес-процессов',
                    'features': ['CRM', 'ERP', 'Аналитика', 'Отчёты'],
                    'href': '/projects/ansar_biznes/'
                }
            ],

        }
    }
    return render(request, 'project.html', context=data)

# Команда компании
def team_ansar(request):
    return render(request, 'team.html')

# Контакты
def contact(request):
    return render(request, 'contacts.html')


# Передача данных в контекстах

def index(request):
    header = 'Данные пользователя',
    lang = ['Python', 'Django', 'JavaScript', 'HTML', 'CSS']
    user = {
        'name': 'Ansar',
        'age': 20,
        }
    address = ('Абрикосная', 23, 45)

    data = {
        'header': header,
        'lang': lang,
        'user': user,
        'address': address,
    }
    # Пример шаблона jionja2
    '''
    <h1>{{ header }}</h1>

    <h2>Язык программирования</h2>
    <ul>
        {% for item in lang %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>

    <h2>Пользователь</h2>
    <p>Имя: {{ user.name }}</p>
    <p>Возраст: {{ user.age }}</p>

    <h2>Адрес</h2>
    <ul>
        <li>Улица: {{ address.0 }}</li>
        <li>Дом: {{ address.1 }}</li>
        <li>Квартира: {{ address.2 }}</li>
    </ul>
    '''
    return render(request, 'index.html', context=data)


# Задача 
def profile(request):
    context = {
    "meta": {"title": "Профиль — IT Ansar", "year": 2025},
    "nav_active": "home",  # или 'projects'/'team'/'contacts'
    "user": {
        "name": "Ибрагим",
        "tagline": "Python Backend / FastAPI",
        "bio": "Пишу продакшн-сервисы, люблю чистую архитектуру и измеримые метрики.",
        "age": 20,
        "email": "ibrahim@example.com",
        "website": "https://example.com",
        "profile_picture_url": ""  # или ссылка
    },
    "address": ["Грозный", "12", "34"],
    "lang": ["Python", "FastAPI", "Django", "PostgreSQL", "Docker"],
    "skills": ["SQLAlchemy", "AsyncIO", "CI/CD", "Unit-экономика (для продакта)"],
}
    return render(request, 'profile.html', context=context)
