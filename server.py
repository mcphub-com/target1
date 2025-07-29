import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/target1'

mcp = FastMCP('target1')

@mcp.tool()
def auto_complete(q: Annotated[str, Field(description='Any familiar term or phrase to search for products')]) -> dict: 
    '''Get suggestion by term or phrase'''
    url = 'https://target1.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list(category: Annotated[Union[str, None], Field(description='Used to list child categories, you need to parse the value of target field (taxonomy_nodes->actions->target) OR children->node_id returned right in this endpoint, such as : ...?category=5xtg6')] = None) -> dict: 
    '''List all root and sub categories'''
    url = 'https://target1.p.rapidapi.com/categories/v2/list'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def categories_list(category: Annotated[Union[str, None], Field(description='Used to list child categories, you need to parse the value of target field returned right in this endpoint, such as : ...?category=5xtg6')] = None) -> dict: 
    '''List all root and sub categories'''
    url = 'https://target1.p.rapidapi.com/categories/list'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_search_by_barcode(store_id: Annotated[str, Field(description='The value of location_id returned in …/stores/list endpoint')],
                               barcode: Annotated[str, Field(description='The barcode')]) -> dict: 
    '''Search product by barcode'''
    url = 'https://target1.p.rapidapi.com/products/search-by-barcode'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store_id': store_id,
        'barcode': barcode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_details(tcin: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/v2/list or .../products/search-by-barcode endpoint Default: 54191097')],
                   store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''Get detail information of product'''
    url = 'https://target1.p.rapidapi.com/products/v3/get-details'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcin': tcin,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list_recommended(tcins: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                        store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''List more products to consider'''
    url = 'https://target1.p.rapidapi.com/products/v2/list-recommended'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcins': tcins,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_list_recommended(tcins: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                              store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''List more products to consider'''
    url = 'https://target1.p.rapidapi.com/products/list-recommended'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcins': tcins,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_list(storeId: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')],
                  endecaId: Annotated[str, Field(description='You need to parse the value of target field returned in .../categories/list endpoint, such as : ...?category=o9rnh. Please notice that do NOT use searchTerm and endecaId parameters together, searchTerm OR endecaId is required.')],
                  pageSize: Annotated[Union[int, float, None], Field(description='For paging purpose, maximum 20 items per page. Default: 20')] = None,
                  pageNumber: Annotated[Union[int, float, None], Field(description='For paging purpose Default: 1')] = None,
                  sortBy: Annotated[Union[str, None], Field(description='One of the following is allowed relevance|newest|RatingHigh|bestselling|PriceLow|PriceHigh')] = None,
                  searchTerm: Annotated[Union[str, None], Field(description='Search for products by term or phrase, such as : macbook air. Please notice that do NOT use searchTerm and endecaId parameters together, searchTerm OR endecaId is required.')] = None,
                  storeSearch: Annotated[Union[bool, None], Field(description='Only search for In-store products')] = None,
                  facets: Annotated[Union[str, None], Field(description='Look for suitable values returned under facetView/Entry/ExtendedData/value JSON object, separated by comma for multiple options, such as : 5tal2,q643lesaelr,etc...')] = None) -> dict: 
    '''List products in specific store with options and filters'''
    url = 'https://target1.p.rapidapi.com/products/list'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'storeId': storeId,
        'endecaId': endecaId,
        'pageSize': pageSize,
        'pageNumber': pageNumber,
        'sortBy': sortBy,
        'searchTerm': searchTerm,
        'storeSearch': storeSearch,
        'facets': facets,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_list_collection(tcin: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                             store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''List whole collection relating to a product'''
    url = 'https://target1.p.rapidapi.com/products/list-collection'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcin': tcin,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_get_details(tcin: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                         store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''Get detail information of product'''
    url = 'https://target1.p.rapidapi.com/products/get-details'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcin': tcin,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_details(tcin: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                   store_id: Annotated[Union[int, float], Field(description='The value of location_id returned in .../stores/list endpoint Default: 911')]) -> dict: 
    '''Get detail information of product'''
    url = 'https://target1.p.rapidapi.com/products/v2/get-details'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcin': tcin,
        'store_id': store_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reviews_list(tcin: Annotated[Union[int, float], Field(description='The value of tcin field returned in .../products/list endpoint Default: 54191097')],
                 sort: Annotated[Union[str, None], Field(description='One of the following is allowed time_desc|helpfulness_desc|rating_desc|rating_asc')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='For paging purpose, maximum items per page is 30 Default: 30')] = None,
                 offset: Annotated[Union[int, float, None], Field(description='For paging purpose Default: 0')] = None) -> dict: 
    '''List reviews relating to a product'''
    url = 'https://target1.p.rapidapi.com/reviews/list'
    headers = {'x-rapidapi-host': 'target1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tcin': tcin,
        'sort': sort,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
