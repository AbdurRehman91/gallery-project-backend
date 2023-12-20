import os
import json
from datetime import datetime
from dotenv import load_dotenv
from bson import json_util
from pymongo import MongoClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
from django.views import View

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")
database = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

client = MongoClient(mongo_uri)
db = client[database]
collection = db[collection_name]

@csrf_exempt
def save_picture(request):
    image_data = json.loads(request.body)
    image_data['created_at'] = datetime.now()
    print("======== obj is :", image_data)
    result = collection.insert_one(image_data)
    inserted_image = collection.find_one({'_id': result.inserted_id})
    nested_obj = {'$oid': str(inserted_image['_id'])}
    return JsonResponse({'_id': nested_obj, 'created_at': inserted_image['created_at'],
                         'title': inserted_image['title'], 'url': inserted_image['url'], 'category': inserted_image['category']})


def pictures(request):
    results = []
    category = request.GET.get('category', '')
    if category:
        results = collection.find({"category":category})
    else:
        results = collection.find({})
    json_result = json.loads(json_util.dumps(list(results)))
    return JsonResponse(json_result, safe=False)
    