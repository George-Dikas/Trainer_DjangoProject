from django.forms import ModelForm
from .models import Trainer

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields=('lastname', 'firstname', 'phone', 'subject')

    def __init__(self, *args, **kwargs):
        super(TrainerForm,self).__init__(*args, **kwargs)
        self.fields['subject'].empty_label = "Select a subject"