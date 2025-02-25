
from django.db import models

# EXPLICAÇAO DOS CAMPOS ( ATRIBUTOS ) 
# entity_type: Tipo de entidade (Empresa, Cliente, Fornecedor).
# legal_name: Razão social da entidade.
# trade_name: Nome fantasia da entidade.
# cnpj: Cadastro Nacional da Pessoa Jurídica, que deve ser único.
# state_registration: Inscrição estadual da entidade.
# email: Endereço de email da entidade.
# postal_code: Código de Endereçamento Postal (CEP).
# address: Endereço da entidade.
# address_number: Número do endereço.
# address_complement: Complemento do endereço.
# neighborhood: Bairro.
# city: Cidade.
# state: Estado.
# phone_number: Número de telefone da entidade.
# cell_phone: Número de celular da entidade.
# whatsapp_number: Número de WhatsApp da entidade.
# contact: Nome do contato principal da entidade.
# company_date: Data de fundação da empresa.
# created_at: Data de criação do registro.
# updated_at: Data da última atualização do registro.
# is_active: Indica se a entidade está ativa ou não.


from django.db import models


# classe da entidade (cliente - fornecedor - empresa)
class Entity(models.Model):

    # entity_type: Tipo de entidade (Empresa, Cliente, Fornecedor).
    ENTITY_TYPES = [
        ('Company', 'Empresa'),
        ('Client', 'Cliente'),
        ('Supplier', 'Fornecedor'),
    ]
    
    
    # Tipo de pessoa (Pessoa Física ou Pessoa Jurídica).
    PERSON_TYPES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    id = models.AutoField(primary_key=True, verbose_name='ID')
    entity_type = models.CharField(max_length=10, choices=ENTITY_TYPES, verbose_name='Tipo de Entidade')
    person_type = models.CharField(max_length=1, choices=PERSON_TYPES, verbose_name='Tipo de Pessoa')
    legal_name = models.CharField(max_length=100, verbose_name='Razão Social')
    trade_name = models.CharField(max_length=100, verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    state_registration = models.CharField(max_length=20, verbose_name='Inscrição Estadual')
    email = models.EmailField(verbose_name='Email')
    postal_code = models.CharField(max_length=10, verbose_name='CEP')
    address = models.CharField(max_length=100, verbose_name='Endereço')
    address_number = models.CharField(max_length=10, verbose_name='Número')
    address_complement = models.CharField(max_length=50, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=50, verbose_name='Bairro')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='Estado')
    phone_number = models.CharField(max_length=15, verbose_name='Telefone')
    cell_phone = models.CharField(max_length=15, verbose_name='Celular')
    whatsapp_number = models.CharField(max_length=15, verbose_name='WhatsApp')
    contact = models.CharField(max_length=100, verbose_name='Contato')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    company_date = models.DateField(verbose_name='Data da Empresa')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        ordering = ['legal_name']
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return f'{self.legal_name} ({self.get_entity_type_display()})'


# Explicação dos novos campos no modelo DebtStatus:
# entity: Relacionamento um-para-um com a entidade correspondente.
# owes: Campo booleano para indicar se a entidade deve ou não.
# amount: Campo para armazenar o valor devido pela entidade.
# last_payment_date: Campo para registrar a data do último pagamento realizado pela entidade (opcional).


class DebtStatus(models.Model):
    entity = models.OneToOneField(Entity, on_delete=models.CASCADE, related_name='debt_status')
    owes = models.BooleanField(default=False, verbose_name='Deve')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Devido')
    last_payment_date = models.DateField(null=True, blank=True, verbose_name='Data do Último Pagamento')

    def __str__(self):
        return f'{self.entity.legal_name} - Deve: {self.owes}, Valor: {self.amount}'




