from django.shortcuts import render, redirect
from .form import RegisterForm

def registration(response):
    if response.method == "POST":

        form = Registerfrom(respose.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form =RegisterForm()

    return render(response, "register/registration.html" ,{"form":form})
