from django import forms

from toys.models import Toy,User

class UserAdminForm(forms.ModelForm):
    email = forms.EmailField(label='User Email', required=True)

    class Meta:
        model = User
        fields = '__all__'

class ToyAdminForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = '__all__'

    def __init__(self, *args,**kwargs):
        initial = kwargs.pop('initial',None)
        instance = kwargs.pop('instance', None)

        super(ToyAdminForm,self).__init__(*args,**kwargs)