from django.db import models

# collection_date: Data e hora da coleta.
# company_code: Relacionamento com a entidade que é uma empresa.
# client_code: Relacionamento com a entidade que é um cliente.
# driver: Relacionamento com o motorista responsável pelo frete.
# vehicle: Relacionamento com o veículo utilizado no frete.
# notes: Campo de texto para notas adicionais, com limite de 255 caracteres.
# quantity_volume: Quantidade de volumes transportados.
# merchandise_value: Valor da mercadoria transportada.
# observation: Campo de texto para observações, com limite de 100 caracteres.
# additional_value: Valor adicional do frete.
# freight_value: Valor base do frete.
# total_freight_value: Valor total do frete, somando freight_value e additional_value.
# payment_days: Dias para pagamento.
# due_date: Data de vencimento do pagamento.
# payment_method: Método de pagamento (boleto, pix, dinheiro, cartão, cheque).
# created_at: Data de criação do registro.
# freight_status: Situação do frete (pago, parcial, aberto).


# classe Freight  ( frete )
class Freight(models.Model):
    FREIGHT_STATUS = [
        ('Paid', 'Pago'),
        ('Partial', 'Parcial'),
        ('Open', 'Aberto'),
    ]

    PAYMENT_METHODS = [
        ('Boleto', 'Boleto'),
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
        ('Cheque', 'Cheque'),
    ]

    id = models.AutoField(primary_key=True, verbose_name='ID')
    collection_date = models.DateTimeField(verbose_name='Data da Coleta')
    company_code = models.ForeignKey('Entity', on_delete=models.CASCADE, limit_choices_to={'entity_type': 'Company'}, verbose_name='Código da Empresa', related_name='company_freights')
    client_code = models.ForeignKey('Entity', on_delete=models.CASCADE, limit_choices_to={'entity_type': 'Client'}, verbose_name='Código do Cliente', related_name='client_freights')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, verbose_name='Motorista')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name='Veículo')
    notes = models.TextField(max_length=255, verbose_name='Notas', blank=True, null=True)
    quantity_volume = models.IntegerField(verbose_name='Quantidade de Volume')
    merchandise_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da Mercadoria')
    observation = models.CharField(max_length=100, verbose_name='Observação', blank=True, null=True)
    additional_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Acrescido', blank=True, null=True)
    freight_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Frete')
    total_freight_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total do Frete')
    payment_days = models.IntegerField(verbose_name='Dias para Pagamento')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, verbose_name='Forma de Pagamento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    freight_status = models.CharField(max_length=10, choices=FREIGHT_STATUS, verbose_name='Situação do Frete')

    class Meta:
        ordering = ['collection_date']
        verbose_name = 'Frete'
        verbose_name_plural = 'Fretes'

    def __str__(self):
        return f'Frete {self.id} - {self.collection_date}'

