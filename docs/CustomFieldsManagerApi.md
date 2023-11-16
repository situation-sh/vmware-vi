# vmware_vi.CustomFieldsManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_fields_manager_add_custom_field_def**](CustomFieldsManagerApi.md#custom_fields_manager_add_custom_field_def) | **POST** /CustomFieldsManager/{moId}/AddCustomFieldDef | Creates a new custom field. 
[**custom_fields_manager_get_field**](CustomFieldsManagerApi.md#custom_fields_manager_get_field) | **GET** /CustomFieldsManager/{moId}/field | List of custom fields defined on this server. 
[**custom_fields_manager_remove_custom_field_def**](CustomFieldsManagerApi.md#custom_fields_manager_remove_custom_field_def) | **POST** /CustomFieldsManager/{moId}/RemoveCustomFieldDef | Removes a custom field. 
[**custom_fields_manager_rename_custom_field_def**](CustomFieldsManagerApi.md#custom_fields_manager_rename_custom_field_def) | **POST** /CustomFieldsManager/{moId}/RenameCustomFieldDef | Renames a custom field. 
[**custom_fields_manager_set_field**](CustomFieldsManagerApi.md#custom_fields_manager_set_field) | **POST** /CustomFieldsManager/{moId}/SetField | Assigns a value to a custom field on an entity. 


# **custom_fields_manager_add_custom_field_def**
> CustomFieldDef custom_fields_manager_add_custom_field_def(mo_id, add_custom_field_def_request_type)

Creates a new custom field. 

Creates a new custom field.  If the moType is specified, the field will only be available for that type of managed object.  ***Required privileges:*** Global.ManageCustomFields 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_custom_field_def_request_type import AddCustomFieldDefRequestType
from vmware_vi.models.custom_field_def import CustomFieldDef
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.CustomFieldsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_custom_field_def_request_type = vmware_vi.AddCustomFieldDefRequestType() # AddCustomFieldDefRequestType | 

    try:
        # Creates a new custom field. 
        api_response = api_instance.custom_fields_manager_add_custom_field_def(mo_id, add_custom_field_def_request_type)
        print("The response of CustomFieldsManagerApi->custom_fields_manager_add_custom_field_def:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsManagerApi->custom_fields_manager_add_custom_field_def: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_custom_field_def_request_type** | [**AddCustomFieldDefRequestType**](AddCustomFieldDefRequestType.md)|  | 

### Return type

[**CustomFieldDef**](CustomFieldDef.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***DuplicateName***: if a custom field with the name already exists.  ***InvalidPrivilege***: if a specified privilege is not defined.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_manager_get_field**
> List[CustomFieldDef] custom_fields_manager_get_field(mo_id)

List of custom fields defined on this server. 

List of custom fields defined on this server.  The fields are sorted by name.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_def import CustomFieldDef
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.CustomFieldsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom fields defined on this server. 
        api_response = api_instance.custom_fields_manager_get_field(mo_id)
        print("The response of CustomFieldsManagerApi->custom_fields_manager_get_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsManagerApi->custom_fields_manager_get_field: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldDef]**](CustomFieldDef.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_manager_remove_custom_field_def**
> custom_fields_manager_remove_custom_field_def(mo_id, remove_custom_field_def_request_type)

Removes a custom field. 

Removes a custom field.  This also removes all values assigned to this custom field.  ***Required privileges:*** Global.ManageCustomFields 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_custom_field_def_request_type import RemoveCustomFieldDefRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.CustomFieldsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_custom_field_def_request_type = vmware_vi.RemoveCustomFieldDefRequestType() # RemoveCustomFieldDefRequestType | 

    try:
        # Removes a custom field. 
        api_instance.custom_fields_manager_remove_custom_field_def(mo_id, remove_custom_field_def_request_type)
    except Exception as e:
        print("Exception when calling CustomFieldsManagerApi->custom_fields_manager_remove_custom_field_def: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_custom_field_def_request_type** | [**RemoveCustomFieldDefRequestType**](RemoveCustomFieldDefRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_manager_rename_custom_field_def**
> custom_fields_manager_rename_custom_field_def(mo_id, rename_custom_field_def_request_type)

Renames a custom field. 

Renames a custom field.  ***Required privileges:*** Global.ManageCustomFields 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.rename_custom_field_def_request_type import RenameCustomFieldDefRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.CustomFieldsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_custom_field_def_request_type = vmware_vi.RenameCustomFieldDefRequestType() # RenameCustomFieldDefRequestType | 

    try:
        # Renames a custom field. 
        api_instance.custom_fields_manager_rename_custom_field_def(mo_id, rename_custom_field_def_request_type)
    except Exception as e:
        print("Exception when calling CustomFieldsManagerApi->custom_fields_manager_rename_custom_field_def: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_custom_field_def_request_type** | [**RenameCustomFieldDefRequestType**](RenameCustomFieldDefRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidArgument***: if no custom field with that key exists.  ***DuplicateName***: if a custom field with the name already exists.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_manager_set_field**
> custom_fields_manager_set_field(mo_id, set_field_request_type)

Assigns a value to a custom field on an entity. 

Assigns a value to a custom field on an entity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_field_request_type import SetFieldRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.CustomFieldsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_field_request_type = vmware_vi.SetFieldRequestType() # SetFieldRequestType | 

    try:
        # Assigns a value to a custom field on an entity. 
        api_instance.custom_fields_manager_set_field(mo_id, set_field_request_type)
    except Exception as e:
        print("Exception when calling CustomFieldsManagerApi->custom_fields_manager_set_field: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_field_request_type** | [**SetFieldRequestType**](SetFieldRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

