# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import requests
# # Create your views here.

# class GoogleTrendAPI(APIView):
#     def get(self,request, format=None):
#         try:
#             google_trend_api = 'https://serpapi.com/search.json'
#             queries = request.query_params.get('query'),
#             date = request.query_params.get('date'),
#             print("queries is ",queries)
#             print("date is ",date)
#             params = {
#                     'engine': 'google_trends',
#                     'q': queries,
#                     'data_type': 'TIMESERIES',
#                     'date': date,
#                     'api_key': '831422e6277f38bad4b744b442213b3508484db93f8b036ed3805ccfe83fd04d',
#                 }
#             response = requests.get(google_trend_api,params=params)

#             if(response.status_code == 200):
#                 api_data = response.json()
#                 return Response(api_data)
#             else:
#                 return Response({"error":"Request failed"}, status=response.status_code)
#         except Exception as e:
#             return Response({'error':str(e)},status=500)

        
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os

# Create your views here.

class GoogleTrendAPI(APIView):
    def get(self, request, format=None):
        try:
            google_trend_api = 'https://serpapi.com/search.json'
            queries = request.query_params.get('query')
            date = request.query_params.get('date')

            # If queries are a tuple, get the first item
            queries = queries[0] if isinstance(queries, tuple) else queries
            date = date[0] if isinstance(date, tuple) else date

            print(f"Queries: {queries}, Date: {date}")

            if not queries or not date:
                return Response({"error": "Query or date parameters are missing"}, status=400)

            params = {
                'engine': 'google_trends',
                'q': queries,
                'data_type': 'TIMESERIES',
                'date': date,
                'api_key': '',
            }

            # Send request to SerpAPI
            response = requests.get(google_trend_api, params=params)

            # Log the response from SerpAPI
            print(f"SerpAPI response: {response.status_code} - {response.text}")

            if response.status_code == 200:
                api_data = response.json()
                return Response(api_data)
            else:
                return Response({"error": f"Request failed with status {response.status_code}"}, status=response.status_code)
        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({'error': str(e)}, status=500)
