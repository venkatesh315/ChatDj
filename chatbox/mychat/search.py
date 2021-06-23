import django_filters
from django_filters import DateFilter
from django.contrib.auth.models import User


class search_user(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ['username']