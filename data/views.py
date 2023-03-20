from django.shortcuts import render
from tablib import Dataset

from data.models import Person
from data.resources import PersonResource


# Create your views here.
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        imported_data = dataset.load(new_person.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            for data in imported_data:
                value = Person(
                    data[0],
                    data[1],
                    data[2],
                    data[3],

                )
                value.save()

    return render(request, 'index.html')
