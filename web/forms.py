from django import forms
from .models import Flan,Contact,ContactForm

class FlanFormModel(forms.ModelForm):
    class Meta:
        model = Flan
        fields =['name','description','image_url','precio']

class ContactFormForm(forms.Form):
    customer_email=forms.EmailField(label='Correo')
    customer_name=forms.CharField(max_length=64, label='Nombre')
    message=forms.CharField(label='Mensaje')
    # customer_name = forms.CharField(
    #     label='Nombre',
    #     max_length=100,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Nombre completo'
    #     })
    # )
    # customer_email = forms.EmailField(
    #     label='Correo electrónico',
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Correo electrónico'
    #     })
    # )
    # message = forms.CharField(
    #     label='Mensaje',
    #     widget=forms.Textarea(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Escribe tu mensaje aquí...',
    #         'rows': 4
    #     })
    # )



#crear el modelo de contactFormModelForm

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Email',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
        widgets = {
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
















