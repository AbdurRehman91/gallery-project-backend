import os
import json
from dotenv import load_dotenv
from bson import json_util
from pymongo import MongoClient
from django.http import JsonResponse    
from django.views import View

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")
database = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

client = MongoClient(mongo_uri)
db = client[database]
collection = db[collection_name]

class ImageListView(View):
    def get(self, request):
        results = []
        category = request.GET.get('category', '')
        if category:
            results = collection.find({"category":category})
        else:
            results = collection.find({})
        json_result = json.loads(json_util.dumps(list(results)))
        return JsonResponse(json_result, safe=False)
    