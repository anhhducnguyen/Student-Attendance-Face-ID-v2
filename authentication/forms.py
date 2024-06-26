from django import forms
from .models import TblStudents

class TblStudentsForm(forms.ModelForm):
    class Meta:
        model = TblStudents
        fields = ['name', 'email', 'phone', 'date_birth']



from .models import Classroom

class ClassroomSelectionForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), required=True, label="Select Classroom")
