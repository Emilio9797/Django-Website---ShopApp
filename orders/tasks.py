# tutaj definiujemy zadania asynchorniczne za pomoce dekoratora @task

from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    " po zakonczonym powodzeniem utworzeniu obniektu zamowienia"
    "dekorator tas asynchornicznie wysle mail z potwierdzeniem do odbiorcy"

    order = Order.objects.get(id = order_id)
    subject = "Dziekujemy za zlozenie zamowienia nr {}.".format(order.id)
    message = "Twoje zamowienie {} zostalo przyjete i oczekuje na platnosc!".format(order.id)

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])

    return mail_sent
