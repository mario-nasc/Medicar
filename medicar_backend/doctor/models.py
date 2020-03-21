from django.db import models


class Specialty(models.Model):
    """Specialty Model"""

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        db_table = 'specialties'


class Doctor(models.Model):
    """Doctor Model"""

    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    especialidade = models.ForeignKey(
        Specialty, on_delete=models.CASCADE, null=True, blank=True)

    def minha_especialidade(self):
        return self.especialidade.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        db_table = 'doctors'
