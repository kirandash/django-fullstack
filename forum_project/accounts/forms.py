from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form: Note, name of classes we are creating should be different from djangos pre defined class
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1',
                  'password2')  # Fields for form
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Labels for Form fields
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
