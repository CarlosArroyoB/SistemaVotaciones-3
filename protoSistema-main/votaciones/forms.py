from django import forms

class VotanteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    tipo_documento = forms.ChoiceField(choices=[("CC", "Cédula de ciudadanía"), ("CE", "Cédula de extranjería")])
    numero_documento = forms.CharField(max_length=20)
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')])
    localidad = forms.ChoiceField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])
    widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Documento'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
    }
