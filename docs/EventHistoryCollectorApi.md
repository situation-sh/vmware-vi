# vmware_vi.EventHistoryCollectorApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_history_collector_destroy_collector**](EventHistoryCollectorApi.md#event_history_collector_destroy_collector) | **POST** /EventHistoryCollector/{moId}/DestroyCollector | Destroys this collector. 
[**event_history_collector_get_filter**](EventHistoryCollectorApi.md#event_history_collector_get_filter) | **GET** /EventHistoryCollector/{moId}/filter | The filter used to create this collector. 
[**event_history_collector_get_latest_page**](EventHistoryCollectorApi.md#event_history_collector_get_latest_page) | **GET** /EventHistoryCollector/{moId}/latestPage | The items in the &#39;viewable latest page&#39;. 
[**event_history_collector_read_next_events**](EventHistoryCollectorApi.md#event_history_collector_read_next_events) | **POST** /EventHistoryCollector/{moId}/ReadNextEvents | Reads the &#39;scrollable view&#39; from the current position. 
[**event_history_collector_read_previous_events**](EventHistoryCollectorApi.md#event_history_collector_read_previous_events) | **POST** /EventHistoryCollector/{moId}/ReadPreviousEvents | Reads the &#39;scrollable view&#39; from the current position. 
[**event_history_collector_reset_collector**](EventHistoryCollectorApi.md#event_history_collector_reset_collector) | **POST** /EventHistoryCollector/{moId}/ResetCollector | Moves the \&quot;scrollable view\&quot; to the item immediately preceding the \&quot;viewable latest page\&quot;. 
[**event_history_collector_rewind_collector**](EventHistoryCollectorApi.md#event_history_collector_rewind_collector) | **POST** /EventHistoryCollector/{moId}/RewindCollector | Moves the \&quot;scrollable view\&quot; to the oldest item. 
[**event_history_collector_set_collector_page_size**](EventHistoryCollectorApi.md#event_history_collector_set_collector_page_size) | **POST** /EventHistoryCollector/{moId}/SetCollectorPageSize | Sets the \&quot;viewable latest page\&quot; size to contain at most the number of items specified by the maxCount parameter). 


# **event_history_collector_destroy_collector**
> event_history_collector_destroy_collector(mo_id)

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this collector. 
        api_instance.event_history_collector_destroy_collector(mo_id)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_destroy_collector: %s\n" % e)
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

# **event_history_collector_get_filter**
> Any event_history_collector_get_filter(mo_id)

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The filter used to create this collector. 
        api_response = api_instance.event_history_collector_get_filter(mo_id)
        print("The response of EventHistoryCollectorApi->event_history_collector_get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_get_filter: %s\n" % e)
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

# **event_history_collector_get_latest_page**
> List[Event] event_history_collector_get_latest_page(mo_id)

The items in the 'viewable latest page'. 

The items in the 'viewable latest page'.  As new events that match the collector's *EventFilterSpec* are created, they are added to this page, and the oldest events are removed from the collector to keep the size of the page to that allowed by *HistoryCollector.SetCollectorPageSize*.  The \"oldest event\" is the one with the smallest key (event ID). The events in the returned page are unordered. 

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The items in the 'viewable latest page'. 
        api_response = api_instance.event_history_collector_get_latest_page(mo_id)
        print("The response of EventHistoryCollectorApi->event_history_collector_get_latest_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_get_latest_page: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Event]**](Event.md)

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

# **event_history_collector_read_next_events**
> List[Event] event_history_collector_read_next_events(mo_id, read_next_events_request_type)

Reads the 'scrollable view' from the current position. 

Reads the 'scrollable view' from the current position.  The scrollable position is moved to the next newer page after the read. No item is returned when the end of the collector is reached. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
from vmware_vi.models.read_next_events_request_type import ReadNextEventsRequestType
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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    read_next_events_request_type = vmware_vi.ReadNextEventsRequestType() # ReadNextEventsRequestType | 

    try:
        # Reads the 'scrollable view' from the current position. 
        api_response = api_instance.event_history_collector_read_next_events(mo_id, read_next_events_request_type)
        print("The response of EventHistoryCollectorApi->event_history_collector_read_next_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_read_next_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **read_next_events_request_type** | [**ReadNextEventsRequestType**](ReadNextEventsRequestType.md)|  | 

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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_history_collector_read_previous_events**
> List[Event] event_history_collector_read_previous_events(mo_id, read_previous_events_request_type)

Reads the 'scrollable view' from the current position. 

Reads the 'scrollable view' from the current position.  The scrollable position is moved to the next older page after the read. No item is returned when the head of the collector is reached. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
from vmware_vi.models.read_previous_events_request_type import ReadPreviousEventsRequestType
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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    read_previous_events_request_type = vmware_vi.ReadPreviousEventsRequestType() # ReadPreviousEventsRequestType | 

    try:
        # Reads the 'scrollable view' from the current position. 
        api_response = api_instance.event_history_collector_read_previous_events(mo_id, read_previous_events_request_type)
        print("The response of EventHistoryCollectorApi->event_history_collector_read_previous_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_read_previous_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **read_previous_events_request_type** | [**ReadPreviousEventsRequestType**](ReadPreviousEventsRequestType.md)|  | 

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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_history_collector_reset_collector**
> event_history_collector_reset_collector(mo_id)

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Moves the \"scrollable view\" to the item immediately preceding the \"viewable latest page\". 
        api_instance.event_history_collector_reset_collector(mo_id)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_reset_collector: %s\n" % e)
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

# **event_history_collector_rewind_collector**
> event_history_collector_rewind_collector(mo_id)

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Moves the \"scrollable view\" to the oldest item. 
        api_instance.event_history_collector_rewind_collector(mo_id)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_rewind_collector: %s\n" % e)
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

# **event_history_collector_set_collector_page_size**
> event_history_collector_set_collector_page_size(mo_id, set_collector_page_size_request_type)

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
    api_instance = vmware_vi.EventHistoryCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_collector_page_size_request_type = vmware_vi.SetCollectorPageSizeRequestType() # SetCollectorPageSizeRequestType | 

    try:
        # Sets the \"viewable latest page\" size to contain at most the number of items specified by the maxCount parameter). 
        api_instance.event_history_collector_set_collector_page_size(mo_id, set_collector_page_size_request_type)
    except Exception as e:
        print("Exception when calling EventHistoryCollectorApi->event_history_collector_set_collector_page_size: %s\n" % e)
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

