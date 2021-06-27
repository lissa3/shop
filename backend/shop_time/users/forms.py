from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _


User = get_user_model()

class UserCreationForm(forms.ModelForm):
    """ A form that creates a user with no privileges from the given email and
    password."""
    error_messages = {
        'duplicate_email': _('A user with that email address already exists.'),
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_('password'),
        widget = forms.PasswordInput
    )
    password2= forms.CharField(
        label = _('Password_confirmation'),
        widget = forms.PasswordInput,
        help_text=_('Enter the same password as above for verification')
    )

    class Meta:
        model = User
        fields=('email','first_name','last_name','password1','password2')


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = "Your Email Address"



    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password2 != password2:
            raise forms.ValidationError(self.error_messages["password_mismatch"])
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        # othewise password set fails
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ A form for updating users.
    Includes all the fields on the user, but replaces the password field with
    admin's password hash display field."""

    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text="Raw passwords are not stored, so there is no way to see "
                                                   "this user's password, but you can change the password "
                                                   "using <a href=\"password/\">this form</a>.")
    class Meta:
        model = User
        fields = ('email','groups',
                  'password','first_name','last_name','is_active','is_staff','is_superuser',
                  'user_permissions')



    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the field does
        not have access to the initial value.
        """
        return self.initial['password']