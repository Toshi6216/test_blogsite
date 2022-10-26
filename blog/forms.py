from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category')

        
class ContentCardForm(forms.ModelForm):  #コンテンツカードのフォーム追加
    class Meta:
        model = ContentCard
        fields = '__all__'
   

#ブログ　インラインフォームセット
CardFormset = forms.inlineformset_factory(
    Post, ContentCard, fields='__all__',
    form=ContentCardForm,  #追加したフォームを渡す
    extra=1,  can_delete=False
)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {'name',}



#以下参考

class SampleChoiceAddForm(forms.Form):
    choice_1 = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(),
        label='地域'
    )

