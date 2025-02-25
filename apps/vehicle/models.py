from django.db import models

'''
brand: Marca (ex Ford, Chevrolet).
model: Modelo (Fiesta, Onix).
manufacturing_year: Ano de fabricação
color: Cor do veiculo
license_plate: Placa do veiculo
chassis_number: numero do chasssi
owner: proprietario
registration_date: data do cadastro

'''
# modelo de Veiculo
class Vehicle(models.Model):   # veiculo 
    id = models.AutoField(primary_key=True, verbose_name='ID')
    brand = models.CharField(max_length=50, verbose_name='Marca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    manufacturing_year = models.IntegerField(verbose_name='Ano de Fabricação')
    color = models.CharField(max_length=20, verbose_name='Cor')
    license_plate = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    chassis_number = models.CharField(max_length=17, unique=True, verbose_name='Número do Chassi')
    owner = models.CharField(max_length=100, verbose_name='Proprietário')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')  # Um campo de data/hora que registra a data de criação do registro
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')  # Um campo de data/hora que registra a data da última atualização do registro.
    is_active = models.BooleanField(default=True, verbose_name='Ativo')   # Um campo booleano para indicar se o veículo está ativo ou não.


    # A classe Meta está configurada para ordenar os veículos pela marca e o 
    # verbose_name está definido como "Veiculo", o que é útil para exibição 
    # em interfaces de administração.

    class Meta:
        ordering = ['brand']    # marca
        verbose_name = 'Veiculo'
    


    def __str__(self):
        return f'{self.brand} {self.model} ({self.manufacturing_year})'

