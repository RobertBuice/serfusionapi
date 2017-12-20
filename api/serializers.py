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

            if 'street_number' in a:
                route = a['street_number'] + " " + a['route']
            else:
                route = a['route']

            Address.objects.create(
                person=p,
                state=a['administrative_area_level_1'],
                postal_code=a['administrative_area_level_1'],
                city=a['locality'],
                street1=route
            )

        for n in phone_numbers:
            PhoneNumber.objects.create(person=p, phone_number=n['value'])

        for e in email_addresses:
            print e['value']
            EmailAddress.objects.create(person=p, email_address=e['value'])

        return p

    def update(self, instance, validated_data):
        addresses = validated_data.pop('addresses', None)
        phone_numbers = validated_data.pop('phone_numbers', None)
        email_addresses = validated_data.pop('email_addresses', None)

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.date_of_birth = validated_data['date_of_birth']

        instance.addresses.all().delete()
        instance.phone_numbers.all().delete()
        instance.email_addresses.all().delete()

        instance.save()

        for a in addresses:

            if 'value' in a:
                Address.objects.create(
                    person=instance,
                    state='',
                    postal_code='',
                    city='',
                    street1=a['value']
                )
                continue

            if 'street_number' in a:
                route = a['street_number'] + " " + a['route']
            else:
                route = a['route']

            Address.objects.create(
                person=instance,
                state=a['administrative_area_level_1'],
                postal_code=a['administrative_area_level_1'],
                city=a['locality'],
                street1=route
            )

        for n in phone_numbers:
            PhoneNumber.objects.create(person=instance, phone_number=n['value'])

        for e in email_addresses:
            EmailAddress.objects.create(person=instance, email_address=e['value'])

        return instance
