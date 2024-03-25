from django.shortcuts import render
import re

def myapp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if re.match(r'^[\w\.-]+@[\w\.-]+$', email):  # Regex for validating email
            username, domain = email.split('@')
            custom_message = f"Hello {username}, welcome from {domain}."
            return render(request, 'myapp/result.html', {'username': username, 'domain': domain, 'message': custom_message})
        else:
            return render(request, 'myapp/error.html')
    else:
        return render(request, 'myapp/emailform.html')
