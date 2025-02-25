
# Classe Entity
## Representa empresas, clientes e fornecedores.

### Atributos:  
- 
- `id`: Identificador único.
- `entity_type`: Tipo de entidade (Empresa, Cliente, Fornecedor).
- `person_type`: Tipo de pessoa (Pessoa Física ou Pessoa Jurídica).
- `legal_name`: Razão social da entidade.
- `trade_name`: Nome fantasia da entidade.
- `cnpj`: Cadastro Nacional da Pessoa Jurídica, único.
- `state_registration`: Inscrição estadual.
- `email`: Endereço de email.
- `postal_code`: Código de Endereçamento Postal (CEP).
- `address`: Endereço.
- `address_number`: Número do endereço.
- `address_complement`: Complemento do endereço.
- `neighborhood`: Bairro.
- `city`: Cidade.
- `state`: Estado.
- `phone_number`: Número de telefone.
- `cell_phone`: Número de celular.
- `whatsapp_number`: Número de WhatsApp.
- `contact`: Nome do contato principal.
- `is_active`: Indica se a entidade está ativa ou não.
- `company_date`: Data de fundação da empresa.
- `created_at`: Data de criação do registro.
- `updated_at`: Data da última atualização do registro.




# Classe Driver
## Representa motoristas.

### Atributos:
- `id`: Identificador único.
- `first_name`: Nome do motorista.
- `last_name`: Sobrenome do motorista.
- `birth_date`: Data de nascimento.
- `license_number`: Número da CNH, único.
- `cell_phone`: Número de celular.
- `whatsapp_number`: Número de WhatsApp.
- `email`: Endereço de email.
- `address`: Endereço.
- `pix_account`: Conta Pix.
- `is_active`: Indica se o motorista está ativo ou não.
- `created_at`: Data de criação do registro.
- `updated_at`: Data da última atualização do registro.



# Classe Vehicle
## Representa veículos.
### Atributos:

- `id`: Identificador único.
- `brand`: Marca do veículo.
- `model`: Modelo do veículo.
- `manufacturing_year`: Ano de fabricação.
- `color`: Cor do veículo.
- `license_plate`: Placa do veículo, única.
- `chassis_number`: Número do chassi, único.
- `owner`: Proprietário do veículo.
- `created_at`: Data de criação do registro.
- `updated_at`: Data da última atualização do registro.
- `is_active`: Indica se o veículo está ativo ou não.


# Classe DebtStatus
## Gerencia o status das dívidas das entidades.
### Atributos:
- `entity`: Relacionamento um-para-um com a entidade correspondente.
- `owes`: Indica se a entidade deve ou não.
- `amount`: Valor devido pela entidade.
- `last_payment_date`: Data do último pagamento realizado.


# Classe Freight
## Gerencia os fretes, relacionando motoristas, veículos e entidades.

### Atributos:
- `id`: Identificador único.
- `collection_date`: Data e hora da coleta.
- `company_code`: Relacionamento com a entidade que é uma empresa.
- `client_code`: Relacionamento com a entidade que é um cliente.
- `driver`: Relacionamento com o motorista responsável pelo frete.
- `vehicle`: Relacionamento com o veículo utilizado no frete.
- `notes`: Campo de texto para notas adicionais.
- `quantity_volume`: Quantidade de volumes transportados.
- `merchandise_value`: Valor da mercadoria transportada.
- `observation`: Campo de texto para observações.
- `additional_value`: Valor adicional do frete.
- `freight_value`: Valor base do frete.
- `total_freight_value`: Valor total do frete, somando `freight_value` e `additional_value`.
- `payment_days`: Dias para pagamento.
- `due_date`: Data de vencimento do pagamento.
- `payment_method`: Método de pagamento (boleto, pix, dinheiro, cartão, cheque).
- `created_at`: Data de criação do registro.
- `freight_status`: Situação do frete (pago, parcial, aberto).
# transportadoraWeb
