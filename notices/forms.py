from django import forms
from django.forms.widgets import TextInput, CheckboxInput
from notices.models import Notice

class NoticeCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        help_text="This will be displayed on the main page search table and should contain keywords for your notice.",
        widget=TextInput(attrs={'placeholder':'Enter the subject of your notice.'})
    )
    web = forms.URLField(
        max_length=200, 
        required=False,
        help_text="Provide a link with more info.", 
        initial="http://",
        widget=TextInput
        )
    active = forms.BooleanField(
        help_text="Deselect this to hide an out-of-date notice.",
        widget=CheckboxInput,
        initial=True,
        required=False
    )

    class Meta:
        model = Notice
        fields = ['title', 'category', 'body', 'web', 'email', 'phone', 'country', 'province', 'postal', 'active']
