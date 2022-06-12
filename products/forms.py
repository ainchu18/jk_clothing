from django import forms
from .models import Product, Category, ReviewRating


class ProductForm(forms.ModelForm):
    """Add product form"""
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded'


class ReviewForm(forms.ModelForm):
    """Add a review rating form"""
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
