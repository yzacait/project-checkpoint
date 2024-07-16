# main/forms.py
from django import forms

class IngredientsForm(forms.Form):
    vegetables = forms.MultipleChoiceField(choices=[
        ('artichokes', 'Artichokes'), 
        ('asparagus', 'Asparagus'), 
        ('beets', 'Beets'), 
        ('bell Peppers', 'Bell Peppers'), 
        ('bok Choy', 'Bok Choy'), 
        ('broccoli', 'Broccoli'), 
        ('brussels Sprouts', 'Brussels Sprouts'), 
        ('cabbage', 'Cabbage'), 
        ('carrots', 'Carrots'), 
        ('cauliflower', 'Cauliflower'), 
        ('celery', 'Celery'), 
        ('collard greens', 'Collard Greens'), 
        ('corn', 'Corn'), 
        ('cucumbers', 'Cucumbers'), 
        ('eggplant', 'Eggplant'), 
        ('garlic', 'Garlic'), 
        ('green Beans', 'Green Beans'), 
        ('green Peas', 'Green Peas'), 
        ('kale', 'Kale'), 
        ('leeks', 'Leeks'), 
        ('lettuce', 'Lettuce'), 
        ('mushrooms', 'Mushrooms'), 
        ('okra', 'Okra'), 
        ('onions', 'Onions'), 
        ('plantains', 'Plantains'), 
        ('potatoes', 'Potatoes'), 
        ('pumpkin', 'Pumpkin'), 
        ('radishes', 'Radishes'), 
        ('scallions', 'Scallions'), 
        ('shallots', 'Shallots'), 
        ('spinach', 'Spinach'), 
        ('squash', 'Squash'), 
        ('sweet potatoes', 'Sweet Potatoes'), 
        ('swiss chard', 'Swiss Chard'), 
        ('tomatoes', 'Tomatoes'), 
        ('turnips', 'Turnips'), 
        ('zucchini', 'Zucchini')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    fruits = forms.MultipleChoiceField(choices=[
        ('apples', 'Apples'), 
        ('apricots', 'Apricots'), 
        ('bananas', 'Bananas'), 
        ('blackberries', 'Blackberries'), 
        ('blueberries', 'Blueberries'), 
        ('cherries', 'Cherries'), 
        ('coconuts', 'Coconuts'), 
        ('dates', 'Dates'), 
        ('dragon fruit', 'Dragon Fruit'), 
        ('figs', 'Figs'), 
        ('grapefruits', 'Grapefruits'), 
        ('guava', 'Guava'), 
        ('kiwifruit', 'Kiwifruit'), 
        ('lemons', 'Lemons'), 
        ('limes', 'Limes'), 
        ('lychee', 'Lychee'), 
        ('mangoes', 'Mangoes'), 
        ('nectarines', 'Nectarines'), 
        ('oranges', 'Oranges'), 
        ('papayas', 'Papayas'), 
        ('passion Fruit', 'Passion Fruit'), 
        ('peaches', 'Peaches'), 
        ('pears', 'Pears'), 
        ('persimmons', 'Persimmons'), 
        ('pineapples', 'Pineapples'), 
        ('plums', 'Plums'), 
        ('pomegranate', 'Pomegranate'), 
        ('quinces', 'Quinces'), 
        ('raspberries', 'Raspberries'), 
        ('starfruit', 'Starfruit'), 
        ('strawberries', 'Strawberries'), 
        ('tangerines', 'Tangerines')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    grains_cereals = forms.MultipleChoiceField(choices=[
        ('all-purpose flour', 'All-Purpose Flour'), 
        ('almond flour', 'Almond Flour'), 
        ('barley', 'Barley'), 
        ('brown rice', 'Brown Rice'), 
        ('buckwheat', 'Buckwheat'), 
        ('coconut flour', 'Coconut Flour'), 
        ('cornmeal', 'Cornmeal'), 
        ('couscous', 'Couscous'), 
        ('farro', 'Farro'), 
        ('millet', 'Millet'), 
        ('oats', 'Oats'), 
        ('penne', 'Penne'), 
        ('quinoa', 'Quinoa'), 
        ('ramen', 'Ramen'), 
        ('soba', 'Soba'), 
        ('spaghetti', 'Spaghetti'), 
        ('udon', 'Udon'), 
        ('whole wheat flour', 'Whole Wheat Flour')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    proteins = forms.MultipleChoiceField(choices=[
        ('anchovies', 'Anchovies'), 
        ('beef', 'Beef'), 
        ('bison', 'Bison'), 
        ('black beans', 'Black Beans'), 
        ('chicken', 'Chicken'), 
        ('Chicken eggs', 'Chicken Eggs'), 
        ('chickpeas', 'Chickpeas'), 
        ('clams', 'Clams'), 
        ('cod', 'Cod'), 
        ('crab', 'Crab'), 
        ('duck', 'Duck'), 
        ('duck eggs', 'Duck Eggs'), 
        ('edamame', 'Edamame'), 
        ('goat', 'Goat'), 
        ('kidney beans', 'Kidney Beans'), 
        ('lamb', 'Lamb'), 
        ('lentils', 'Lentils'), 
        ('lobster', 'Lobster'), 
        ('mackerel', 'Mackerel'), 
        ('mussels', 'Mussels'), 
        ('oysters', 'Oysters'), 
        ('peas', 'Peas'), 
        ('pinto beans', 'Pinto Beans'), 
        ('pork', 'Pork'), 
        ('quail eggs', 'Quail Eggs'), 
        ('salmon', 'Salmon'), 
        ('sardines', 'Sardines'), 
        ('scallops', 'Scallops'), 
        ('seitan', 'Seitan'), 
        ('shrimp', 'Shrimp'), 
        ('squid', 'Squid'),
        ('steak','Steak'),
        ('tempeh', 'Tempeh'), 
        ('tofu', 'Tofu'), 
        ('tuna', 'Tuna'), 
        ('turkey', 'Turkey'), 
        ('veal', 'Veal'), 
        ('venison', 'Venison')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    dairy_alternatives = forms.MultipleChoiceField(choices=[
        ('almond milk', 'Almond Milk'), 
        ('blue cheese', 'Blue Cheese'), 
        ('brie', 'Brie'), 
        ('buttermilk', 'Buttermilk'), 
        ('cheddar', 'Cheddar'), 
        ('clarified butter', 'Clarified Butter'), 
        ('cottage cheese', 'Cottage Cheese'), 
        ('cow’s milk', 'Cow’s Milk'), 
        ('feta', 'Feta'), 
        ('goat cheese', 'Goat Cheese'), 
        ('goat’s milk', 'Goat’s Milk'), 
        ('gouda', 'Gouda'), 
        ('greek yogurt', 'Greek Yogurt'), 
        ('heavy cream', 'Heavy Cream'), 
        ('mozzarella', 'Mozzarella'), 
        ('coconut yogurt', 'Coconut Yogurt'), 
        ('almond yogurt','Almond Yogurt'),
        ('oat milk', 'Oat Milk'), 
        ('parmesan', 'Parmesan'), 
        ('yogurt', 'Regular Yogurt'), 
        ('ricotta', 'Ricotta'), 
        ('salted butter', 'Salted Butter'), 
        ('sour cream', 'Sour Cream'), 
        ('soy milk', 'Soy Milk'), 
        ('unsalted butter', 'Unsalted Butter')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    herbs_spices = forms.MultipleChoiceField(choices=[
        ('basil', 'Basil'), 
        ('bay leaves', 'Bay Leaves'), 
        ('black pepper', 'Black Pepper'), 
        ('cardamom', 'Cardamom'), 
        ('cilantro', 'Cilantro'), 
        ('cinnamon', 'Cinnamon'), 
        ('cloves', 'Cloves'), 
        ('cumin', 'Cumin'), 
        ('dill', 'Dill'), 
        ('fennel seeds', 'Fennel Seeds'), 
        ('ginger', 'Ginger'), 
        ('mint', 'Mint'), 
        ('mustard seeds', 'Mustard Seeds'), 
        ('nutmeg', 'Nutmeg'), 
        ('oregano', 'Oregano'), 
        ('paprika', 'Paprika'), 
        ('parsley', 'Parsley'), 
        ('red pepper flakes', 'Red Pepper Flakes'), 
        ('rosemary', 'Rosemary'), 
        ('saffron', 'Saffron'), 
        ('sage', 'Sage'), 
        ('tarragon', 'Tarragon'), 
        ('thyme', 'Thyme'), 
        ('turmeric', 'Turmeric')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    oils_fats = forms.MultipleChoiceField(choices=[
        ('avocado oil', 'Avocado Oil'), 
        ('canola oil', 'Canola Oil'), 
        ('clarified butter', 'Clarified Butter'), 
        ('coconut oil', 'Coconut Oil'), 
        ('duck fat', 'Duck Fat'), 
        ('ghee', 'Ghee'), 
        ('grape seed oil', 'Grape Seed Oil'), 
        ('lard', 'Lard'), 
        ('macadamia oil', 'Macadamia Oil'), 
        ('olive oil', 'Olive Oil'), 
        ('palm oil', 'Palm Oil'), 
        ('peanut oil', 'Peanut Oil'), 
        ('sesame oil', 'Sesame Oil'), 
        ('tallow', 'Tallow'), 
        ('truffle oil', 'Truffle Oil'), 
        ('vegetable oil', 'Vegetable Oil'), 
        ('walnut oil', 'Walnut Oil')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    baking_ingredients = forms.MultipleChoiceField(choices=[
        ('agave nectar', 'Agave Nectar'), 
        ('agar-agar', 'Agar-Agar'), 
        ('almond extract', 'Almond Extract'), 
        ('baking powder', 'Baking Powder'), 
        ('baking soda', 'Baking Soda'), 
        ('brown rice syrup', 'Brown Rice Syrup'), 
        ('brown sugar', 'Brown Sugar'), 
        ('chocolate chips', 'Chocolate Chips'), 
        ('cocoa powder', 'Cocoa Powder'), 
        ('coconut nectar', 'Coconut Nectar'), 
        ('coconut sugar', 'Coconut Sugar'), 
        ('corn syrup', 'Corn Syrup'), 
        ('cornstarch', 'Cornstarch'), 
        ('cream of tartar', 'Cream of Tartar'), 
        ('dark chocolate', 'Dark Chocolate'), 
        ('date syrup', 'Date Syrup'), 
        ('gelatin', 'Gelatin'), 
        ('granulated sugar', 'Granulated Sugar'), 
        ('honey', 'Honey'), 
        ('lavender extract', 'Lavender Extract'), 
        ('lemon zest', 'Lemon Zest'), 
        ('maple syrup', 'Maple Syrup'), 
        ('milk chocolate', 'Milk Chocolate'), 
        ('molasses', 'Molasses'), 
        ('orange zest', 'Orange Zest'), 
        ('peppermint extract', 'Peppermint Extract'), 
        ('powdered sugar', 'Powdered Sugar'), 
        ('rose water', 'Rose Water'), 
        ('unsweetened chocolate', 'Unsweetened Chocolate'), 
        ('vanilla extract', 'Vanilla Extract'), 
        ('white chocolate', 'White Chocolate'), 
        ('yeast', 'Yeast')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    condiments_sauces = forms.MultipleChoiceField(choices=[
        ('aioli', 'Aioli'), 
        ('apple cider vinegar', 'Apple Cider Vinegar'), 
        ('balsamic vinegar', 'Balsamic Vinegar'), 
        ('barbecue sauce', 'Barbecue Sauce'), 
        ('chili paste', 'Chili Paste'), 
        ('chimichurri sauce', 'Chimichurri Sauce'), 
        ('dijon mustard', 'Dijon Mustard'), 
        ('fish sauce', 'Fish Sauce'), 
        ('gochujang', 'Gochujang'), 
        ('hoisin sauce', 'Hoisin Sauce'), 
        ('horseradish', 'Horseradish'), 
        ('hot sauce', 'Hot Sauce'), 
        ('ketchup', 'Ketchup'), 
        ('mayonnaise', 'Mayonnaise'), 
        ('miso paste', 'Miso Paste'), 
        ('mustard', 'Mustard'), 
        ('ponzu sauce', 'Ponzu Sauce'), 
        ('red wine vinegar', 'Red Wine Vinegar'), 
        ('relish', 'Relish'), 
        ('rice vinegar', 'Rice Vinegar'), 
        ('salsa','Salsa'),
        ('sriracha', 'Sriracha'), 
        ('ssamjang', 'Ssamjang'), 
        ('soy sauce', 'Soy Sauce'), 
        ('tartar sauce', 'Tartar Sauce'), 
        ('teriyaki sauce', 'Teriyaki Sauce'), 
        ('tahini', 'Tahini'), 
        ('white vinegar', 'White Vinegar'), 
        ('worcesteshire sauce', 'Worcestershire Sauce')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    nuts_seeds = forms.MultipleChoiceField(choices=[
        ('almonds', 'Almonds'), 
        ('brazil nuts', 'Brazil Nuts'), 
        ('cashews', 'Cashews'), 
        ('chestnuts', 'Chestnuts'), 
        ('chia seeds', 'Chia Seeds'), 
        ('flaxseeds', 'Flaxseeds'), 
        ('hazelnuts', 'Hazelnuts'), 
        ('hemp seeds', 'Hemp Seeds'), 
        ('macadamia nuts', 'Macadamia Nuts'), 
        ('pine nuts', 'Pine Nuts'), 
        ('pistachios', 'Pistachios'), 
        ('poppy seeds', 'Poppy Seeds'), 
        ('pumpkin seeds', 'Pumpkin Seeds'), 
        ('sesame seeds', 'Sesame Seeds'), 
        ('sunflower seeds', 'Sunflower Seeds'), 
        ('walnuts', 'Walnuts')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    beverages = forms.MultipleChoiceField(choices=[
        ('beer', 'Beer'), 
        ('brandy', 'Brandy'), 
        ('buttermilk', 'Buttermilk'), 
        ('coffee', 'Coffee'), 
        ('coconut water', 'Coconut Water'), 
        ('energy drinks', 'Energy Drinks'), 
        ('gin', 'Gin'), 
        ('herbal tea', 'Herbal Tea'), 
        ('horchata', 'Horchata'), 
        ('juice', 'Juice'), 
        ('kombucha', 'Kombucha'), 
        ('mezcal', 'Mezcal'), 
        ('rum', 'Rum'), 
        ('soda', 'Soda'), 
        ('sparkling water', 'Sparkling Water'), 
        ('sports drinks', 'Sports Drinks'), 
        ('tea', 'Tea'), 
        ('vodka', 'Vodka'), 
        ('water', 'Water'), 
        ('whiskey', 'Whiskey'), 
        ('wine', 'Wine')
    ], widget=forms.CheckboxSelectMultiple, required=False)

    miscellaneous = forms.MultipleChoiceField(choices=[
        ('beans', 'Beans'), 
        ('beef broth', 'Beef Broth'), 
        ('capers', 'Capers'), 
        ('chicken broth', 'Chicken Broth'), 
        ('chutney', 'Chutney'), 
        ('curry pastes', 'Curry Pastes'), 
        ('dried tomatoes', 'Dried Tomatoes'), 
        ('fish stock', 'Fish Stock'), 
        ('hummus', 'Hummus'), 
        ('jams', 'Jams'), 
        ('kimchi', 'Kimchi'), 
        ('nori (seaweed)', 'Nori (Seaweed)'), 
        ('nut butters', 'Nut Butters'), 
        ('olives', 'Olives'), 
        ('pasta sauces','Pasta Sauces'),
        ('pickled jalapeños', 'Pickled Jalapeños'), 
        ('pickles', 'Pickles'), 
        ('sun-dried tomatoes', 'Sun-Dried Tomatoes'), 
        ('tomatoes', 'Tomatoes'), 
        ('vegetable broth', 'Vegetable Broth'), 
        ], widget=forms.CheckboxSelectMultiple, required=False)

class FiltersForm(forms.Form):
    cuisine = forms.MultipleChoiceField(
        choices=[
            ('american', 'American'),
            ('asian', 'Asian'),
            ('chinese', 'Chinese'),
            ('filipino', 'Filipino'),
            ('french', 'French'),
            ('greek', 'Greek'),
            ('indian', 'Indian'),
            ('italian', 'Italian'),
            ('japanese', 'Japanese'),
            ('korean', 'Korean'),
            ('mediterranean', 'Mediterranean'),
            ('mexican', 'Mexican'),
            ('middle eastern', 'Middle Eastern'),
            ('spanish', 'Spanish'),
            ('thai', 'Thai'),
            ('vietnamese', 'Vietnamese'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    vegetarian = forms.BooleanField(required=False)
    difficulty = forms.MultipleChoiceField(choices=[('easy', 'Easy'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], widget=forms.CheckboxSelectMultiple,required=False)