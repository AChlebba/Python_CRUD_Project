from django.db import models
from django.core.urlresolvers import reverse


class Zawodnik(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    wiek = models.IntegerField()

    def __unicode__(self):
        return self.imie

    def get_absolute_url(self):
        return reverse('dziennik_posilkow:zawodnik_edit', kwargs={'pk': self.pk})


class Posilek(models.Model):
    zawodnik = models.ForeignKey(Zawodnik)
    produkt = models.CharField(max_length=200)
    ilosc = models.CharField(max_length=200)
    kalorie = models.IntegerField()

    def __unicode__(self):
        return "Posilek from: " + self.produkt

    def get_absolute_url(self):
        return reverse('dziennik_posilkow:posilek_edit', kwargs={'pk': self.pk})


