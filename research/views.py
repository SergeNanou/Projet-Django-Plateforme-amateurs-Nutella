from django.shortcuts import render
from django.contrib.auth.models import User
from research.forms import SearchForm
from research.models import Category
from research.models import Product



def ind_pge_resultat(request):
    return render(request,'research/ind_pge_resultat.html')

def search(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    a = []
    b = []
    c = []
    a_1 = 0
    b_1 = 0
    c_1 = 0
    prod_subs_1 = [{'name_product':'','description':'',
                    'nutriments':'','nutrient_levels':''
                         ,'url':'','nutrition_score':'',
                         'nutrition_100':'','image':''},
                         {'name_product':'', 'description':'',
                         'nutriments':'','nutrient_levels':'',
                         'url':'','nutrition_score':''
                         ,'nutrition_100':'','image':''},
                         {'name_product':'', 'description':'',
                         'nutriments':'','nutrient_levels':'',
                         'url':'','nutrition_score':''
                         ,'nutrition_100':'','image':''},
                         {'name_product':'', 'description':'',
                         'nutriments':'','nutrient_levels':'',
                         'url':'','nutrition_score':'',
                         'nutrition_100':'','image':''},
                         {'name_product':'', 'description':'',
                         'nutriments':'','nutrient_levels':'',
                         'url':'','nutrition_score':'',
                         'nutrition_100':'','image':''},
                         {'name_product':'', 'description':'',
                         'nutriments':'','nutrient_levels':'',
                         'url':'','nutrition_score':'',
                         'nutrition_100':'','image':''}]
    prod_subs_2 = [{'name_product':'','description':'',
                    'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':'',
                        'nutrition_100':'','image':''},
                        {'name_product':'', 'description':'',
                        'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':''
                        ,'nutrition_100':'','image':''},
                        {'name_product':'', 'description':'',
                        'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':'',
                        'nutrition_100':'','image':''}]
    prod_subs_3 = [{'name_product':'','description':'',
                    'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':'',
                        'nutrition_100':'','image':''},
                        {'name_product':'', 'description':'',
                        'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':''
                        ,'nutrition_100':'','image':''}
                        ,{'name_product':'', 'description':'',
                        'nutriments':'','nutrient_levels':'',
                        'url':'','nutrition_score':'',
                        'nutrition_100':'','image':''}]
    current_user = request.user

    form = SearchForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        
        # Ici nous pouvons traiter les données du formulaire
        product = form.cleaned_data['q']
        

        nutri = list(Product.objects.filter(name_product__contains=product).values('nutrition_score'))[0]
        c = list(Category.objects.filter(cat_product__name_product__contains=product).values('name'))[0]
        if nutri['nutrition_score'] == 'e' or nutri['nutrition_score'] == 'd' or nutri['nutrition_score'] == 'c':
            a = list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values().order_by('?'))[:2]
            a_1 = len(a)
            b = list(Product.objects.filter(category__name=c['name'],nutrition_score='b').values().order_by('?'))[:3]
            b_1 = len(b)
            c = list(Product.objects.filter(category__name=c['name'],nutrition_score='c').values().order_by('?'))[:2]
            c_1 = len(c)
            prod_subs_1[:a_1] = a
            prod_subs_2[:b_1] = b
            prod_subs_3[:c_1] = c
            return render(request,'research/ind_pge_resultat.html',
                         {"prod_name_0": product, 
                          "prod_image_1": '/media/'+prod_subs_1[0]['image'], 
                          "prod_image_2": '/media/'+prod_subs_1[1]['image'],
                          "prod_name_1": prod_subs_1[0]['name_product'],
                          "prod_name_2": prod_subs_1[1]['name_product'],
                          "prod_sub_nut_1":prod_subs_1[0]['nutrition_score'],
                          "prod_sub_nut_2":prod_subs_1[1]['nutrition_score'],
                          "prod_sub_d_1":prod_subs_1[0]['nutriments'],
                          "prod_sub_d_2":prod_subs_1[1]['nutriments'],
                          "prod_sub_n_1":prod_subs_1[0]['nutrient_levels'],
                          "prod_sub_n_2":prod_subs_1[1]['nutrient_levels'],
                          "prod_sub_1_url": prod_subs_1[0]['url'],
                          "prod_sub_2_url": prod_subs_1[1]['url'],

                          "prod_image_3": '/media/'+prod_subs_2[0]['image'],
                          "prod_image_4": '/media/'+prod_subs_2[1]['image'],
                          "prod_image_5": '/media/'+prod_subs_2[2]['image'],
                          "prod_name_3": prod_subs_2[0]['name_product'],
                          "prod_name_4": prod_subs_2[1]['name_product'],
                          "prod_name_5": prod_subs_2[2]['name_product'],
                          "prod_sub_nut_3": prod_subs_2[0]['nutrition_score'],
                          "prod_sub_nut_4": prod_subs_2[1]['nutrition_score'],
                          "prod_sub_nut_5": prod_subs_2[2]['nutrition_score'],
                          "prod_sub_d_3": prod_subs_2[0]['nutriments'],
                          "prod_sub_d_4": prod_subs_2[1]['nutriments'],
                          "prod_sub_d_5": prod_subs_2[2]['nutriments'],
                          "prod_sub_n_3": prod_subs_2[0]['nutrient_levels'],
                          "prod_sub_n_4": prod_subs_2[1]['nutrient_levels'],
                          "prod_sub_n_5": prod_subs_2[2]['nutrient_levels'],
                          "prod_sub_3_url": prod_subs_2[0]['url'],
                          "prod_sub_4_url": prod_subs_2[1]['url'],
                          "prod_sub_5_url": prod_subs_2[2]['url'],
                          
                          "prod_image_6": '/media/'+prod_subs_3[0]['image'],
                          "prod_name_6": prod_subs_3[0]['name_product'],
                          "prod_sub_nut_6": prod_subs_3[0]['nutrition_score'],
                          "prod_sub_d_6": prod_subs_3[0]['nutriments'],
                          "prod_sub_n_6": prod_subs_3[0]['nutrient_levels'],
                          "prod_sub_6_url": prod_subs_3[0]['url']
                          })
             
        
        
        if nutri['nutrition_score'] == 'b' or nutri['nutrition_score'] == 'a':
            a =  list(Product.objects.filter(category__name=c['name'],nutrition_score='a').values())[:7]
            a_1 = len(a)
            prod_subs_1[:a_1] = a
            return render(request,'research/ind_pge_resultat.html',
                         {"prod_name_0": product, 
                          "prod_image_1": '/media/'+prod_subs_1[0]['image'], 
                          "prod_image_2": '/media/'+prod_subs_1[1]['image'],
                          "prod_name_1": prod_subs_1[0]['name_product'],
                          "prod_name_2": prod_subs_1[1]['name_product'],
                          "prod_sub_nut_1":prod_subs_1[0]['nutrition_score'],
                          "prod_sub_nut_2":prod_subs_1[1]['nutrition_score'],
                          "prod_sub_d_1":prod_subs_1[0]['nutriments'],
                          "prod_sub_d_2":prod_subs_1[1]['nutriments'],
                          "prod_sub_n_1":prod_subs_1[0]['nutrient_levels'],
                          "prod_sub_n_2":prod_subs_1[1]['nutrient_levels'],
                          "prod_sub_1_url": prod_subs_1[0]['url'],
                          "prod_sub_2_url": prod_subs_1[1]['url'],

                          "prod_image_3": '/media/'+prod_subs_1[2]['image'],
                          "prod_image_4": '/media/'+prod_subs_1[3]['image'],
                          "prod_image_5": '/media/'+prod_subs_1[4]['image'],
                          "prod_name_3": prod_subs_1[2]['name_product'],
                          "prod_name_4": prod_subs_1[3]['name_product'],
                          "prod_name_5": prod_subs_1[4]['name_product'],
                          "prod_sub_nut_3": prod_subs_1[2]['nutrition_score'],
                          "prod_sub_nut_4": prod_subs_1[3]['nutrition_score'],
                          "prod_sub_nut_5": prod_subs_1[4]['nutrition_score'],
                          "prod_sub_d_3": prod_subs_1[2]['nutriments'],
                          "prod_sub_d_4": prod_subs_1[3]['nutriments'],
                          "prod_sub_d_5": prod_subs_1[4]['nutriments'],
                          "prod_sub_n_3": prod_subs_1[2]['nutrient_levels'],
                          "prod_sub_n_4": prod_subs_1[3]['nutrient_levels'],
                          "prod_sub_n_5": prod_subs_1[4]['nutrient_levels'],

                          "prod_sub_3_url": prod_subs_1[2]['url'],
                          "prod_sub_4_url": prod_subs_1[3]['url'],
                          "prod_sub_5_url": prod_subs_1[4]['url'],
                          
                          "prod_image_6": '/media/'+prod_subs_1[5]['image'],
                          "prod_name_6": prod_subs_1[5]['name_product'],
                          "prod_sub_nut_6": prod_subs_1[5]['nutrition_score'],
                          "prod_sub_d_6": prod_subs_1[5]['nutriments'],
                          "prod_sub_n_6": prod_subs_1[5]['nutrient_levels'],
                          "prod_sub_6_url": prod_subs_1[5]['url']
                          })
        
        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'search.html', locals())