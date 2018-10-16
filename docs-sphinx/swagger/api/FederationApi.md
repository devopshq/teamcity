# dohq_teamcity.FederationApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/FederationApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_server**](FederationApi.md#add_server) | **PUT** /app/rest/federation/servers | 
[**servers**](FederationApi.md#servers) | **GET** /app/rest/federation/servers | 


# **add_server**
> Servers add_server(body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

body = dohq_teamcity.Servers() # Servers |  (optional)

try:
    api_response = tc.federation_api.add_server(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FederationApi->add_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servers**](Servers.md)|  | [optional] 

### Return type

[**Servers**](../models/Servers.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **servers**
> Servers servers(fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.federation_api.servers(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FederationApi->servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Servers**](../models/Servers.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


