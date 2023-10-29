from django.forms import ModelForm
from .models import Trainer


class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].empty_label = "Select a subject"
