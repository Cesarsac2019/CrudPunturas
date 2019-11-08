from django import forms
from .models import Pintura, Pintor


class PintorForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ('nombre', 'anio', 'actores')

    def __init__ (self, *args, **kwargs):
        super(PintorForm, self).__init__(*args, **kwargs)
        self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actores"].help_text = "Ingrese los pintores"
        self.fields["actores"].queryset = Actor.objects.all()
