from django.http import JsonResponse
from .models import Booking
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Page with no Frontent!")

def booking_listing(request):
    # Pagination
    page_number = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    # Sorting
    sort_by = request.GET.get('sort_by', 'ticket_id')
    bookings = Booking.objects.order_by(sort_by)

    # Searching
    search_query = request.GET.get('search', '')
    if search_query:
        bookings = bookings.filter(ticket_id__icontains=search_query)

    paginated_bookings = list(bookings[start_index:end_index].values())

    return JsonResponse(paginated_bookings, status=200)

def booking_details(request, ticket_id):
    try:
        booking = Booking.objects.get(ticket_id=ticket_id)
        booking_data = {
            'ticket_id': booking.ticket_id,
            'trip_id': booking.trip_id,
            'traveller_name': booking.traveller_name,
            'traveller_number': booking.traveller_number,
            'ticket_cost': str(booking.ticket_cost),
            'traveller_email': booking.traveller_email
        }

        return JsonResponse(booking_data, status=200)
    except Booking.DoesNotExist:
        return JsonResponse({"error": "Booking not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
