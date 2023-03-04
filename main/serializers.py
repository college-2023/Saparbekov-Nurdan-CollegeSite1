from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = 'image'.split()


class ShortItemSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    item_images = ImageSerializer(many=True)

    class Meta:
        model = Item
        fields = 'title price category item_images'.split()


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = 'name'.split()


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = TypeSerializer()
    company = CompanySerializer()
    material = MaterialSerializer()

    class Meta:
        model = Item
        fields = 'id title slug description colors size price company type category material'.split()


