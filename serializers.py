from rest_framework import serializers
from .models import LibraryPermission

class LibraryPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LibraryPermission
        fields = ('book_name', 'librarian_name', 'member_approval', 'library_director_approval', 'permission_date', 'reason')