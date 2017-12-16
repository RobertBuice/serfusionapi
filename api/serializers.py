from rest_framework import serializers
from models import Person, Address, EmailAddress, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class EmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PersonGetSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    phone_numbers = PhoneNumberSerializer(many=True)
    email_addresses = EmailAddressSerializer(many=True)

    class Meta:
        model = Person
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    addresses = serializers.ListField(write_only=True, required=False)
    phone_numbers = serializers.ListField(write_only=True, required=True)
    email_addresses = serializers.ListField(write_only=True, required=True)

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        addresses = validated_data.pop('addresses', None)
        phone_numbers = validated_data.pop('phone_numbers', None)
        email_addresses = validated_data.pop('email_addresses', None)

        p = Person.objects.create(**validated_data)

        for a in addresses:
            Address.objects.create(person=p, **a)

        for n in phone_numbers:
            PhoneNumber.objects.create(person=p, phone_number=n)

        for e in email_addresses:
            EmailAddress.objects.create(person=p, email_address=e)

        return p



