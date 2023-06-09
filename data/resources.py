from import_export import resources

from data.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = '__all__'
