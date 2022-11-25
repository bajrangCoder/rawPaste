import datetime
from django import forms
from django.apps import apps
from .models import Paste

config = apps.get_app_config("pastes")


class PasteForm(forms.Form):
    EXPIRATION_CHOICES = (
        (config.FIFTEEN_MINUTES, "15 minutes"),
        (config.ONE_HOUR, "1 hour"),
        (config.ONE_DAY, "1 day"),
        (config.ONE_WEEK, "1 week"),
        (config.ONE_MONTH, "1 month"),
        (config.SIX_MONTH, "6 month"),
        (config.ONE_YEAR, "1 year"),
    )
    
    title = forms.CharField(max_length=128,
                            required=False,
                            widget=forms.TextInput(attrs={"placeholder": "Untitled"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Awesome code goes here..."}))
    expiration = forms.ChoiceField(required=True,choices=EXPIRATION_CHOICES)
    lang = forms.ChoiceField(required=True,choices=config.LANGUAGES)
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        
        if self.request == None:
            raise AttributeError("'%s' requires a valid Django request object as its request parameter" % self.__class__.__name__)
        
        super(PasteForm, self).__init__(*args, **kwargs)
    
    def clean_title(self):
        """
        Replace the title with Untitled if it is not provided
        """
        title = self.cleaned_data.get("title")
        
        # If user provides an empty title, replace it with Untitled
        if title.strip() == "":
            title = "Untitled"
            
        return title
