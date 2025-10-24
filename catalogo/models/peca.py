from django.db import models


class Peca(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    descricao = models.TextField(
        verbose_name='Descrição',
    )

    preco = models.DecimalField(
        verbose_name='Preço',
        max_digits=10,
        decimal_places=2,
    )

    quantidade = models.PositiveIntegerField(
        verbose_name='Quantidade',
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'catalogo'
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'
