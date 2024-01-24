from django.db import models


class Flor(models.Model):
    nome = models.CharField('Nome da flor', max_length = 50, unique=True)
    quantidade = models.BigIntegerField('Quantidade')
    valor_unitario = models.DecimalField('Valor unitário', max_digits=7, decimal_places = 2)

    class  Meta:
        verbose_name_plural = 'Flores'

    def __str__(self):
        return f'Nome da flor: {self.nome}, Quantidade: {self.quantidade}, Valor: {self.valor_unitario:.2f}R$'
        