from django.db import models
from django.contrib.auth.models import User

class Deudas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    deudaTotal = models.IntegerField() 

class DetallesDeuda(models.Model):
    deuda = models.ForeignKey(Deudas, on_delete=models.CASCADE)
    valorMensual = models.IntegerField()
    calculoValor = models.IntegerField()
    cantidadCuota = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    finalizada = models.BooleanField()

    def calcular_valor_mensual(self):
        if self.cantidadCuota != 0:
            self.calculoValor = self.deuda.deudaTotal // self.cantidadCuota
        else:
            self.calculoValor = 0

    def save(self, *args, **kwargs):
        if not self.pk:
            self.calcular_valor_mensual()
            self.valorMensual = self.calculoValor
        else:
            if self.valorMensual == 0:
                self.calcular_valor_mensual()
                self.valorMensual = self.calculoValor    
        
        
        
        if self.cantidadCuota == 0:
            self.finalizada = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.descripcion} - Valor Mensual: {self.valorMensual}, Cuotas: {self.cantidadCuota}, Finalizada: {self.finalizada}"
    


    