from django.shortcuts import render, redirect
from .models import Train, Ticket
from django.utils import timezone

# Home Page (List of Trains)




def train_list(request):
    trains = Train.objects.all()  # Fetch all trains
    return render(request, 'tickets/train_list.html', {'trains': trains})

# Book Ticket


def book_ticket(request, train_id):
    train = Train.objects.get(id=train_id)
    if request.method == 'POST':
        passenger_name = request.POST['passenger_name']
        age = int(request.POST['age'])  # Convert age to integer
        seat_number = int(request.POST['seat_number'])  # Convert seat_number to integer

        # Corrected: Pass the Train instance, not train_id
        ticket = Ticket.objects.create(
            train=train,  # Pass train instance
            passenger_name=passenger_name,
            age=age,
            seat_number=seat_number,
            booked_at=timezone.now()
        )

        return redirect('ticket_list')  # Redirect to booked tickets page

    return render(request, 'tickets/book_ticket.html', {'train': train})

# View Booked Tickets



def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})
