from rest_framework import serializers
from .models import Appointment
from datetime import date

class AppointmentSerializer(serializers.ModelSerializer):

    def validate(self, data):
        timeslot = data['timeslot']

        if not timeslot.is_available:
            raise serializers.ValidationError("Time slot already booked")

        if timeslot.date < date.today():
            raise serializers.ValidationError("Cannot book past dates")

        if self.context['request'].user == timeslot.doctor.user:
            raise serializers.ValidationError("Doctor cannot book himself")

        return data

    def create(self, validated_data):
        timeslot = validated_data['timeslot']
        timeslot.is_available = False
        timeslot.save()
        return super().create(validated_data)

    class Meta:
        model = Appointment
        fields = "__all__"
