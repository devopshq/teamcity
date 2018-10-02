# swagger_client.ServerApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_license_keys**](ServerApi.md#add_license_keys) | **POST** /app/rest/server/licensingData/licenseKeys | 
[**delete_license_key**](ServerApi.md#delete_license_key) | **DELETE** /app/rest/server/licensingData/licenseKeys/{licenseKey} | 
[**get_backup_status**](ServerApi.md#get_backup_status) | **GET** /app/rest/server/backup | 
[**get_children**](ServerApi.md#get_children) | **GET** /app/rest/server/files/{areaId}/children{path} | 
[**get_children_alias**](ServerApi.md#get_children_alias) | **GET** /app/rest/server/files/{areaId}/{path} | 
[**get_content**](ServerApi.md#get_content) | **GET** /app/rest/server/files/{areaId}/content{path} | 
[**get_content_alias**](ServerApi.md#get_content_alias) | **GET** /app/rest/server/files/{areaId}/files{path} | 
[**get_license_key**](ServerApi.md#get_license_key) | **GET** /app/rest/server/licensingData/licenseKeys/{licenseKey} | 
[**get_license_keys**](ServerApi.md#get_license_keys) | **GET** /app/rest/server/licensingData/licenseKeys | 
[**get_licensing_data**](ServerApi.md#get_licensing_data) | **GET** /app/rest/server/licensingData | 
[**get_metadata**](ServerApi.md#get_metadata) | **GET** /app/rest/server/files/{areaId}/metadata{path} | 
[**get_root**](ServerApi.md#get_root) | **GET** /app/rest/server/files/{areaId} | 
[**get_zipped**](ServerApi.md#get_zipped) | **GET** /app/rest/server/files/{areaId}/archived{path} | 
[**serve_plugins**](ServerApi.md#serve_plugins) | **GET** /app/rest/server/plugins | 
[**serve_server_info**](ServerApi.md#serve_server_info) | **GET** /app/rest/server | 
[**serve_server_version**](ServerApi.md#serve_server_version) | **GET** /app/rest/server/{field} | 
[**start_backup**](ServerApi.md#start_backup) | **POST** /app/rest/server/backup | 


# **add_license_keys**
> LicenseKeys add_license_keys(body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
body = 'body_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_license_keys(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->add_license_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**LicenseKeys**](LicenseKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_license_key**
> delete_license_key(license_key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
license_key = 'license_key_example' # str | 

try:
    api_instance.delete_license_key(license_key)
except ApiException as e:
    print("Exception when calling ServerApi->delete_license_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_status**
> str get_backup_status(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
body = swagger_client.BackupProcessManager() # BackupProcessManager |  (optional)

try:
    api_response = api_instance.get_backup_status(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_backup_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupProcessManager**](BackupProcessManager.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children**
> Files get_children(path, area_id, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_children(path, area_id, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_alias**
> Files get_children_alias(path, area_id, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_children_alias(path, area_id, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_children_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content**
> get_content(path, area_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 

try:
    api_instance.get_content(path, area_id)
except ApiException as e:
    print("Exception when calling ServerApi->get_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_alias**
> get_content_alias(path, area_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 

try:
    api_instance.get_content_alias(path, area_id)
except ApiException as e:
    print("Exception when calling ServerApi->get_content_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_key**
> LicenseKey get_license_key(license_key, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
license_key = 'license_key_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_license_key(license_key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_license_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**LicenseKey**](LicenseKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_keys**
> LicenseKeys get_license_keys(fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_license_keys(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_license_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**LicenseKeys**](LicenseKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licensing_data**
> LicensingData get_licensing_data(fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_licensing_data(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_licensing_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**LicensingData**](LicensingData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> file get_metadata(path, area_id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_metadata(path, area_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> Files get_root(area_id, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
area_id = 'area_id_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_root(area_id, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_id** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zipped**
> get_zipped(path, area_id, base_path=base_path, locator=locator, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
path = 'path_example' # str | 
area_id = 'area_id_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    api_instance.get_zipped(path, area_id, base_path=base_path, locator=locator, name=name)
except ApiException as e:
    print("Exception when calling ServerApi->get_zipped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **area_id** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_plugins**
> Plugins serve_plugins(fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_plugins(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->serve_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Plugins**](Plugins.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_server_info**
> Server serve_server_info(fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_server_info(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->serve_server_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Server**](Server.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_server_version**
> str serve_server_version(field)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_server_version(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->serve_server_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_backup**
> str start_backup(file_name=file_name, add_timestamp=add_timestamp, include_configs=include_configs, include_database=include_database, include_build_logs=include_build_logs, include_personal_changes=include_personal_changes, include_running_builds=include_running_builds, include_supplimentary_data=include_supplimentary_data, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
file_name = 'file_name_example' # str |  (optional)
add_timestamp = true # bool |  (optional)
include_configs = true # bool |  (optional)
include_database = true # bool |  (optional)
include_build_logs = true # bool |  (optional)
include_personal_changes = true # bool |  (optional)
include_running_builds = true # bool |  (optional)
include_supplimentary_data = true # bool |  (optional)
body = swagger_client.BackupProcessManager() # BackupProcessManager |  (optional)

try:
    api_response = api_instance.start_backup(file_name=file_name, add_timestamp=add_timestamp, include_configs=include_configs, include_database=include_database, include_build_logs=include_build_logs, include_personal_changes=include_personal_changes, include_running_builds=include_running_builds, include_supplimentary_data=include_supplimentary_data, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->start_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | [optional] 
 **add_timestamp** | **bool**|  | [optional] 
 **include_configs** | **bool**|  | [optional] 
 **include_database** | **bool**|  | [optional] 
 **include_build_logs** | **bool**|  | [optional] 
 **include_personal_changes** | **bool**|  | [optional] 
 **include_running_builds** | **bool**|  | [optional] 
 **include_supplimentary_data** | **bool**|  | [optional] 
 **body** | [**BackupProcessManager**](BackupProcessManager.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

