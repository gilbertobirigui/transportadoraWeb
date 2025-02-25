from django.db import models

# classe de Motorista
class Driver(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    first_name = models.CharField(max_length=40, verbose_name='Nome')
    last_name = models.CharField(max_length=35, verbose_name='Sobrenome')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    license_number = models.CharField(max_length=20, unique=True, verbose_name='Número da CNH')
    cell_number = models.CharField(max_length=15, verbose_name='Celular')
    whatsapp_number = models.CharField(max_length=15, verbose_name='WhatsApp')
    pix_account = models.CharField(max_length=60, verbose_name='Conta Pix')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=80, verbose_name='Endereço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    # Explicação dos atributos:
    # id: Identificador único do motorista, gerado automaticamente.
    # first_name: Nome do motorista.
    # last_name: Sobrenome do motorista.
    # birth_date: Data de nascimento do motorista.
    # license_number: Número da Carteira Nacional de Habilitação (CNH) do motorista, que deve ser único.
    # cell_number: Número do celular do motorista.
    # whatsapp_number: numero do whatsapp
    # email: Endereço de email do motorista.
    # address: Endereço residencial do motorista.
    # created_at: Data de criação do registro.
    # updated_at: Data da última atualização do registro.
    # is_active: Indica se o motorista está ativo ou não.



    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

