from django import forms
# from .models import MyModel
# from django.core import validators
from django.forms.widgets import NumberInput
import datetime
from pra_app.models import My_Models

BIRTH_YEAR_CHOICES =  ['1980', '1981', '1982','1983']
FAVORITE_COLORS_CHOICES = [
    ('blue','Blue'),
    ('green','Green'),
    ('black','Black'),
]
class contact_Form(forms.Form):
    first_name = forms.CharField(initial='Your first name')
    name = forms.CharField(label="Enter your Full Name", required=False, initial='Your full name')
    comment = forms.CharField(min_length=50,required=False,initial='Give some comment',widget = forms.Textarea(attrs={'rows' : 3}))
    email = forms.EmailField(required=False, label="Enter your full name")
    roll = forms.IntegerField(help_text='Enter 5 digit roll')
    message = forms.CharField(min_length= 20, max_length=50)
    Agree = forms.BooleanField(required=False, initial=True)
    date = forms.DateField(required=True)
    Birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial= datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    my_colors = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)

    my_favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES) 

    my_multiple_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)

    file = forms.FileField()

    # model_choice = forms.ModelChoiceField(queryset= MyModel.objects.all(), initial=0)

    # model_choices = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=MyModel.objects.all(),initial=0)

    agree = forms.BooleanField(required=False)
   
class My_form(forms.ModelForm):
    class Meta:
        model = My_Models
        fields = '__all__'