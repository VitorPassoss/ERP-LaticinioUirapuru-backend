from rest_framework import serializers
from apps.producao.models.produtos import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'



