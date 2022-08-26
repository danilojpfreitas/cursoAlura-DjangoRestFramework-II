from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF não é valido"})
        if not validade_nome(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})
        if not validade_rg(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos"})
        if not validade_celular(data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir o seguinte modelo: 11 91234-1234"})
        return data 

