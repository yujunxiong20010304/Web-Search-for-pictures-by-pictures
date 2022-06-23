from django.http import JsonResponse
import json
import base64
import numpy as np
import cv2
from utils import lookup
from .models import Goods


# Create your views here.
def search_view(request):
    data = json.loads(request.body)
    image = data.get('image')
    img = image.split(',')[1]
    img_data = base64.b64decode(img)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    query_info = lookup.lookup(img)
    image_name = query_info.get('image_name')
    probability = query_info.get('probability')
    result = []
    for i in image_name[:7]:
        id = str(i).split('.')[0].split("'")[1]
        data = Goods.objects.filter(id=id).values().first()
        result.append(data)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': result})
