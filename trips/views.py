from django.http import JsonResponse
from .models import Trip 
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the page with no Frontend!")

def trip_listing(request):

    #pagination
    page_number = request.GET.get('page',1)
    page_size = request.GET.get('page_size',10)
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    #sorting
    sort_by = request.Get.get('sort_by', 'trip_id')
    trips = trips.order_by(sort_by)

    #searching
    search_query = request.Get.get('search', '')
    if search_query:
        trips = trips.filter(trip_id__icontains=search_query)

    paginated_trips = list(trips[start_index:end_index].values())

    return JsonResponse(paginated_trips, status=200)




def trip_details(request, trip_id):
    try:
        trip = Trip.objects.get(trip_id= trip_id)
        trip_data = {
            'trip_id': trip.trip_id,
            'user_id': trip.user_id,
            'vehicle_id': trip.vehicle_id,
            'driver_name': trip.driver_name,
            'trip_distance': trip.trip_distance
        }
 
        return JsonResponse(trip_data, status=200)
    except Trip.DoesNotExist:
        return JsonResponse({"error": "Trip not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

