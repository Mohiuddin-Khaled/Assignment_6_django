from django import forms
from reviews.models import ReviewModel


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["comment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "appearance-none block w-full bg-gray-200 text-gray-700 "
                    "border border-gray-200 rounded py-3 px-4 leading-tight "
                    "focus:outline-none focus:bg-white focus:border-gray-500"
                }
            )
