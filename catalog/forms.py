from django import forms
from django.forms import BooleanField
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('creator',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data.lower():
                raise ValueError('При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.'
                )

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data.lower():
                raise ValueError(
                    'При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.'
                )

        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_publication',)

        def clean_description(self):
            cleaned_data = self.cleaned_data.get('description')

            for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
                if i in cleaned_data.lower():
                    raise ValueError(
                        'При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.'
                    )

            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
