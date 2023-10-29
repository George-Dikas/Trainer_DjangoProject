from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import TrainerForm
from .models import Trainer

def trainer_registration(request):
    data = {}
    data['title_tag'] = data['logo'] = 'Trainer Registration'
    data['button_tag'] = 'Submit'

    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer-list')

    form = TrainerForm()
    data['form'] = form
    return render(request, 'trainer_app/trainer_form.html', data)

def trainer_update(request, trainer_id, lastname, firstname):
    trainer = Trainer.objects.get(id=trainer_id)
    data = {}
    data['title_tag'] = data['logo'] = 'Trainer Update'
    data['button_tag'] = 'Update'

    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer-list')

    form = TrainerForm(instance=trainer)
    data['form'] = form
    return render(request, 'trainer_app/trainer_form.html', data)

def trainer_list(request): 
    paginator = Paginator(Trainer.objects.select_related('subject'), 7)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    data = {}
    data['title_tag'] = data['logo'] = 'List of Trainers'
    data['page_obj'] = page_obj

    return render(request, 'trainer_app/trainer_list.html', data)

def trainer_deletion(request, trainer_id):
    Trainer.objects.get(id=trainer_id).delete()
    return redirect('trainer-list')
    