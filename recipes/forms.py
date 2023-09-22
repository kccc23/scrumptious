from django.forms import ModelForm, TextInput, URLInput, Textarea
from recipes.models import Recipe, RecipeStep, Ingredient

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]
        widgets = {
            "title": TextInput(attrs={
                            'placeholder': 'Title'}),
            "picture": URLInput(attrs={
                            'placeholder': 'URL'}),
            "description": Textarea(attrs={
                            'placeholder': 'Start your scrumptious recipe here...'}),
        }

class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = [
            "step_number",
            "instruction",
        ]
        widgets = {
            "step_number": TextInput(attrs={
                            'placeholder': 'Step Number'}),
            "instruction": Textarea(attrs={
                            'placeholder': 'Add a step to your recipe...'}),
        }

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "food_item",
        ]
        widgets = {
            "amount": TextInput(attrs={
                            'placeholder': 'Amount'}),
            "food_item": TextInput(attrs={
                            'placeholder': 'Food Item'}),
        }