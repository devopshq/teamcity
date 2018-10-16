#################
dohq_teamcity.FederationApi
#################


All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_server**](FederationApi.md#add_server) | **PUT** /app/rest/federation/servers | 
[**servers**](FederationApi.md#servers) | **GET** /app/rest/federation/servers | 


# **add_server**
> Servers add_server(body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.FederationApi()
body = dohq_teamcity.Servers() # Servers |  (optional)

try:
    api_response = api_instance.add_server(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FederationApi->add_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servers**](Servers.md)|  | [optional] 

### Return type

[**Servers**](Servers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers**
> Servers servers(fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.FederationApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.servers(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FederationApi->servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Servers**](Servers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

