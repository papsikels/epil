from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import CustomerUser, Costume, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class CostumeForm(forms.ModelForm):
    class Meta:
        model = Costume
        fields = ['name', 'description', 'photo1', 'photo2', 'photo3', 'status']

class BookmarkForm(forms.Form):
    costume_id = forms.IntegerField()

    def save(self, user):
        costume_id = self.cleaned_data['costume_id']
        costume = Costume.objects.get(pk=costume_id)
        Bookmark.objects.get_or_create(user=user, costume=costume)
        
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomerUser
        fields = ['full_name', 'username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data
    
class EditProfileForm(UserChangeForm):
    clear_profile = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput())
    class Meta:
        model = CustomerUser
        fields = ['full_name', 'profile', 'address', 'contact_number', 'birthdate','clear_profile']

        widgets = {
                'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control' }),
            }
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'old-password', 'class': 'form-control', 'placeholder':'leave blank if unchanged'}),
        strip=False,
        required=False,
    )

    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder':'leave blank if unchanged'}),
        strip=False,
        required=False,
    )

    new_password2 = forms.CharField(
        label=("Confirm new password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder':'leave blank if unchanged'}),
        strip=False,
        required=False,
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if old_password and not self.user.check_password(old_password):
            raise forms.ValidationError("Your old password was entered incorrectly. Please enter it again.")
        return old_password

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get('new_password1')
        old_password = self.cleaned_data.get('old_password')
        
        if not old_password and not new_password1:
            return new_password1  
        if len(new_password1) < 8:
            raise forms.ValidationError("This password is too short. It must contain at least 8 characters.")

        return new_password1
    
    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")
        
        return new_password2
        

