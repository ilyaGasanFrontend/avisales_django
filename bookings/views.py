from django.shortcuts import render
from .forms import FlightForm
from .models import Flight
from django.core.paginator import Paginator
from .forms import TicketForm
from .models import Flight
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            # Сохранение данных из формы в базу данных
            form.save()
            # Перенаправление на другую страницу или вывод сообщения об успешном сохранении
    else:
        form = FlightForm()
    return render(request, 'bookings/add_flight.html', {'form': form})

def test_page(request):
    return render(request, 'bookings/test_page.html')

def flight_list(request):
    flights = Flight.objects.all()
    paginator = Paginator(flights, 3)  # Показывать по 3 элементов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookings/flight_list.html', {'page_obj': page_obj})


def buy_ticket(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.flight = flight
            ticket.save()
            # Уменьшение количества свободных мест
            flight.available_seats -= 1
            flight.save()
            return redirect('success_page')  # Перенаправление на страницу успешной покупки
    else:
        form = TicketForm()
    return render(request, 'bookings/buy_ticket.html', {'form': form})

def success_page(request):
    return render(request, 'bookings/success_page.html')