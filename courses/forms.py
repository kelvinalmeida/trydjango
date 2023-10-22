from django import forms
from .models import Course

class CreateCourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = [
            'title',
        ] 

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if title.lower() == 'abc':
            raise forms.ValidationError("THIS TITLE IS NOT VALID.")
        
        return title