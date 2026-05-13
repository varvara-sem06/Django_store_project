from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        print("=" * 50)
        print(f"Сообщение от {name}")
        print(f"Email: {email}")
        print("Сообщение: {message}")
    
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')