from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import TrainerForm
from .models import Trainer

def regTrainerView(request):
    data = {}
    data['title'] = 'Trainer Registration'
    data['logo'] = 'Trainer Registration'
    data['button'] = 'Submit'

    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listTrainerView')

    form = TrainerForm()
    data['form'] = form
    return render(request, 'trainer_app/trainer_form.html', data)

def updTrainerView(request, trainer_id, lastname, firstname):
    trainer = Trainer.objects.get(id=trainer_id)
    data = {}
    data['title'] = 'Trainer Update'
    data['logo'] = 'Trainer Update'
    data['button'] = 'Update'

    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('listTrainerView')

    form = TrainerForm(instance=trainer)
    data['form'] = form
    return render(request, 'trainer_app/trainer_form.html', data)

def listTrainerView(request): 
    paginator = Paginator(Trainer.objects.all(), 7)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  

    return render(request, 'trainer_app/trainer_list.html', {'page_obj':page_obj})

def delTrainerView(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('listTrainerView')