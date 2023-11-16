# vmware_vi.ScheduledTaskManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduled_task_manager_create_object_scheduled_task**](ScheduledTaskManagerApi.md#scheduled_task_manager_create_object_scheduled_task) | **POST** /ScheduledTaskManager/{moId}/CreateObjectScheduledTask | Creates a scheduled task. 
[**scheduled_task_manager_create_scheduled_task**](ScheduledTaskManagerApi.md#scheduled_task_manager_create_scheduled_task) | **POST** /ScheduledTaskManager/{moId}/CreateScheduledTask | Creates a scheduled task. 
[**scheduled_task_manager_get_description**](ScheduledTaskManagerApi.md#scheduled_task_manager_get_description) | **GET** /ScheduledTaskManager/{moId}/description | Static descriptive strings used in scheduled tasks. 
[**scheduled_task_manager_get_scheduled_task**](ScheduledTaskManagerApi.md#scheduled_task_manager_get_scheduled_task) | **GET** /ScheduledTaskManager/{moId}/scheduledTask | All available scheduled tasks. 
[**scheduled_task_manager_retrieve_entity_scheduled_task**](ScheduledTaskManagerApi.md#scheduled_task_manager_retrieve_entity_scheduled_task) | **POST** /ScheduledTaskManager/{moId}/RetrieveEntityScheduledTask | Available scheduled tasks defined on the entity. 
[**scheduled_task_manager_retrieve_object_scheduled_task**](ScheduledTaskManagerApi.md#scheduled_task_manager_retrieve_object_scheduled_task) | **POST** /ScheduledTaskManager/{moId}/RetrieveObjectScheduledTask | Available scheduled tasks defined on the object. 


# **scheduled_task_manager_create_object_scheduled_task**
> ManagedObjectReference scheduled_task_manager_create_object_scheduled_task(mo_id, create_object_scheduled_task_request_type)

Creates a scheduled task. 

Creates a scheduled task.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_object_scheduled_task_request_type import CreateObjectScheduledTaskRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_object_scheduled_task_request_type = vmware_vi.CreateObjectScheduledTaskRequestType() # CreateObjectScheduledTaskRequestType | 

    try:
        # Creates a scheduled task. 
        api_response = api_instance.scheduled_task_manager_create_object_scheduled_task(mo_id, create_object_scheduled_task_request_type)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_create_object_scheduled_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_create_object_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_object_scheduled_task_request_type** | [**CreateObjectScheduledTaskRequestType**](CreateObjectScheduledTaskRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled task created by the operation.  Refers instance of *ScheduledTask*.  |  -  |
**500** | ***InvalidName***: if the scheduled task name is empty or too long.  ***DuplicateName***: if a scheduled task with the name already exists.  ***InvalidArgument***: if the specification is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_manager_create_scheduled_task**
> ManagedObjectReference scheduled_task_manager_create_scheduled_task(mo_id, create_scheduled_task_request_type)

Creates a scheduled task. 

Creates a scheduled task. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_scheduled_task_request_type import CreateScheduledTaskRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_scheduled_task_request_type = vmware_vi.CreateScheduledTaskRequestType() # CreateScheduledTaskRequestType | 

    try:
        # Creates a scheduled task. 
        api_response = api_instance.scheduled_task_manager_create_scheduled_task(mo_id, create_scheduled_task_request_type)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_create_scheduled_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_create_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_scheduled_task_request_type** | [**CreateScheduledTaskRequestType**](CreateScheduledTaskRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled task created by the operation.  Refers instance of *ScheduledTask*.  |  -  |
**500** | ***InvalidName***: if the scheduled task name is empty or too long.  ***DuplicateName***: if a scheduled task with the name already exists.  ***InvalidArgument***: if the specification is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_manager_get_description**
> ScheduledTaskDescription scheduled_task_manager_get_description(mo_id)

Static descriptive strings used in scheduled tasks. 

Static descriptive strings used in scheduled tasks.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.scheduled_task_description import ScheduledTaskDescription
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Static descriptive strings used in scheduled tasks. 
        api_response = api_instance.scheduled_task_manager_get_description(mo_id)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ScheduledTaskDescription**](ScheduledTaskDescription.md)

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

# **scheduled_task_manager_get_scheduled_task**
> List[ManagedObjectReference] scheduled_task_manager_get_scheduled_task(mo_id)

All available scheduled tasks. 

All available scheduled tasks.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # All available scheduled tasks. 
        api_response = api_instance.scheduled_task_manager_get_scheduled_task(mo_id)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_get_scheduled_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_get_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *ScheduledTask*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_manager_retrieve_entity_scheduled_task**
> List[ManagedObjectReference] scheduled_task_manager_retrieve_entity_scheduled_task(mo_id, retrieve_entity_scheduled_task_request_type)

Available scheduled tasks defined on the entity. 

Available scheduled tasks defined on the entity.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.retrieve_entity_scheduled_task_request_type import RetrieveEntityScheduledTaskRequestType
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_entity_scheduled_task_request_type = vmware_vi.RetrieveEntityScheduledTaskRequestType() # RetrieveEntityScheduledTaskRequestType | 

    try:
        # Available scheduled tasks defined on the entity. 
        api_response = api_instance.scheduled_task_manager_retrieve_entity_scheduled_task(mo_id, retrieve_entity_scheduled_task_request_type)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_retrieve_entity_scheduled_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_retrieve_entity_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_entity_scheduled_task_request_type** | [**RetrieveEntityScheduledTaskRequestType**](RetrieveEntityScheduledTaskRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled tasks.  Refers instances of *ScheduledTask*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_task_manager_retrieve_object_scheduled_task**
> List[ManagedObjectReference] scheduled_task_manager_retrieve_object_scheduled_task(mo_id, retrieve_object_scheduled_task_request_type)

Available scheduled tasks defined on the object. 

Available scheduled tasks defined on the object.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.retrieve_object_scheduled_task_request_type import RetrieveObjectScheduledTaskRequestType
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
    api_instance = vmware_vi.ScheduledTaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_object_scheduled_task_request_type = vmware_vi.RetrieveObjectScheduledTaskRequestType() # RetrieveObjectScheduledTaskRequestType | 

    try:
        # Available scheduled tasks defined on the object. 
        api_response = api_instance.scheduled_task_manager_retrieve_object_scheduled_task(mo_id, retrieve_object_scheduled_task_request_type)
        print("The response of ScheduledTaskManagerApi->scheduled_task_manager_retrieve_object_scheduled_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTaskManagerApi->scheduled_task_manager_retrieve_object_scheduled_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_object_scheduled_task_request_type** | [**RetrieveObjectScheduledTaskRequestType**](RetrieveObjectScheduledTaskRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled tasks.  Refers instances of *ScheduledTask*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

