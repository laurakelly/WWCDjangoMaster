from mentor.models import ContactForm
from django.shortcuts import HttpResponseRedirect, render_to_response

def mentoring(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('mentor/contact.html', {
        'form': form,
        })
