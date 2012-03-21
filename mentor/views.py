from mentor.models import ContactForm
from django.shortcuts import HttpResponseRedirect, render_to_response
from django.core.context_processors import csrf
from django.core.mail import send_mail

def mentor(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            #recipients = ['llkelly88@gmail.com']
            #send_mail(form, recipients)
            return HttpResponseRedirect('/thanks/', c) # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('mentor/contact.html', {
        'form': form,
        }, c
    )
