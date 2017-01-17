from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'size', 'rent', 'date_available', 'bathroom', 'laundry', 'pets', 'location']
        labels = {'title': 'Title',
                  'description': 'Room Description',
                  'size': 'Room Size',
                  'rent': 'Rent',
                  'date_available': 'Date Available',
                  'bathroom': 'Private Bathroom',
                  'laundry': 'Laundry',
                  'pets': 'Pets',
                  'location': 'Location',
                  }
