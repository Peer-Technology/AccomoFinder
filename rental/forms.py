from django import forms
from crispy_forms.bootstrap import FormActions, UneditableField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Button, Div, Field, Fieldset, Layout, Submit
from .models import *
class DateInput(forms.DateInput):
    input_type = 'date'
class RentalPlaceForm(forms.ModelForm):
    class Meta:
        model = rental_listing
        fields = (
            'home_owner',
            'organization',
            'address',
            'house_number',
            'price_total',
            'description',
            'lease_terms',
            'type_of_listing',
            'city',
            'max_rooms',
            'vacant',
            'available_rooms',
            'price_per_room',
            'geom_lat',
            'geom_long',
            'preference',
            'wifi',
            'solar',
            'curfew',
            'pets_allowed',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                HTML("""
                        <br/>
                    """),
                Div(
                    Field('home_owner',
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('organization',
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('address',rows="2", cols="10",
                          wrapper_class="col-md-3", style="font-size: x-small;", ),
                    Field('house_number',
                          wrapper_class="col-md-3", style="font-size: x-small;", ),
                    Field('price_total', css_class="",type="",
                          wrapper_class="col-md-3", style="font-size: x-small;", ),
                    Field('description', autocomplete='off', type="",
                          wrapper_class="col-md-3",rows="2", cols="10", style="font-size: x-small;",),
                    Field('lease_terms', autocomplete='off', type="",
                          wrapper_class="col-md-3" ,rows="2", cols="10", style="font-size: x-small;",),
                    Field('type_of_listing', autocomplete='off', type="",
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('city', autocomplete='off', type="",
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('max_rooms', autocomplete='off', type="",
                          wrapper_class="col-md-2", style="font-size: x-small;",),
                    Field('vacant', autocomplete='off', type="",
                          wrapper_class="col-md-2", style="font-size: x-small;",),
                    Field('available_rooms', autocomplete='off', type="",
                          wrapper_class="col-md-2", style="font-size: x-small;",),
                    Field('price_per_room', autocomplete='off', type="",
                          wrapper_class="col-md-2", style="font-size: x-small;",),
                    Field('geom_lat', autocomplete='off', type="",
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('geom_long', autocomplete='off', type="",
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    Field('preference', autocomplete='off', type="",
                          wrapper_class="col-md-3", style="font-size: x-small;",),
                    
                    css_class='row text-center'
                ),
               
                Div(
                    Field('pets_allowed', autocomplete='off', type="",
                          wrapper_class="col-md-3"),
                    Field('wifi', autocomplete='off', type="",
                          wrapper_class="col-md-3"),
                    Field('solar', autocomplete='off', type="",
                          wrapper_class="col-md-3"),
                    Field('curfew', autocomplete='off', type="",
                          wrapper_class="col-md-3"),
                    css_class='row text-center',
                    # hidden=True,
                    # style="opacity:0;height:0"
                ),
                 FormActions(
                    Submit('submit', 'Save' , css_class="btn  btn-sm btn-block btn-success" )
                ),

            )
        )
        # self.fields['secret_code'].required = False
        # self.fields['tel'].required = False
        self.helper.form_id = 'id-rent-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        # self.helper.add_input(Submit('submit', 'Submit')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address',]
    # def __init__(self, *args):
    #     super(SearchForm, self).__init__(*args))
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tenant',
            'listing',
            'number_of_rooms',
            ]
    # def __init__(self, *args):
    #     super(SearchForm, self).__init__(*args))
class BookingPayForm(forms.ModelForm):
    class Meta:
        model = BookingPay
        fields = [
            'booking',
            # 'proof_of_payment_attached',
            # 'file',
            'amount',
            ]
    # def __init__(self, *args):
    #     super(SearchForm, self).__init__(*args))

class OlRentalPlaceForm(forms.ModelForm):
    class Meta:
        model = rental_listing
        fields = [
            'home_owner',
            'organization',
            'address',
            'house_number',
            'price_total',
            'description',
            'lease_terms',
            'type_of_listing',
            'city',
            'max_rooms',
            'vacant',
            'available_rooms',
            'price_per_room',
            'geom_lat',
            'geom_long',
            ]