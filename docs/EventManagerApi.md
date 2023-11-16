# vmware_vi.EventManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_manager_create_collector_for_events**](EventManagerApi.md#event_manager_create_collector_for_events) | **POST** /EventManager/{moId}/CreateCollectorForEvents | Creates an event history collector, which is a specialized history collector that provides Event objects. 
[**event_manager_get_description**](EventManagerApi.md#event_manager_get_description) | **GET** /EventManager/{moId}/description | Static descriptive strings used in events. 
[**event_manager_get_latest_event**](EventManagerApi.md#event_manager_get_latest_event) | **GET** /EventManager/{moId}/latestEvent | The latest event that happened on the VirtualCenter server. 
[**event_manager_get_max_collector**](EventManagerApi.md#event_manager_get_max_collector) | **GET** /EventManager/{moId}/maxCollector | For each client, the maximum number of event collectors that can exist simultaneously. 
[**event_manager_log_user_event**](EventManagerApi.md#event_manager_log_user_event) | **POST** /EventManager/{moId}/LogUserEvent | Logs a user defined event against a particular managed entity. 
[**event_manager_post_event**](EventManagerApi.md#event_manager_post_event) | **POST** /EventManager/{moId}/PostEvent | Posts the specified event, optionally associating it with a task. 
[**event_manager_query_events**](EventManagerApi.md#event_manager_query_events) | **POST** /EventManager/{moId}/QueryEvents | Returns the events in specified filter. 
[**event_manager_retrieve_argument_description**](EventManagerApi.md#event_manager_retrieve_argument_description) | **POST** /EventManager/{moId}/RetrieveArgumentDescription | Retrieves the argument meta-data for a given Event type 


# **event_manager_create_collector_for_events**
> ManagedObjectReference event_manager_create_collector_for_events(mo_id, create_collector_for_events_request_type)

Creates an event history collector, which is a specialized history collector that provides Event objects. 

Creates an event history collector, which is a specialized history collector that provides Event objects.  Event collectors do not persist beyond the current client session.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_collector_for_events_request_type import CreateCollectorForEventsRequestType
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_collector_for_events_request_type = vmware_vi.CreateCollectorForEventsRequestType() # CreateCollectorForEventsRequestType | 

    try:
        # Creates an event history collector, which is a specialized history collector that provides Event objects. 
        api_response = api_instance.event_manager_create_collector_for_events(mo_id, create_collector_for_events_request_type)
        print("The response of EventManagerApi->event_manager_create_collector_for_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_create_collector_for_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_collector_for_events_request_type** | [**CreateCollectorForEventsRequestType**](CreateCollectorForEventsRequestType.md)|  | 

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
**200** | The event collector based on the filter.  Refers instance of *EventHistoryCollector*.  |  -  |
**500** | ***InvalidArgument***: if the filter is null or if any of its fields is invalid, such as an invalid reference to a managed object, alarm, or scheduled task, or an invalid event type or event chain id, etc.  ***InvalidState***: if there are more than the maximum number of event collectors.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_manager_get_description**
> EventDescription event_manager_get_description(mo_id)

Static descriptive strings used in events. 

Static descriptive strings used in events.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event_description import EventDescription
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Static descriptive strings used in events. 
        api_response = api_instance.event_manager_get_description(mo_id)
        print("The response of EventManagerApi->event_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**EventDescription**](EventDescription.md)

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

# **event_manager_get_latest_event**
> Event event_manager_get_latest_event(mo_id)

The latest event that happened on the VirtualCenter server. 

The latest event that happened on the VirtualCenter server.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The latest event that happened on the VirtualCenter server. 
        api_response = api_instance.event_manager_get_latest_event(mo_id)
        print("The response of EventManagerApi->event_manager_get_latest_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_get_latest_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**Event**](Event.md)

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

# **event_manager_get_max_collector**
> int event_manager_get_max_collector(mo_id)

For each client, the maximum number of event collectors that can exist simultaneously. 

For each client, the maximum number of event collectors that can exist simultaneously.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # For each client, the maximum number of event collectors that can exist simultaneously. 
        api_response = api_instance.event_manager_get_max_collector(mo_id)
        print("The response of EventManagerApi->event_manager_get_max_collector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_get_max_collector: %s\n" % e)
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

# **event_manager_log_user_event**
> event_manager_log_user_event(mo_id, log_user_event_request_type)

Logs a user defined event against a particular managed entity. 

Logs a user defined event against a particular managed entity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.log_user_event_request_type import LogUserEventRequestType
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    log_user_event_request_type = vmware_vi.LogUserEventRequestType() # LogUserEventRequestType | 

    try:
        # Logs a user defined event against a particular managed entity. 
        api_instance.event_manager_log_user_event(mo_id, log_user_event_request_type)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_log_user_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **log_user_event_request_type** | [**LogUserEventRequestType**](LogUserEventRequestType.md)|  | 

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

# **event_manager_post_event**
> event_manager_post_event(mo_id, post_event_request_type)

Posts the specified event, optionally associating it with a task. 

Posts the specified event, optionally associating it with a task.  The event being posted should have the following info in it: - The *ManagedEntity* on which the event is being posted should   be set in the appropriate *EntityEventArgument* field of the base   *Event* class. It is OK to not set any entity, in which case the   event is treated as an event about the system. - Some Event fields (*Event.key*, *Event.chainId*,   *Event.createdTime*) are mandatory because of the nature of   the structure, but any caller-supplied values will be overwritten by   the system.    If the event being posted is to be associated with an existing *Task*, the appropriate *TaskInfo* needs to be passed in. This task can either be one returned from a vSphere API operation or an extension task created by calling *TaskManager.CreateTask*.  ***Since:*** VI API 2.5  ***Required privileges:*** Global.LogEvent 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.post_event_request_type import PostEventRequestType
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    post_event_request_type = vmware_vi.PostEventRequestType() # PostEventRequestType | 

    try:
        # Posts the specified event, optionally associating it with a task. 
        api_instance.event_manager_post_event(mo_id, post_event_request_type)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_post_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **post_event_request_type** | [**PostEventRequestType**](PostEventRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if - an invalid reference to a managed object is passed in to one of the   *EntityEventArgument* fields - an invalid severity value is passed in an *EventEx*.    ***InvalidEvent***: no longer thrown by this API  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_manager_query_events**
> List[Event] event_manager_query_events(mo_id, query_events_request_type)

Returns the events in specified filter. 

Returns the events in specified filter.  Returns empty array when there are not any events qualified.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
from vmware_vi.models.query_events_request_type import QueryEventsRequestType
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_events_request_type = vmware_vi.QueryEventsRequestType() # QueryEventsRequestType | 

    try:
        # Returns the events in specified filter. 
        api_response = api_instance.event_manager_query_events(mo_id, query_events_request_type)
        print("The response of EventManagerApi->event_manager_query_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_query_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_events_request_type** | [**QueryEventsRequestType**](QueryEventsRequestType.md)|  | 

### Return type

[**List[Event]**](Event.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The events matching the filter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_manager_retrieve_argument_description**
> List[EventArgDesc] event_manager_retrieve_argument_description(mo_id, retrieve_argument_description_request_type)

Retrieves the argument meta-data for a given Event type 

Retrieves the argument meta-data for a given Event type  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event_arg_desc import EventArgDesc
from vmware_vi.models.retrieve_argument_description_request_type import RetrieveArgumentDescriptionRequestType
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
    api_instance = vmware_vi.EventManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_argument_description_request_type = vmware_vi.RetrieveArgumentDescriptionRequestType() # RetrieveArgumentDescriptionRequestType | 

    try:
        # Retrieves the argument meta-data for a given Event type 
        api_response = api_instance.event_manager_retrieve_argument_description(mo_id, retrieve_argument_description_request_type)
        print("The response of EventManagerApi->event_manager_retrieve_argument_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->event_manager_retrieve_argument_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_argument_description_request_type** | [**RetrieveArgumentDescriptionRequestType**](RetrieveArgumentDescriptionRequestType.md)|  | 

### Return type

[**List[EventArgDesc]**](EventArgDesc.md)

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

