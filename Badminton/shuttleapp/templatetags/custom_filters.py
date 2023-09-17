from django import template
from shuttleapp.models import Booking  # Import your Booking model

register = template.Library()


@register.filter
def booking_count_for_time_slot(booking_date, start_time, end_time):
    return Booking.objects.filter(
        booking_date=booking_date,
        booking_start_time=start_time,
        booking_end_time=end_time,
    ).count()
