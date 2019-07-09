from django.shortcuts import render

from research.forms import SearchForm
from research.models import Category
from research.models import Product


prod_subs_1 = {}
prod_subs_2 = {}
prod_subs_3 = {}
prod_subs_4 = {}

def search(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = SearchForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        
        # Ici nous pouvons traiter les données du formulaire
        product = form.cleaned_data['q']
        nutri = list(Product.objects.filter(name_product__contains=product).values('nutrition_score'))[1]
        c = list(Category.objects.filter(cat_product__name_product__contains=product).values('name'))[1]
        if nutri['nutrition_score'] == 'e':
            prod_subs_1['a'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[0]
            prod_subs_2['b'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='b').values())[:2]
            prod_subs_3['c'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='c').values())[0]        
            prod_subs_4['d'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='d').values())[0]
        if nutri['nutrition_score'] == 'd':
            prod_subs_1['a'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[0]
            prod_subs_2['b'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='b').values())[:3]
            prod_subs_3['c'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='c').values())[:1]        
        if nutri['nutrition_score'] == 'c':
            prod_subs_1['a'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[:2]
            prod_subs_2['b'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='b').values())[:3]
        
        if nutri['nutrition_score'] == 'b':
            prod_subs_1['a'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[:5]
        if nutri['nutrition_score'] == 'a':
            prod_subs_1['a'] = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[:5]
            
        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'search.html', locals())