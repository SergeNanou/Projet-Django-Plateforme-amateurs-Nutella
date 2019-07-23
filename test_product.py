# coding: utf-8
import os
import django
import requests
import regex as re


import tempfile
from django.db import models
from research.models import *
from  django.core.files import File


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amateurs_nutella.settings")
django.setup()


search = ['pizza', 'viennoiseries', 'Snacks', 'Epicerie', 'Desserts']
d_store ={}
	# Openfoodfacts API request to take a data for category types

# for store in liste_store:
# 	s = Shop(name_shop = store)
# 	s.save()
# 	d_store[store] = s
# print(d_store)
for search_term in search:
	c = Category(name=search_term)
	c.save()
		
	payload = {"search_terms": search_term,"search_tag": 
                   "categories","page_size": 1000, "json": 1}
	res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", 
                            params=payload)
	# url result 
	res.url
	liste_store = []
	# result of json request 
	results = res.json()
	products = results["products"]
		# selection data  type 
	for product in products:
	# test to ensure the our attributs presence 
		if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys() and 'image_front_url'in product.keys() and 'nutriments' in product.keys() and 'nutrient_levels' in product.keys():
			if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys() and  'stores' in product.keys() and 'nutrition_score_debug' in product.keys():
				store = product['stores']
				code = product['code']
				nutri = product['nutrition_grade_fr']
				nutri = re.sub(r"\p{P}+", r"", nutri)
				prod = product['product_name_fr']
				nutri_100 = product['nutrition_score_debug']
				# regex to delete punctuation in data
				prod =  re.sub(r"\p{P}+", r"", prod) 
				url = product['url']
				ingred = product['ingredients_text_fr']
				ingred = re.sub(r"\p{P}+", r"", ingred)
				nutriments = product['nutriments']
				# nutriments = re.sub(r"\p{P}+", r"", nutriments)
				nutrient_levels = product['nutrient_levels']
				# nutrient_levels = re.sub(r"\p{P}+", r"", nutrient_levels)

				# nutri_1.save()
				# url_1 = Product(url=url)
				# url_1.save()
				# ingred_1 = Product(description=ingred)
				# ingred_1.save()
				# prod_1 = Product(name_product=prod)
				# prod_1.save()
				image_url = product['image_front_url']
				request = requests.get(image_url, stream=True)

    			# Was the request OK?
				if request.status_code != requests.codes.ok:
				# Nope, error handling, skip file etc etc etc
					continue

				# Get the filename from the url, used for saving later
				file_name = image_url.split('/')[-1]
				#print(file_name)
				# Create a temporary file
				lf = tempfile.NamedTemporaryFile()

				# Read the streamed image in sections
				for block in request.iter_content(1024 * 8):

					# If no more file then stop
					if not block:
						break

					# Write image block to temporary file
					lf.write(block)
					lf.flush()
				# Create the model you want to save the image to
				
				# a = Product(image=(file_name, File(lf)))
				p = Product(nutrition_score=nutri,url=url,
					        description=ingred,name_product=prod, 
					        nutrition_100=nutri_100,
					        nutriments=nutriments, 
					        nutrient_levels= nutrient_levels)
				p.image.save(file_name, File(lf))
				p.save()
	
				p.category.add(c)
				# if store in liste_store:
				# 	p.shop.add(d_store[store])
				# Save the temporary image to the model#
				# This saves the model so be sure that is it valid

					
