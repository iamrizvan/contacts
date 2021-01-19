import contact
from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.


def index(request):
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    context = {
        'contacts': contacts,
        'search_input':search_input
    }
    return render(request, 'index.html', context)


def new_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new_contact.html')


def edit(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {
        'contact': contact
    }
    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', context)


def profile(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {
        'contact': contact
    }
    return render(request, 'profile.html', context)


def delete(request,pk):
    contact = Contact.objects.get(id=pk)
    context = {
        'contact':contact
    }
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', context)
