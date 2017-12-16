# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField()


class Address(models.Model):
    person = models.ForeignKey(Person, related_name='addresses', blank=True, null=True)

    street1 = models.CharField(max_length=200, default='')
    street2 = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=2, default='')
    postal_code = models.CharField(max_length=20, default='')


class PhoneNumber(models.Model):
    person = models.ForeignKey(Person, related_name='phone_numbers')

    phone_number = PhoneNumberField()


class EmailAddress(models.Model):
    person = models.ForeignKey(Person, related_name='email_addresses')

    email_address = models.EmailField(max_length=240, default='')
