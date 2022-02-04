from attr import attrs
from django import forms
from .models import Trainee


class TraineeForm1(forms.Form):
    traineename = forms.CharField(
        max_length=20, label='Trainee Name ', required=True)
    traineetrack = forms.CharField(
        max_length=20, label='Trainee Track ', required=True)
    traineebdate = forms.DateField(label='Trainee Birthday ', required=True)
    traineeintake = forms.ChoiceField(label='Avaliable Intakes', choices=[
        ("1", "45"),
        ("2", "46")], required=True)
    traineepromotion = forms.DecimalField(
        label='Trainee Promotion', max_digits=5, decimal_places=1, required=True)

    class Meta:
        model = Trainee
        fields = '__all__'


class TraineeForm2(forms.ModelForm):

    traineename = forms.CharField(
        max_length=20, required=True)
    traineetrack = forms.CharField(
        max_length=20, required=True)
    traineebdate = forms.DateField(required=True)
    traineeintake = forms.ChoiceField(choices=[
        ("1", "45"),
        ("2", "46")], required=True)
    traineepromotion = forms.DecimalField(
        max_digits=5, decimal_places=1, required=True)

    class Meta:
        model = Trainee
        fields = '__all__'
