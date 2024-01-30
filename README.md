# API-Floricultura
API de estoque de flores
Desenvolvi com a framework Django e RestFramewok uma api que consome os principais verbos em um estoque virtual de flores. 
## Esta classe é a estrutura do banco de dados. nome com valor único, quantidade e valor unitário de preço de cada flor.
    class Flor(models.Model):
        nome = models.CharField('Nome da flor', max_length = 50, unique=True)
        quantidade = models.BigIntegerField('Quantidade')
        valor_unitario = models.DecimalField('Valor unitário', max_digits=7, decimal_places = 2)

        class  Meta:
            verbose_name_plural = 'Flores'
    
        def __str__(self):
            return f'Nome da flor: {self.nome}, Quantidade: {self.quantidade}, Valor: {self.valor_unitario:.2f}R$'**
    
## Na visualização:

    class FloresAPIView(generics.ListCreateAPIView):
        queryset = Flor.objects.all()
        serializer_class = FlorSerializers
   

    class FlorAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Flor.objects.all()
        serializer_class = FlorSerializers


## Processo de serialização

    class FlorSerializers(serializers.ModelSerializer):
        class  Meta:
            model = Flor
            fields = '__all__'
        
    
