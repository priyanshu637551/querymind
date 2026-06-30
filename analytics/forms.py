from django import forms

class QueryForm(forms.Form):
    question = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ask a business question..."
            }
        )
    )