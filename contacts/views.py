from django.shortcuts import (render ,
                              get_object_or_404 ,
                              redirect
                              )
from .models import (Contact ,
                     Email
                     )
from django.contrib.auth.decorators import login_required
from .forms import (EmailForm ,
                    ContactForm
                    )
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy , reverse
from django.core.mail import send_mass_mail
from django.conf import settings




def contacts_list(request):


    contacts = Contact.objects.all()
    emails = None

    new_email = None

    if request.method == 'POST':

        email_form = EmailForm(data=request.POST)
     
        if email_form.is_valid():

            email_cd = email_form.cleaned_data
            new_email = email_form.save(commit=False)
            new_email.is_selected = True
            new_email.save()      
        
    else:

        email_form = EmailForm()


    emails = Email.objects.all()
    selected_contacts = Contact.objects.filter(is_selected=True)

    return render(request,
                  'contacts_list.html',
                  {'contacts':contacts,
                   'email_form':email_form,
                   'emails':emails,
                   'selected_contacts':selected_contacts})





@require_POST
def select_contact(request , contact_id , contact_slug):

    
    contact = get_object_or_404(Contact,
                                id=contact_id,
                                slug=contact_slug)
    

    if not contact.is_selected:

        contact.is_selected = True
        contact.save()

    else:

        contact.is_selected = False
        contact.save()
    
    return redirect('contacts_all')





def create_contact(request):

    new_contact = None

    if request.method == "POST":

        form = ContactForm(data=request.POST,
                           files=request.FILES)

        if form.is_valid():

            new_contact = form.save(commit=False)
            new_contact.is_selected = True
            new_contact.save()

            return redirect('contacts_all')
    
    else:

        form = ContactForm()
    
    return render(request , 'contact_create.html' , {'form':form,
                                                      'new_contact':new_contact})




@require_POST
def delete_contact(request , contact_id , contact_slug):

    contact = get_object_or_404(Contact,
                                id=contact_id,
                                slug=contact_slug)
    

    contact.delete()
    
    return redirect('contacts_all')





class ContactUpdate(UpdateView):

    model = Contact
    form_class = ContactForm
    template_name = 'update_contact.html'
    success_url = reverse_lazy('contacts_all')






def delete_confirm(request , contact_id , contact_slug):

    contact = get_object_or_404(Contact,
                                id=contact_id,
                                slug=contact_slug)
    
    return render(request , 'delete_confirm.html' , {'contact':contact})






@require_POST
def delete_email(request , email_id):

    email = get_object_or_404(Email,
                              id=email_id)
    
    email.delete()
    return redirect('contacts_all')





def emails_sent(request):

    return render(request , 'emails_sent.html')






@require_POST
def send_emails(request):

    emails = Email.objects.all()
    selected_contacts = Contact.objects.filter(is_selected=True)
    

    selected_contacts_emails = [x.email for x in selected_contacts]
    
    messages = list()

    for email in emails:

        messages.append((email.subject,
                         email.message,
                         settings.EMAIL_HOST_USER,
                         selected_contacts_emails))
    
    messages = tuple(messages)
    send_mass_mail(messages , fail_silently=False)

    return redirect('emails_sent')
