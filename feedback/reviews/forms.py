<<<<<<< HEAD
from django import forms
from .models import Review

# Handles the form validation.
#class ReviewForm(forms.Form):
    #user_name = forms.CharField(
        #label="Your name", max_length=100, error_messages={
        #"required": "Your name must not be empty.",
        #"max_length": "Please enter a shorter name."})
    #review_text = forms.CharField(
        #label="Your feedback", widget=forms.Textarea, max_length=200)
    #rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

# Does the same as the code seen above, but using the forms provided by Django, 
# meaning it's much more powerfull and less code has to be writen.
class ReviewForm(forms.ModelForm):
    # 'Meta' is used to override built-in features provided in base code.
    class Meta:
        model = Review
        fields = "__all__"
        #exclude = [''] - should we want to exclude some field from the model.
        # Handles the labels that will be populated in the model.
        labels = {
            "user_name": "Your name",
            "review": "Your feedback",
            "rating": "Your rating"
        }
        # Handles any possible errors that might occur on the browser side.
        error = {
            "user_name": {
                "required": "Your name must not be empty.",
                "max_length": "Please enter a shorter name."
            }
=======
from django import forms
from .models import Review

# Handles the form validation.
#class ReviewForm(forms.Form):
    #user_name = forms.CharField(
        #label="Your name", max_length=100, error_messages={
        #"required": "Your name must not be empty.",
        #"max_length": "Please enter a shorter name."})
    #review_text = forms.CharField(
        #label="Your feedback", widget=forms.Textarea, max_length=200)
    #rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

# Does the same as the code seen above, but using the forms provided by Django, 
# meaning it's much more powerfull and less code has to be writen.
class ReviewForm(forms.ModelForm):
    # 'Meta' is used to override built-in features provided in base code.
    class Meta:
        model = Review
        fields = "__all__"
        #exclude = [''] - should we want to exclude some field from the model.
        # Handles the labels that will be populated in the model.
        labels = {
            "user_name": "Your name",
            "review": "Your feedback",
            "rating": "Your rating"
        }
        # Handles any possible errors that might occur on the browser side.
        error = {
            "user_name": {
                "required": "Your name must not be empty.",
                "max_length": "Please enter a shorter name."
            }
>>>>>>> 7db6920b4a9d41e78a548ec5f18a2925d35d29e3
        }