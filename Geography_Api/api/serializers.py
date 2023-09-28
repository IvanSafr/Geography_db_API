from rest_framework import serializers

from rest_framework import serializers

from .models import student_info

class SudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student_info
        fields = ('profile', 'profile_num', 'name', 'surname', 'geoposition')