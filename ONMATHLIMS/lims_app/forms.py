# coding:utf-8

from django.forms import ModelForm
from models import SampleProjectMaster, UserInfo
from django import forms


class SampleProjectMasterForm(ModelForm):
    class Meta:
        model = SampleProjectMaster
        fields = "__all__"


class UserForm(forms.Form):
    username = forms.CharField(label=u'', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'用户名'}))
    password = forms.CharField(label=u'', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'密码'}))

    def clean_password(self):
        user = self.cleaned_data.get('username')
        passwd = self.cleaned_data.get('password')
        user_db = UserInfo.objects.filter(username=user)
        if not user_db:
            raise forms.ValidationError(u'不存在这个用户,请注册!')
        else:
            user_object = UserInfo.objects.get(username=user)
            if passwd != user_object.get_password():
                raise forms.ValidationError(u'密码错误,请重试!')
