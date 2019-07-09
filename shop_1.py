
# coding: utf-8
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amateurs_nutella.settings")
from django.db import models
from research.models import *

import requests

payload = {"search_terms": "pizza","search_tag": "categories","page_size": 200, "json": 1}
res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

# url result
res.url
liste_store = []
# Take the product
results = res.json()
products = results["products"]

# Display the product names
for product in products:
	print(product['nutrition_score_debug'])
	if 'stores' in product.keys():
		liste_store.append(product['stores'])

liste_coma = []
coma = ","
# fonction  to construct a store list
for store in liste_store:
	if coma in store:
		liste_coma.append(store)		

for element in liste_coma:
	b = element.split(",")
	for a in b:

		liste_store.append(a)
for c in liste_coma:
	
	liste_store.remove(c)
liste_store = list(set(liste_store))
liste_store.remove('')
records_to_insert = []
for elt in liste_store:
	name = Shop(name_shop=elt)
	name.save()

