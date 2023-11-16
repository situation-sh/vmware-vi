# vmware_vi.TaskHistoryCollectorApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_history_collector_destroy_collector**](TaskHistoryCollectorApi.md#task_history_collector_destroy_collector) | **POST** /TaskHistoryCollector/{moId}/DestroyCollector | Destroys this collector. 
[**task_history_collector_get_filter**](TaskHistoryCollectorApi.md#task_history_collector_get_filter) | **GET** /TaskHistoryCollector/{moId}/filter | The filter used to create this collector. 
[**task_history_collector_get_latest_page**](TaskHistoryCollectorApi.md#task_history_collector_get_latest_page) | **GET** /TaskHistoryCollector/{moId}/latestPage | The items in the &#39;viewable latest page&#39;. 
[**task_history_collector_read_next_tasks**](TaskHistoryCollectorApi.md#task_history_collector_read_next_tasks) | **POST** /TaskHistoryCollector/{moId}/ReadNextTasks | Reads the &#39;scrollable view&#39; from the current position. 
[**task_history_collector_read_previous_tasks**](TaskHistoryCollectorApi.md#task_history_collector_read_previous_tasks) | **POST** /TaskHistoryCollector/{moId}/ReadPreviousTasks | Reads the &#39;scrollable view&#39; from the current position. 
[**task_history_collector_reset_collector**](TaskHistoryCollectorApi.md#task_history_collector_reset_collector) | **POST** /TaskHistoryCollector/{moId}/ResetCollector | Moves the \&quot;scrollable view\&quot; to the item immediately preceding the \&quot;viewable latest page\&quot;. 
[**task_history_collector_rewind_collector**](TaskHistoryCollectorApi.md#task_history_collector_rewind_collector) | **POST** /TaskHistoryCollector/{moId}/RewindCollector | Moves the \&quot;scrollable view\&quot; to the oldest item. 
[**task_history_collector_set_collector_page_size**](TaskHistoryCollectorApi.md#task_history_collector_set_collector_page_size) | **POST** /TaskHistoryCollector/{moId}/SetCollectorPageSize | Sets the \&quot;viewable latest page\&quot; size to contain at most the number of items specified by the maxCount parameter). 


# **task_history_collector_destroy_collector**
> task_history_collector_destroy_collector(mo_id)

Destroys this collector. 

Destroys this collector. 

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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this collector. 
        api_instance.task_history_collector_destroy_collector(mo_id)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_destroy_collector: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_history_collector_get_filter**
> Any task_history_collector_get_filter(mo_id)

The filter used to create this collector. 

The filter used to create this collector.  The type of the returned filter is determined by the managed object for which the collector is created. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.any import Any
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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The filter used to create this collector. 
        api_response = api_instance.task_history_collector_get_filter(mo_id)
        print("The response of TaskHistoryCollectorApi->task_history_collector_get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_get_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**Any**](Any.md)

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

# **task_history_collector_get_latest_page**
> List[TaskInfo] task_history_collector_get_latest_page(mo_id)

The items in the 'viewable latest page'. 

The items in the 'viewable latest page'.  As new tasks that match the collector's *TaskFilterSpec* are created, they are added to this page, and the oldest tasks are removed from the collector to keep the size of the page to that allowed by *HistoryCollector.SetCollectorPageSize*.  The \"oldest task\" is the one with the oldest creation time. The tasks in the returned page are unordered. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.task_info import TaskInfo
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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The items in the 'viewable latest page'. 
        api_response = api_instance.task_history_collector_get_latest_page(mo_id)
        print("The response of TaskHistoryCollectorApi->task_history_collector_get_latest_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_get_latest_page: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[TaskInfo]**](TaskInfo.md)

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

# **task_history_collector_read_next_tasks**
> List[TaskInfo] task_history_collector_read_next_tasks(mo_id, read_next_tasks_request_type)

Reads the 'scrollable view' from the current position. 

Reads the 'scrollable view' from the current position.  The scrollable position is moved to the next newer page after the read. No item is returned when the end of the collector is reached. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.read_next_tasks_request_type import ReadNextTasksRequestType
from vmware_vi.models.task_info import TaskInfo
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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    read_next_tasks_request_type = vmware_vi.ReadNextTasksRequestType() # ReadNextTasksRequestType | 

    try:
        # Reads the 'scrollable view' from the current position. 
        api_response = api_instance.task_history_collector_read_next_tasks(mo_id, read_next_tasks_request_type)
        print("The response of TaskHistoryCollectorApi->task_history_collector_read_next_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_read_next_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **read_next_tasks_request_type** | [**ReadNextTasksRequestType**](ReadNextTasksRequestType.md)|  | 

### Return type

[**List[TaskInfo]**](TaskInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_history_collector_read_previous_tasks**
> List[TaskInfo] task_history_collector_read_previous_tasks(mo_id, read_previous_tasks_request_type)

Reads the 'scrollable view' from the current position. 

Reads the 'scrollable view' from the current position.  The scrollable position is then moved to the next older page after the read. No item is returned when the head of the collector is reached. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.read_previous_tasks_request_type import ReadPreviousTasksRequestType
from vmware_vi.models.task_info import TaskInfo
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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    read_previous_tasks_request_type = vmware_vi.ReadPreviousTasksRequestType() # ReadPreviousTasksRequestType | 

    try:
        # Reads the 'scrollable view' from the current position. 
        api_response = api_instance.task_history_collector_read_previous_tasks(mo_id, read_previous_tasks_request_type)
        print("The response of TaskHistoryCollectorApi->task_history_collector_read_previous_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_read_previous_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **read_previous_tasks_request_type** | [**ReadPreviousTasksRequestType**](ReadPreviousTasksRequestType.md)|  | 

### Return type

[**List[TaskInfo]**](TaskInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_history_collector_reset_collector**
> task_history_collector_reset_collector(mo_id)

Moves the \"scrollable view\" to the item immediately preceding the \"viewable latest page\". 

Moves the \"scrollable view\" to the item immediately preceding the \"viewable latest page\".  If you use \"readPrev\", *ReadPreviousTasks* or *ReadPreviousEvents*, all items are retrieved from the newest item to the oldest item. 

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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Moves the \"scrollable view\" to the item immediately preceding the \"viewable latest page\". 
        api_instance.task_history_collector_reset_collector(mo_id)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_reset_collector: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_history_collector_rewind_collector**
> task_history_collector_rewind_collector(mo_id)

Moves the \"scrollable view\" to the oldest item. 

Moves the \"scrollable view\" to the oldest item.  If you use *ReadNextTasks* or *ReadNextEvents*, all items are retrieved from the oldest item to the newest item. This is the default setting when the collector is created. 

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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Moves the \"scrollable view\" to the oldest item. 
        api_instance.task_history_collector_rewind_collector(mo_id)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_rewind_collector: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_history_collector_set_collector_page_size**
> task_history_collector_set_collector_page_size(mo_id, set_collector_page_size_request_type)

Sets the \"viewable latest page\" size to contain at most the number of items specified by the maxCount parameter). 

Sets the \"viewable latest page\" size to contain at most the number of items specified by the maxCount parameter). 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_collector_page_size_request_type import SetCollectorPageSizeRequestType
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
    api_instance = vmware_vi.TaskHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_collector_page_size_request_type = vmware_vi.SetCollectorPageSizeRequestType() # SetCollectorPageSizeRequestType | 

    try:
        # Sets the \"viewable latest page\" size to contain at most the number of items specified by the maxCount parameter). 
        api_instance.task_history_collector_set_collector_page_size(mo_id, set_collector_page_size_request_type)
    except Exception as e:
        print("Exception when calling TaskHistoryCollectorApi->task_history_collector_set_collector_page_size: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_collector_page_size_request_type** | [**SetCollectorPageSizeRequestType**](SetCollectorPageSizeRequestType.md)|  | 

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

