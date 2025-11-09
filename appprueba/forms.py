
from django import forms

'''class nueva_tarea(forms.Form):

    titulo = forms.CharField()'''

'''class nueva_tarea(forms.Form):

    numero1 = forms.CharField();
    numero2 = forms.CharField();
    '''

class nueva_tarea(forms.Form):

    selecciones = forms.ChoiceField(
        choices=[('arg', 'Argentina'),('chita', 'china')])

    
