from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from dziennik_posilkow.models import Zawodnik, Posilek

# ========== Forms =========

class ZawodnikForm(ModelForm):
    class Meta:
        model = Zawodnik
        fields = ['imie', 'nazwisko', 'wiek']

class PosilekForm(ModelForm):
    class Meta:
        model = Posilek
        fields = ['produkt', 'ilosc', 'kalorie']


# ========== Home =========

def home(request, template_name='dziennik_posilkow/home.html'):
    zawodnicy = Zawodnik.objects.all()
    ctx = {}
    ctx['zawodnicy'] = zawodnicy
    return render(request, template_name, ctx)
    

# ========== Zawodnik CRUD =========

def zawodnik_view(request, pk, template_name='dziennik_posilkow/zawodnik_view.html'):
    zawodnik= get_object_or_404(Zawodnik, pk=pk)
    posilki = Posilek.objects.filter(zawodnik=zawodnik)
    ctx = {}
    ctx["zawodnik"] = zawodnik
    ctx["posilki"] = posilki
    return render(request, template_name, ctx)

def zawodnik_create(request, template_name='dziennik_posilkow/zawodnik_form.html'):
    form = ZawodnikForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dziennik_posilkow:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def zawodnik_update(request, pk, template_name='dziennik_posilkow/zawodnik_form.html'):
    zawodnik= get_object_or_404(Zawodnik, pk=pk)
    form = ZawodnikForm(request.POST or None, instance=zawodnik)
    if form.is_valid():
        form.save()
        return redirect('dziennik_posilkow:home')
    ctx = {}
    ctx["form"] = form
    ctx["zawodnik"] = zawodnik
    return render(request, template_name, ctx)

def zawodnik_delete(request, pk, template_name='dziennik_posilkow/zawodnik_confirm_delete.html'):
    zawodnik= get_object_or_404(Zawodnik, pk=pk)    
    if request.method=='POST':
        zawodnik.delete()
        return redirect('dziennik_posilkow:home')
    ctx = {}
    ctx["object"] = zawodnik
    ctx["zawodnik"] = zawodnik
    return render(request, template_name, ctx)


# ========== Posilek CRUD =========

def posilek_create(request, parent_pk, template_name='dziennik_posilkow/posilek_form.html'):
    zawodnik = get_object_or_404(Zawodnik, pk=parent_pk)
    form = PosilekForm(request.POST or None)
    if form.is_valid():
        posilek = form.save(commit=False)
        posilek.zawodnik = zawodnik
        posilek.save()
        return redirect('dziennik_posilkow:zawodnik_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["zawodnik"] = zawodnik
    return render(request, template_name, ctx)

def posilek_update(request, pk, template_name='dziennik_posilkow/posilek_form.html'):
    posilek = get_object_or_404(Posilek, pk=pk)
    parent_pk = posilek.zawodnik.pk
    form = PosilekForm(request.POST or None, instance=posilek)
    if form.is_valid():
        form.save()
        return redirect('dziennik_posilkow:zawodnik_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["zawodnik"] = posilek.zawodnik
    return render(request, template_name, ctx)

def posilek_delete(request, pk, template_name='dziennik_posilkow/posilek_confirm_delete.html'):
    posilek = get_object_or_404(Posilek, pk=pk)    
    parent_pk = posilek.zawodnik.pk
    if request.method=='POST':
        posilek.delete()
        return redirect('dziennik_posilkow:zawodnik_view', parent_pk)
    ctx = {}
    ctx["object"] = posilek
    ctx["zawodnik"] = posilek.zawodnik
    return render(request, template_name, ctx)
