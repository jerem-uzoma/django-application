# add to the top
from collection.forms import ContactForm

# add to your views
def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })
