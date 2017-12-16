# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

from models import Person, Address, EmailAddress, PhoneNumber
from serializers import PersonSerializer, AddressSerializer, \
    EmailAddressSerializer, PhoneNumberSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows people to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


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

