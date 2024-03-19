from .models import UserProfile,Customer,User
# ...
class UserEditForm(forms.ModelForm):
 class Meta:
   model = Customer
   fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
  class Meta:
   model = UserProfile
   fields = ['date_of_birth', 'photo']