from serializers.categs import serializers
from rest_framework import serializers as ser
from categories.models import Category

class FilterCategListSerializer(ser.ListSerializer):
    """front should get a list with only root categs"""
    def to_representation(self,objects):
        data = objects.filter(parent=None)
        return super().to_representation(data)



class CustomChildrenSerializer(ser.Serializer):
    """for each child"""
    def to_representation(self, obj):
        # self.parent.__class__.__name__)          # ListSerializer
        # self.parent.parent.__class__.__name__)# CategorySerializer
        serializer = self.parent.parent.__class__(obj)
        #print("ser data: ",serializer.data)
        # {'id': 2, 'name': 'Fiction', 'slug': 'fiction', 'parent': 1, 'children': []}
        return serializer.data


class CategorySerializer(ser.ModelSerializer):
    """ each related object if parent has attr children == 'related name' from model FK
    and will be ser-ed by CategorySerializer; you need children (no need parents) """
    children = CustomChildrenSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id','name','slug','children')
        # over-write list_ser_cls (to filter data: only parents)
        list_serializer_class = FilterCategListSerializer