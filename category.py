import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amateurs_nutella.settings")
from django.db import models
from research.models import *

records_to_insert = ['Viennoiseries', 'Snacks', 'Epicerie', 'Desserts', 'pizza']
for elt in records_to_insert:
	name = Category(name=elt)
	name.save()