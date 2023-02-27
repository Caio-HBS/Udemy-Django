from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["parent_post"]
        labels = {
            "username": "Seu nome de usuário",
            "user_email": "Seu E-mail",
            "rating": "Sua avaliação",
            "comment_text": "Seu comentário"
        }
        error_messages = {
            "username": {
                "required": "Este campo é obrigatório.",
                "max_length": "Limite de caracteres excedido."
            },
            "user_email": {
                "required": "Este campo é obrigatório.",
                "max_length": "Limite de caracteres excedido."
            },
            "comment_text": {
                "required": "Este campo é obrigatório.",
                "max_length": "Limite de caracteres excedido."
            }
        }