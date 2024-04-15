from django import forms

from feedback.models import Feedback


# class UserForm(forms.Form):
#     name = forms.CharField() # -> html input
#     age = forms.IntegerField(required=False)

class AddFeedbackForm(forms.ModelForm):
    text = forms.CharField(
        label='ваш текст для отзыва',
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}),
        required=False,
    )
    class Meta:
        model = Feedback

        fields = ['text'] #'__all__'


