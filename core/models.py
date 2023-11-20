from django.db import models
from django.utils.translation import gettext_lazy as _
from isbn_field import ISBNField

class Libro(models.Model):
    titolo = models.CharField(_("Titolo"), max_length=50)
    autore=models.ForeignKey("Autore", verbose_name=_("Autore"), on_delete=models.CASCADE)
    genere=models.ForeignKey("Genere", verbose_name=_("Genere"), on_delete=models.CASCADE)
    


    class Meta:
        verbose_name = _("Libro")
        verbose_name_plural = _("Libri")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("Libro_detail", kwargs={"pk": self.pk})

class Autore(models.Model):

    nome = models.CharField(_("Nome"), max_length=50)
    cognome = models.CharField(_("Cognome"), max_length=50)
    data_di_nascita = models.DateField(_("Data di Nascita"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Autore")
        verbose_name_plural = _("Autori")

    def __str__(self):
        return self.nome+ " " + self.cognome

    def get_absolute_url(self):
        return reverse("Autore_detail", kwargs={"pk": self.pk})


class Genere(models.Model):

    nome = models.CharField(_("Nome"), max_length=50)

    class Meta:
        verbose_name = _("Genere")
        verbose_name_plural = _("Generi")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Genere_detail", kwargs={"pk": self.pk})
