from . models import Review
from django import forms
from . models import Movie

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["author","stars","comment"]

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','description','title_upload_date','movie_cover']
