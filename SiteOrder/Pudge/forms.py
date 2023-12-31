from django import forms

class ClubsForm(forms.Form):
    name = forms.CharField()
    map = forms.CharField()
    img = forms.FileField()
    contacts = forms.JSONField()
    priceData = forms.JSONField()
    computerSpecs = forms.JSONField()
    quantityComputers = forms.JSONField()

    def get_absolute_url(self):
      return self.img.url

class NewClubsTestForm(forms.Form):
    name = forms.CharField()
    map = forms.CharField()
    img = forms.FileField()

    def get_absolute_url(self):
        return self.img.url

class GalleryForm(forms.Form):
    name = forms.CharField()
    img = forms.FileField()
    text = forms.CharField(required=False)

    def get_absolute_url(self):
        return self.img.url

class NewsForm(forms.Form):
    title = forms.CharField()
    img = forms.FileField()
    text1 = forms.CharField()
    text2 = forms.CharField(required=False)
    text3 = forms.CharField(required=False)

    def get_absolute_url(self):
        return self.img.url

class ReservationForm(forms.Form):
  name = forms.CharField()
  phone_number = forms.CharField()
  telegram = forms.CharField(required=False)
  club = forms.CharField()
  tariff = forms.CharField()
  reservation_time = forms.CharField()
  quantity_seats = forms.CharField()
  recipient = forms.CharField(required=False)

class PartnersForm(forms.Form):
  name = forms.CharField()
  img = forms.CharField()
  # url = forms.CharField(required=False)
  text = forms.CharField(required=False)

