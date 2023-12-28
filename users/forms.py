from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import ForumUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=127, help_text="Required. Enter valid email address"
    )

    class Meta:
        model = ForumUser
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("username", css_class="col s12"),
                Column("email", css_class="col s12"),
            ),
            Row(
                Column("password1", css_class="col s6"),
                Column("password2", css_class="col s6"),
            ),
            Submit("submit", "Sign Up", css_class="btn waves-effect waves-light"),
        )
        self.field_order = ["username", "email", "password1", "password2"]
