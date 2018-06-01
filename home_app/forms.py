from django import forms


# Normal Acount Form
class NormalAccountForm(forms.Form):
    username = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    password = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Password',
                                      'type': 'password'})
    )
    office_key = forms.CharField(
        max_length=20, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Office Key',
                                      'type': 'password'})
    )


# Office & Admin Account Form
class OfficeAccountForm(forms.Form):
    office_name = forms.CharField(
        max_length=250, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Office Name'})
    )
    office_type = forms.ChoiceField(
        required=True, label='',
        widget=forms.Select(), choices=([('JOURNALISM', 'Journalism')])
    )
    username = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    password = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Password',
                                      'type': 'password'})
    )


# Announcaments Form
class AnnouncamentForm(forms.Form):
    content = forms.CharField(
        max_length=1000, label='', required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Announce ...',
                                     'id': 'announcament-content'})
    )
