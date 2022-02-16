import json

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from mixin import MixinHttpResponse


# Create your views here.


class JsonCbv(View):
    def get(self, request, *args, **kwargs):
        data = {'msg': 'this is form get method'}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = {'msg': 'this is form post method'}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        data = {'msg': 'this is form put method'}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        data = {'msg': 'this is form delete method'}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)

    def render_to_http_response(self, json_data):
        pass
