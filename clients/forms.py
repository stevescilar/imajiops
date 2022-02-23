from django.forms import ModelForm
from .models import Client

class CLientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'