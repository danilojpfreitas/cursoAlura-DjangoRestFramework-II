import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def validade_nome(nome):
    return nome.isalpha()

def validade_rg(rg):
    return len(rg) == 9

def validade_celular(celular):
    # Verifica se o celular é valido (11 91234-1234)
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' 
    resposta = re.findall(modelo, celular)
    return resposta


        
