from django import forms
from .models import Producto
from .models import Fabrica


class ProductoForm(forms.ModelForm):
    nueva_fabrica = forms.CharField(
        max_length=255,
        required=False,
        label="Nueva Fábrica (si aplica)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe el nombre de una nueva fábrica...',
        })
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'fabrica', 'nueva_fabrica']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'descripcion': 'Descripción del producto',
            'fabrica': 'Fábrica asociada',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe brevemente el producto...',
            }),
            'fabrica': forms.Select(attrs={
                'class': 'form-control',
                'title': 'Seleccione una fábrica o créela en el campo inferior',  # Mensaje que aparecerá al pasar el mouse
            }),
        }

    def save(self, commit=True):
        producto = super().save(commit=False)
        nueva_fabrica_nombre = self.cleaned_data.get('nueva_fabrica')

        if nueva_fabrica_nombre:
            fabrica, created = Fabrica.objects.get_or_create(nombre=nueva_fabrica_nombre)
            producto.fabrica = fabrica

        if commit:
            producto.save()

        return producto
        
        
class FabricaForm(forms.ModelForm):
    class Meta:
        model = Fabrica
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la Fábrica',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


