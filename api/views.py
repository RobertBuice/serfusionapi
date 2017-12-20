# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

from django.db.models import Q

from models import Person, Address, EmailAddress, PhoneNumber
from serializers import PersonSerializer, PersonGetSerializer, AddressSerializer, \
    EmailAddressSerializer, PhoneNumberSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows people to be viewed or edited.
    """

    def get_queryset(self):
        queryset = Person.objects.all()
        api_filter = self.request.query_params.get('filter', None)
        if api_filter is not None:

            addresses = Address.objects.filter(Q(street1__icontains=api_filter) | Q(city__icontains=api_filter) |
                                   Q(state__icontains=api_filter) | Q(postal_code__icontains=api_filter))

            emails = EmailAddress.objects.filter(Q(email_address__icontains=api_filter))

            phones = PhoneNumber.objects.filter(Q(phone_number__icontains=api_filter))

            queryset = queryset.distinct().filter(
                Q(first_name__icontains=api_filter) | Q(last_name__icontains=api_filter) |
                Q(date_of_birth__icontains=api_filter) | Q(addresses__in=addresses) |
                Q(email_addresses__in=emails) | Q(phone_numbers__in=phones)
            )
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PersonGetSerializer
        return PersonSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EmailAddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows email addresses to be viewed or edited.
    """
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows phone numbers to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
