from django import forms
from.models import *


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['mobile', 'profile_pic', 'gender']
        GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )
class PublisherForm(forms.ModelForm):
    class Meta:
        model = publisher
        fields = ['certificate','mobile', 'profile_pic', 'gender']
        GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )


class movies_form(forms.ModelForm):
    class Meta:
        model = add_categories
        fields = (
        'uploader_name','title', 'category', 'image', 'screen_shot', 'discription', 'movie_length', 'actor_name', 'movie_director',
        'geners', 'movie_link', 'language')
        # labels = {
        #     'title': '',
        #     'category': '',
        #     'image': '',
        #     'screen_shot': '',
        #
        #     'discription': '',
        #     'movie_length': '',
        #     'actor_name': '',
        #     'movie_director': '',
        #     'language': '',
        #     'geners': '',
        #
        #     'movie_link': '',

        widgets = {
            'uploader_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the Name'}),
            'title': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie title'}),

            'actor_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the actor name'}),
            'movie_director': forms.TextInput(
                attrs={'class': 'sign__input', 'placeholder': 'Enter the movie director name'}),

            'discription': forms.TextInput(
                attrs={'class': 'sign__input', 'placeholder': 'Enter the movie description'}),
            'image': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),
            'screen_shot': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),

            'movie_length': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie duration'}),
            'movie_link': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie link'}),
            'language': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie language'}),
            'category': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie catagory'}),

            'geners': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie status'}),
        }




class publisher_form(forms.ModelForm):
    class Meta:
        model=add_categories
        fields=('uploader_name','title','category','image','screen_shot','discription','movie_length','actor_name','movie_director','geners','movie_link', 'language')
        # labels = {
        #     'title': '',
        #     'category': '',
        #     'image': '',
        #     'screen_shot': '',
        #
        #     'discription': '',
        #     'movie_length': '',
        #     'actor_name': '',
        #     'movie_director': '',
        #     'language': '',
        #     'geners': '',
        #
        #     'movie_link': '',



        widgets = {
            'uploader_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the Name'}),
            'title': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie title'}),


            'actor_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the actor name'}),
            'movie_director': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie director name'}),

            'discription': forms.TextInput(
                attrs={'class': 'sign__input', 'placeholder': 'Enter the movie description'}),
            'image': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),
            'screen_shot': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),

            'movie_length': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie duration'}),
            'movie_link': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie link'}),
            'language': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie language'}),
            'category':forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie catagory'}),

            'geners': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie status'}),
        }





