from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title of task', max_length=200, widget=forms.TextInput(attrs={'class': 'input_title'}))  
    description = forms.CharField(label='Description of task', widget=forms.Textarea(attrs={'class': 'input_description'}))


class CreateNewProject(forms.Form):
    name = forms.CharField(label='Name of project', max_length=200, widget=forms.TextInput(attrs={'class': 'input_name'}))