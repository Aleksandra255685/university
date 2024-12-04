from django.shortcuts import render
from django.http import Http404


staff = [
    {
        "id": 1,
        "name": "Иван Иванов",
        "workplace": "Кабинет 101",
        "load": 0.75,
        "disciplines": ["Математика", "Программирование"],
        "tasks": ["Кураторство", "Контроль публикаций"],
    },
    {
        "id": 2,
        "name": "Анна Смирнова",
        "workplace": "Кабинет 102",
        "load": 1.0,
        "disciplines": ["Физика", "Алгоритмы"],
        "tasks": ["Проведение практик"],
    },
]
STAFF_DICT = {p['id']: p for p in staff}


def index(request):
    template_name = 'staff/index.html'
    context = {'staff': reversed(staff)}
    return render(request, template_name, context)


def staff_detail(request, person_id):
    template_name = 'staff/detail.html'
    if person_id not in STAFF_DICT:
        raise Http404(f'Сотрудника с id {person_id} не существует!')
    context = {'person': STAFF_DICT[person_id]}
    return render(request, template_name, context)


def discipline_persons(request, discipline_slug):
    template_name = 'staff/discipline.html'
    context = {'discipline_slug': discipline_slug}
    return render(request, template_name, context)


def task_persons(request, task_slug):
    template_name = 'staff/category.html'
    context = {'task_slug': task_slug}
    return render(request, template_name, context)
