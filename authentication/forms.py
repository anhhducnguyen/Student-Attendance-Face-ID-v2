from django import forms
from .models import TblStudents
from .models import Classroom

class TblStudentsForm(forms.ModelForm):
    class Meta:
        model = TblStudents
        fields = ['name', 'email', 'phone', 'date_birth']

class ClassroomSelectionForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), required=True, label="Select Classroom")
