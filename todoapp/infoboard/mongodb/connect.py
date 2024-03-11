from pymongo import MongoClient
from django.conf import settings

client = MongoClient(
    host='mongodb+srv://Vladislav_B:dIvg5BCNadnWGk7E@hwmongobase.o1jywze.mongodb.net/?retryWrites=true&w=majority'
)
db = client['Celery']