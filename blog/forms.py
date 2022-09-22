from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea)
    


class SampleChoiceAddForm(forms.Form):
    choice_1 = forms.ChoiceField(
        
        required=True,
        widget=forms.widgets.Select(),
        label='地域'
    )

