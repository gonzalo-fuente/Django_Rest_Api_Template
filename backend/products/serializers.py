from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product

from .validators import unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    # owner = UserPublicSerializer(source='user', read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    title = serializers.CharField(
        validators=[unique_product_title])

    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
            'my_discount',
            'my_user_data',
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        # To avoid having an error when the data doesn't have the aggregated fields
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()

    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
