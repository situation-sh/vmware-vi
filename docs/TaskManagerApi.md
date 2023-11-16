# vmware_vi.TaskManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_manager_create_collector_for_tasks**](TaskManagerApi.md#task_manager_create_collector_for_tasks) | **POST** /TaskManager/{moId}/CreateCollectorForTasks | Creates a *TaskHistoryCollector*, a specialized *HistoryCollector* that gathers *TaskInfo* data objects. 
[**task_manager_create_task**](TaskManagerApi.md#task_manager_create_task) | **POST** /TaskManager/{moId}/CreateTask | Creates a new *Task*, specifying the object with which the *Task* is associated, the type of task, and whether the task is cancelable. 
[**task_manager_get_description**](TaskManagerApi.md#task_manager_get_description) | **GET** /TaskManager/{moId}/description | Locale-specific, static strings that describe *Task* information to users. 
[**task_manager_get_max_collector**](TaskManagerApi.md#task_manager_get_max_collector) | **GET** /TaskManager/{moId}/maxCollector | Maximum number of *TaskHistoryCollector* data objects that can exist concurrently, per client. 
[**task_manager_get_recent_task**](TaskManagerApi.md#task_manager_get_recent_task) | **GET** /TaskManager/{moId}/recentTask | A list of *Task* managed objects that completed recently, that are currently running, or that are queued to run. 


# **task_manager_create_collector_for_tasks**
> ManagedObjectReference task_manager_create_collector_for_tasks(mo_id, create_collector_for_tasks_request_type)

Creates a *TaskHistoryCollector*, a specialized *HistoryCollector* that gathers *TaskInfo* data objects. 

Creates a *TaskHistoryCollector*, a specialized *HistoryCollector* that gathers *TaskInfo* data objects.  A *TaskHistoryCollector* does not persist beyond the current client session.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_collector_for_tasks_request_type import CreateCollectorForTasksRequestType
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
    api_instance = vmware_vi.TaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_collector_for_tasks_request_type = vmware_vi.CreateCollectorForTasksRequestType() # CreateCollectorForTasksRequestType | 

    try:
        # Creates a *TaskHistoryCollector*, a specialized *HistoryCollector* that gathers *TaskInfo* data objects. 
        api_response = api_instance.task_manager_create_collector_for_tasks(mo_id, create_collector_for_tasks_request_type)
        print("The response of TaskManagerApi->task_manager_create_collector_for_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->task_manager_create_collector_for_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_collector_for_tasks_request_type** | [**CreateCollectorForTasksRequestType**](CreateCollectorForTasksRequestType.md)|  | 

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
**200** | The task collector based on the filter.  Refers instance of *TaskHistoryCollector*.  |  -  |
**500** | ***InvalidArgument***: if the filter is null or unknown.  ***InvalidState***: if there are more than the maximum number of task collectors.  ***NotSupported***: if called directly on a host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_manager_create_task**
> TaskInfo task_manager_create_task(mo_id, create_task_request_type)

Creates a new *Task*, specifying the object with which the *Task* is associated, the type of task, and whether the task is cancelable. 

Creates a new *Task*, specifying the object with which the *Task* is associated, the type of task, and whether the task is cancelable.  Use this operation in conjunction with the *ExtensionManager*.  ***Since:*** VI API 2.5  ***Required privileges:*** Task.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_task_request_type import CreateTaskRequestType
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
    api_instance = vmware_vi.TaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_task_request_type = vmware_vi.CreateTaskRequestType() # CreateTaskRequestType | 

    try:
        # Creates a new *Task*, specifying the object with which the *Task* is associated, the type of task, and whether the task is cancelable. 
        api_response = api_instance.task_manager_create_task(mo_id, create_task_request_type)
        print("The response of TaskManagerApi->task_manager_create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->task_manager_create_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_task_request_type** | [**CreateTaskRequestType**](CreateTaskRequestType.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | *TaskInfo* data object describing the new task  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_manager_get_description**
> TaskDescription task_manager_get_description(mo_id)

Locale-specific, static strings that describe *Task* information to users. 

Locale-specific, static strings that describe *Task* information to users.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.task_description import TaskDescription
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
    api_instance = vmware_vi.TaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Locale-specific, static strings that describe *Task* information to users. 
        api_response = api_instance.task_manager_get_description(mo_id)
        print("The response of TaskManagerApi->task_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->task_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**TaskDescription**](TaskDescription.md)

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

# **task_manager_get_max_collector**
> int task_manager_get_max_collector(mo_id)

Maximum number of *TaskHistoryCollector* data objects that can exist concurrently, per client. 

Maximum number of *TaskHistoryCollector* data objects that can exist concurrently, per client.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.TaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Maximum number of *TaskHistoryCollector* data objects that can exist concurrently, per client. 
        api_response = api_instance.task_manager_get_max_collector(mo_id)
        print("The response of TaskManagerApi->task_manager_get_max_collector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->task_manager_get_max_collector: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**int**

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

# **task_manager_get_recent_task**
> List[ManagedObjectReference] task_manager_get_recent_task(mo_id)

A list of *Task* managed objects that completed recently, that are currently running, or that are queued to run. 

A list of *Task* managed objects that completed recently, that are currently running, or that are queued to run.  The list contains only *Task* objects that the client has permission to access, which is determined by having permission to access the *Task* object's managed *entity*.  The completed *Task* objects by default include only *Task* objects that completed within the past 10 minutes. When connected to vCenter Server, there is an additional default limitation that each of the completed *Task* objects in this list is one of the last 200 completed *Task* objects.  This property should not be used for tracking *Task* completion. Generally, a *ListView* is a better way to monitor a specific set of *Task* objects. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.TaskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A list of *Task* managed objects that completed recently, that are currently running, or that are queued to run. 
        api_response = api_instance.task_manager_get_recent_task(mo_id)
        print("The response of TaskManagerApi->task_manager_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskManagerApi->task_manager_get_recent_task: %s\n" % e)
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
**200** | Refers instances of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

