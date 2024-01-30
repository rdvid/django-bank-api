from rest_framework import serializers, filters
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"Número de cpf inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"Campo nome não pode ter números"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"RG":"O RG precisa ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"Celular":"O número do celular deve seguir o padrão: (xx) 9xxxx-xxxx (respeitando espacos e tracos)"})
        return data
