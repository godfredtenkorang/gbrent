from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'role', 'password1', 'password2']
        
        # Add widgets to customize the HTML input elements
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'role': forms.Select(attrs={'placeholder': 'Select role'}),
        }

    # Customizing password fields' placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
            # Mark email field as required
        
        self.fields['email'].required = True
    
    # Email validation
    
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is invalid')
        
        # Len function updated ###
        
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')
        return email
    

# Login Form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

    
    # Customizing password fields' placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter password'
        })