from .models import *
import datetime
from django.shortcuts import get_object_or_404

class Util():
    def calcula_Desconto(self, a, r):
        desconto_cliente = 0
        desconto_semana = 0
        tema = get_object_or_404(Theme, pk = r.theme.id)
        cliente = get_object_or_404(Client, pk= r.client.id)

        a.save()

        given_date = datetime.datetime.strptime(r.date, "%Y-%m-%d")
        if not given_date.isoweekday() > 4:
            desconto_semana = tema.price * 0.40
            
        for i in Rent.objects.all():
            if i.client == r.client:
                desconto_cliente = tema.price * 0.10

        r.price = tema.price - (desconto_cliente + desconto_semana)
        return r.save() 