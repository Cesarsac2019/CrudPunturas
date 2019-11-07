from django import forms
from .models import Pintura, Pintor


class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ('nombre', 'anio', 'colores')

    def __init__ (self, *args, **kwargs):
        super(PinturaForm, self).__init__(*args, **kwargs)
        self.fields["colores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["colores"].help_text = "Ingrese los colores de para la pintura"
        self.fields["colores"].queryset = Pintor.objects.all()
