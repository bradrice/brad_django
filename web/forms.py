from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message',)

        first_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset('Personal',
            Field('first_name', css_class='my_class'),
            'last_name',
            'email',
            css_class='large-12 columns'
        ),
            Fieldset('Message',
            'message',
            css_class='large-12 columns'
            )
        )
        self.helper.add_input(Submit("submit", "Send", css_class='button'))