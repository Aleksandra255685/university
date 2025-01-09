from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TutorForm, ProfileEditForm
from .models import Tutor, Discipline, Workplace


def index(request):
    template_name = 'staff/index.html'
    staff = Tutor.objects.all()
    paginator = Paginator(staff, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
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


class RegisterView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('staff:index')


@login_required
def create_person(request):
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff:index')
    else:
        form = TutorForm()
    context = {
        'form': form
    }
    return render(request, 'staff/create.html', context)


@login_required
def edit_person(request, person_id):
    tutor = get_object_or_404(Tutor, id=person_id)
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_detail', person_id=person_id)
    else:
        form = TutorForm(instance=tutor)
    context = {
        'form': form
    }
    return render(request, 'staff/create.html', context)


@login_required
def delete_person(request, person_id):
    tutor = get_object_or_404(Tutor, id=person_id)
    if request.method == 'POST':
        tutor.delete()
        return redirect('staff:index')
    context = {
        'person': tutor
    }
    return render(request, 'staff/create.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': request.user,
        'profile': user,
    }
    return render(request, 'staff/profile.html', context)


@login_required
def edit_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff:profile',
                            username=request.user.username)
    else:
        form = ProfileEditForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'staff/user.html', context)
