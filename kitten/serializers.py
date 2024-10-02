from rest_framework import serializers

from kitten.models import Kitten, Rating


class KittenSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели Котенка """

    class Meta:
        model = Kitten
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели оценки котенка """

    class Meta:
        model = Rating
        fields = '__all__'
