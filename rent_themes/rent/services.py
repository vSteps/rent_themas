from .models import *
import datetime

class RentServices():
    def salvarRent(self, request):
        comprou_antes = False
        a = Address(street = request.POST['street'],
            number = request.POST['number'],
            complement = request.POST['complement'], 
            district = request.POST['district'],
            city = request.POST['city'],
            state = request.POST['state'] )
        a.save()
        
        r = Rent(date=request.POST['date'], 
            start_hours=request.POST['start_hours'],
            end_hours=request.POST['end_hours'],
            client_id= request.POST['select_client'],
            theme_id = request.POST['select_theme'],
            address = a )


        t = Theme(price=request.POST['price'],)   

        given_date = datetime.datetime.strptime(r.date, "%Y-%m-%d")
        if not given_date.weekday() == 4 or given_date.weekday() == 5 or given_date.weekday() == 6:
            t.price = float(t.price) - (float(t.price) * 0.4)
        for i in Rent.objects.all():
            if i.client.id == r.client_id:
                comprou_antes = True
        if comprou_antes == True:
            t.price = float(t.price) - (float(t.price) * 0.10)
        if not (comprou_antes == False) and (given_date.weekday() == 5 or given_date.weekday() == 6 or given_date.isoweekday() == 7):
            t.price = float(t.price) - (float(t.price) * 0.5)

        return t.save() 