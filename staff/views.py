from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Tutor, Discipline, Workplace


def index(request):
    template_name = 'staff/index.html'
    staff = Tutor.objects.all()
    context = {'staff': staff}
    return render(request, template_name, context)


def staff_detail(request, person_id):
    template_name = 'staff/detail.html'
    person = get_object_or_404(Tutor, id=person_id)
    context = {'person': person}
    return render(request, template_name, context)


def discipline_tutor(request, discipline_slug):
    template_name = 'staff/discipline.html'
    discipline = get_object_or_404(Discipline, slug=discipline_slug)
    tutors = Tutor.objects.filter(disciplines=discipline)
    context = {'discipline': discipline,
               'tutors': tutors}
    return render(request, template_name, context)



