from django.forms import ModelForm
from models import SampleProjectMaster


class SampleProjectMasterForm(ModelForm):
    class Meta:
        model = SampleProjectMaster
        fields = "__all__"
