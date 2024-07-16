# main/views.py
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import IngredientsForm, FiltersForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'main/home.html')

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect(home)  # Replace 'home' with the name of your home view
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

def checklist(request):
    if request.method == 'POST':
        ingredients_form = IngredientsForm(request.POST)
        filters_form = FiltersForm(request.POST)
        if ingredients_form.is_valid() and filters_form.is_valid():
            ingredients = ingredients_form.cleaned_data
            filters = filters_form.cleaned_data
            request.session['ingredients'] = ingredients
            request.session['filters'] = filters
            return redirect('results')
    else:
        ingredients_form = IngredientsForm()
        filters_form = FiltersForm()
    return render(request, 'main/checklist.html', {'ingredients_form': ingredients_form, 'filters_form': filters_form})

from django.contrib import messages

def results(request):
    ingredients = request.session.get('ingredients', {})
    filters = request.session.get('filters', {})

    # Load CSV file into a DataFrame
    df = pd.read_csv('main/data/recipes.csv')

    # Ensure the 'vegetarian' column is of boolean type
    df['vegetarian'] = df['vegetarian'].astype(bool)

    # Filtering logic based on user inputs
    filtered_df = df.copy()
    
    for category, selected_ingredients in ingredients.items():
        if selected_ingredients:
            filtered_df = filtered_df[filtered_df['ingredients'].str.contains('|'.join(selected_ingredients))]
    
    if filters.get('cuisine'):
        filtered_df = filtered_df[filtered_df['cuisine'].str.lower().isin(filters['cuisine'])]
    
    if filters.get('vegetarian'):
        filtered_df = filtered_df[filtered_df['vegetarian'] == filters['vegetarian']]
    
    if filters.get('difficulty'):
        difficulties = [difficulty.lower() for difficulty in filters['difficulty']]
        filtered_df = filtered_df[filtered_df['difficulty'].str.lower().isin(difficulties)]

    recipes = filtered_df.to_dict('records')

    if not recipes:
        messages.info(request, 'No recipes found matching your criteria.')

    return render(request, 'main/results.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    df = pd.read_csv('main/data/recipes.csv')
    recipe = df.loc[df['id'] == recipe_id].to_dict('records')[0]
    return render(request, 'main/recipe_detail.html', {'recipe': recipe})

    # if request.method == 'POST' and 'save_recipe' in request.POST:
    #     # Assuming you have authenticated users, get the current user
    #     user = request.user
    #     if user.is_authenticated:
    #         # Save the recipe for the current user
    #         SavedRecipe.objects.get_or_create(user=user, recipe_id=recipe_id)
    #         messages.success(request, 'Recipe saved successfully.')
    #     else:
    #         messages.error(request, 'You must be logged in to save recipes.')

    return render(request, 'main/recipe_detail.html', {'recipe': recipe})