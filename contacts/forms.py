from django import forms
from .models import Email , Contact


class EmailForm(forms.ModelForm):
    
    class Meta:

        model = Email
        fields = ['subject',
                  'message']
        
    
    def __init__(self , *args , **kwargs):

        super(EmailForm,self).__init__(*args , **kwargs)

        subject = self.fields['subject']
        message = self.fields['message']
        
        subject.widget.attrs['placeholder'] = 'subject'
        subject.widget.attrs['class'] = 'subject-field field'

        message.widget.attrs['placeholder'] = 'message'
        message.widget.attrs['class'] = 'message-field field'




class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['email',
                  'name',
                  'profile_picture']
    

    def __init__(self , *args , **kwargs):

        super(ContactForm,self).__init__(*args , **kwargs)

        email = self.fields['email']
        name  = self.fields['name']
        profile_picture = self.fields['profile_picture']

        email.widget.attrs['placeholder'] = 'Enter email'
        email.widget.attrs['class'] = 'email-field field'
        email.label = 'Email'


        name.widget.attrs['placeholder'] = 'Enter name'
        name.widget.attrs['class'] = 'name-field field'
        name.label = 'Name'
        
        profile_picture.label = 'Select an image for contact'
        profile_picture.widget.attrs['class'] = 'image-field'

