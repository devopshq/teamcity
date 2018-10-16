# dohq_teamcity.UserApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/UserApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](UserApi.md#add_group) | **POST** /app/rest/users/{userLocator}/groups | 
[**add_role**](UserApi.md#add_role) | **POST** /app/rest/users/{userLocator}/roles | 
[**add_role_simple**](UserApi.md#add_role_simple) | **PUT** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
[**add_role_simple_post**](UserApi.md#add_role_simple_post) | **POST** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
[**create_user**](UserApi.md#create_user) | **POST** /app/rest/users | 
[**delete_remember_me**](UserApi.md#delete_remember_me) | **DELETE** /app/rest/users/{userLocator}/debug/rememberMe | 
[**delete_role**](UserApi.md#delete_role) | **DELETE** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
[**delete_user**](UserApi.md#delete_user) | **DELETE** /app/rest/users/{userLocator} | 
[**delete_user_field**](UserApi.md#delete_user_field) | **DELETE** /app/rest/users/{userLocator}/{field} | 
[**get_groups**](UserApi.md#get_groups) | **GET** /app/rest/users/{userLocator}/groups | 
[**get_permissions**](UserApi.md#get_permissions) | **GET** /app/rest/users/{userLocator}/debug/permissions | 
[**list_role**](UserApi.md#list_role) | **GET** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
[**list_roles**](UserApi.md#list_roles) | **GET** /app/rest/users/{userLocator}/roles | 
[**put_user_property**](UserApi.md#put_user_property) | **PUT** /app/rest/users/{userLocator}/properties/{name} | 
[**remove_user_property**](UserApi.md#remove_user_property) | **DELETE** /app/rest/users/{userLocator}/properties/{name} | 
[**replace_groups**](UserApi.md#replace_groups) | **PUT** /app/rest/users/{userLocator}/groups | 
[**replace_roles**](UserApi.md#replace_roles) | **PUT** /app/rest/users/{userLocator}/roles | 
[**serve_user**](UserApi.md#serve_user) | **GET** /app/rest/users/{userLocator} | 
[**serve_user_field**](UserApi.md#serve_user_field) | **GET** /app/rest/users/{userLocator}/{field} | 
[**serve_user_properties**](UserApi.md#serve_user_properties) | **GET** /app/rest/users/{userLocator}/properties | 
[**serve_user_property**](UserApi.md#serve_user_property) | **GET** /app/rest/users/{userLocator}/properties/{name} | 
[**serve_users**](UserApi.md#serve_users) | **GET** /app/rest/users | 
[**set_user_field**](UserApi.md#set_user_field) | **PUT** /app/rest/users/{userLocator}/{field} | 
[**update_user**](UserApi.md#update_user) | **PUT** /app/rest/users/{userLocator} | 


# **add_group**
> Group add_group(user_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
body = dohq_teamcity.Group() # Group |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.add_group(user_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **body** | [**Group**](Group.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Group**](../models/Group.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **add_role**
> Role add_role(user_locator, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
body = dohq_teamcity.Role() # Role |  (optional)

try:
    api_response = tc.user_api.add_role(user_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **body** | [**Role**](Role.md)|  | [optional] 

### Return type

[**Role**](../models/Role.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **add_role_simple**
> Role add_role_simple(user_locator, role_id, scope)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    api_response = tc.user_api.add_role_simple(user_locator, role_id, scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_role_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**Role**](../models/Role.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **add_role_simple_post**
> add_role_simple_post(user_locator, role_id, scope)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    tc.user_api.add_role_simple_post(user_locator, role_id, scope)
except ApiException as e:
    print("Exception when calling UserApi->add_role_simple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **create_user**
> User create_user(body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

body = dohq_teamcity.User() # User |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.create_user(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**User**](../models/User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_remember_me**
> delete_remember_me(user_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 

try:
    tc.user_api.delete_remember_me(user_locator)
except ApiException as e:
    print("Exception when calling UserApi->delete_remember_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_role**
> delete_role(user_locator, role_id, scope)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    tc.user_api.delete_role(user_locator, role_id, scope)
except ApiException as e:
    print("Exception when calling UserApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_user**
> delete_user(user_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 

try:
    tc.user_api.delete_user(user_locator)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_user_field**
> delete_user_field(user_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
field = 'field_example' # str | 

try:
    tc.user_api.delete_user_field(user_locator, field)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_groups**
> Groups get_groups(user_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.get_groups(user_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Groups**](../models/Groups.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_permissions**
> str get_permissions(user_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 

try:
    api_response = tc.user_api.get_permissions(user_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **list_role**
> Role list_role(user_locator, role_id, scope)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    api_response = tc.user_api.list_role(user_locator, role_id, scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**Role**](../models/Role.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **list_roles**
> Roles list_roles(user_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 

try:
    api_response = tc.user_api.list_roles(user_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 

### Return type

[**Roles**](../models/Roles.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **put_user_property**
> str put_user_property(user_locator, name, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.user_api.put_user_property(user_locator, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->put_user_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **remove_user_property**
> remove_user_property(user_locator, name)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
name = 'name_example' # str | 

try:
    tc.user_api.remove_user_property(user_locator, name)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **replace_groups**
> Groups replace_groups(user_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
body = dohq_teamcity.Groups() # Groups |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.replace_groups(user_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->replace_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **body** | [**Groups**](Groups.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Groups**](../models/Groups.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **replace_roles**
> Roles replace_roles(user_locator, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
body = dohq_teamcity.Roles() # Roles |  (optional)

try:
    api_response = tc.user_api.replace_roles(user_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->replace_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **body** | [**Roles**](Roles.md)|  | [optional] 

### Return type

[**Roles**](../models/Roles.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_user**
> User serve_user(user_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.serve_user(user_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->serve_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**User**](../models/User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_user_field**
> str serve_user_field(user_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.user_api.serve_user_field(user_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->serve_user_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_user_properties**
> Properties serve_user_properties(user_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.serve_user_properties(user_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->serve_user_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_user_property**
> str serve_user_property(user_locator, name)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_response = tc.user_api.serve_user_property(user_locator, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->serve_user_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_users**
> Users serve_users(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.serve_users(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->serve_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Users**](../models/Users.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_user_field**
> str set_user_field(user_locator, field, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.user_api.set_user_field(user_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **update_user**
> User update_user(user_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

user_locator = 'user_locator_example' # str | 
body = dohq_teamcity.User() # User |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.user_api.update_user(user_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_locator** | **str**|  | 
 **body** | [**User**](User.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**User**](../models/User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


