import django_tables2 as tables
from .models import *

from django_tables2.export.views import ExportMixin


class RentalListingTable(tables.Table):
    class Meta:
        model = rental_listing
        template_name = "django_tables2/bootstrap.html"
        fields = (
                'home_owner',
                'organization',
                'description',
                'lease_terms',
                'type_of_listing',
                'address',
                'city',
                'house_number',
                'max_rooms',
                'vacant',
                'available_rooms',
                'price_per_room',
                # 'geom_lat',
                # 'geom_long',
                # 'added_on',
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        row_attrs = {
            "data-id": lambda record: record.pk
        }
class BookingTable(tables.Table):
    class Meta:
        model = Booking
        template_name = "django_tables2/bootstrap.html"
        fields = (
                'tenant',
                'listing',
                'number_of_rooms',
                'approved',
                'rejected',
                'waiting_list',
                'date_of_booking',
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        row_attrs = {
            "data-id": lambda record: record.pk
        }