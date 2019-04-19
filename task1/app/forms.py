from django import forms
from .models import Feedback_Form
class feedback(forms.ModelForm):
    class Meta:
        model =Feedback_Form
        fields=["f_name","l_name","email","comment"]