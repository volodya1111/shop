from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from .models import Phone, Watch, Laptop


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'color', 'memory', 'price', 'description', 'image', 'category', 'on_main']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'color': TextInput(attrs={
                'placeholder': 'Цвет'
            }),
            'memory': NumberInput(attrs={
                'placeholder': 'Память'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Цена'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание'
            }),
            'category': Select(attrs={
                'selected': 'selected'
            })
        }


class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'color', 'memory', 'price', 'description', 'image', 'category', 'on_main']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'color': TextInput(attrs={
                'placeholder': 'Цвет'
            }),
            'memory': NumberInput(attrs={
                'placeholder': 'Память'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Цена'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание'
            }),
            'category': Select(attrs={
                'selected': 'selected'
            })
        }


class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ['name', 'color', 'price', 'description', 'image', 'category', 'on_main']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'color': TextInput(attrs={
                'placeholder': 'Цвет'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Цена'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание'
            }),
            'category': Select(attrs={
                'selected': 'selected'
            })
        }
