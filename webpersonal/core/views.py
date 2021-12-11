from django.shortcuts import render, HttpResponse

html_base ="""
    <h1> Mi web personal chingadamadre</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de...</a></li>
        <li><a href="/about2/">Portafolio...</a></li>
        <li><a href="/about3/">Contacto del grupo...</a></li>
    </ul>
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")
  

def about3(request):
    return render(request, "core/Contactos.html")
   