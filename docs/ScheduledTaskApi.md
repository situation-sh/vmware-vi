# vmware_vi.ScheduledTaskApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduled_task_get_available_field**](ScheduledTaskApi.md#scheduled_task_get_available_field) | **GET** /ScheduledTask/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**scheduled_task_get_info**](ScheduledTaskApi.md#scheduled_task_get_info) | **GET** /ScheduledTask/{moId}/info | Information about the current scheduled task. 
[**scheduled_task_get_value**](ScheduledTaskApi.md#scheduled_task_get_value) | **GET** /ScheduledTask/{moId}/value | List of custom field values. 
[**scheduled_task_reconfigure_scheduled_task**](ScheduledTaskApi.md#scheduled_task_reconfigure_scheduled_task) | **POST** /ScheduledTask/{moId}/ReconfigureScheduledTask | Reconfigures the scheduled task properties. 
[**scheduled_task_remove_scheduled_task**](ScheduledTaskApi.md#scheduled_task_remove_scheduled_task) | **POST** /ScheduledTask/{moId}/RemoveScheduledTask | Removes the scheduled task. 
[**scheduled_task_run_scheduled_task**](ScheduledTaskApi.md#scheduled_task_run_scheduled_task) | **POST** /ScheduledTask/{moId}/RunScheduledTask | Runs the scheduled task immediately. 
[**scheduled_task_set_custom_value**](ScheduledTaskApi.md#scheduled_task_set_custom_value) | **POST** /ScheduledTask/{moId}/setCustomValue | Assigns a value to a custom field. 


# **scheduled_task_get_available_field**
> List[CustomFieldDef] scheduled_task_get_available_field(mo_id)

List of custom field definitions that are valid for the object's type. 

List of custom field definitions that are valid for the object's type.  The fields are sorted by *CustomFieldDef.name*.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.scheduled_task_get_available_field(mo_id)
        print("The response of ScheduledTaskApi->scheduled_task_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_get_available_field: %s\n" % e)
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

# **scheduled_task_get_info**
> ScheduledTaskInfo scheduled_task_get_info(mo_id)

Information about the current scheduled task. 

Information about the current scheduled task. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.scheduled_task_info import ScheduledTaskInfo
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about the current scheduled task. 
        api_response = api_instance.scheduled_task_get_info(mo_id)
        print("The response of ScheduledTaskApi->scheduled_task_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ScheduledTaskInfo**](ScheduledTaskInfo.md)

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

# **scheduled_task_get_value**
> List[CustomFieldValue] scheduled_task_get_value(mo_id)

List of custom field values. 

List of custom field values.  Each value uses a key to associate an instance of a *CustomFieldStringValue* with a custom field definition.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_value import CustomFieldValue
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.scheduled_task_get_value(mo_id)
        print("The response of ScheduledTaskApi->scheduled_task_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_get_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldValue]**](CustomFieldValue.md)

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

# **scheduled_task_reconfigure_scheduled_task**
> scheduled_task_reconfigure_scheduled_task(mo_id, reconfigure_scheduled_task_request_type)

Reconfigures the scheduled task properties. 

Reconfigures the scheduled task properties.  ***Required privileges:*** ScheduledTask.Edit 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfigure_scheduled_task_request_type import ReconfigureScheduledTaskRequestType
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_scheduled_task_request_type = vmware_vi.ReconfigureScheduledTaskRequestType() # ReconfigureScheduledTaskRequestType | 

    try:
        # Reconfigures the scheduled task properties. 
        api_instance.scheduled_task_reconfigure_scheduled_task(mo_id, reconfigure_scheduled_task_request_type)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_reconfigure_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_scheduled_task_request_type** | [**ReconfigureScheduledTaskRequestType**](ReconfigureScheduledTaskRequestType.md)|  | 

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
**500** | ***InvalidState***: if the scheduled task is running.  ***InvalidName***: if the scheduled task name is empty or too long.  ***DuplicateName***: if a scheduled task with the name already exists.  ***InvalidArgument***: if the specification is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_remove_scheduled_task**
> scheduled_task_remove_scheduled_task(mo_id)

Removes the scheduled task. 

Removes the scheduled task.  ***Required privileges:*** ScheduledTask.Delete 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes the scheduled task. 
        api_instance.scheduled_task_remove_scheduled_task(mo_id)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_remove_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidState***: if the scheduled task is running.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_run_scheduled_task**
> scheduled_task_run_scheduled_task(mo_id)

Runs the scheduled task immediately. 

Runs the scheduled task immediately.  The schedule for future runs remains in effect.  ***Required privileges:*** ScheduledTask.Run 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Runs the scheduled task immediately. 
        api_instance.scheduled_task_run_scheduled_task(mo_id)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_run_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidState***: if the scheduled task is running already.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_set_custom_value**
> scheduled_task_set_custom_value(mo_id, set_custom_value_request_type)

Assigns a value to a custom field. 

Assigns a value to a custom field.  The setCustomValue method requires whichever updatePrivilege is defined as one of the *CustomFieldDef.fieldInstancePrivileges* for the CustomFieldDef whose value is being changed.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_custom_value_request_type import SetCustomValueRequestType
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
    api_instance = vmware_vi.ScheduledTaskApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.scheduled_task_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling ScheduledTaskApi->scheduled_task_set_custom_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_custom_value_request_type** | [**SetCustomValueRequestType**](SetCustomValueRequestType.md)|  | 

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

