# vmware_vi.PropertyCollectorApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**property_collector_cancel_retrieve_properties_ex**](PropertyCollectorApi.md#property_collector_cancel_retrieve_properties_ex) | **POST** /PropertyCollector/{moId}/CancelRetrievePropertiesEx | Discards remaining results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 
[**property_collector_cancel_wait_for_updates**](PropertyCollectorApi.md#property_collector_cancel_wait_for_updates) | **POST** /PropertyCollector/{moId}/CancelWaitForUpdates | Attempts to cancel outstanding calls to *PropertyCollector.WaitForUpdates* or *PropertyCollector.WaitForUpdatesEx* in the current session. 
[**property_collector_check_for_updates**](PropertyCollectorApi.md#property_collector_check_for_updates) | **POST** /PropertyCollector/{moId}/CheckForUpdates | Checks for updates on properties specified by the union of all current filters. 
[**property_collector_continue_retrieve_properties_ex**](PropertyCollectorApi.md#property_collector_continue_retrieve_properties_ex) | **POST** /PropertyCollector/{moId}/ContinueRetrievePropertiesEx | Retrieves additional results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 
[**property_collector_create_filter**](PropertyCollectorApi.md#property_collector_create_filter) | **POST** /PropertyCollector/{moId}/CreateFilter | Creates a new filter for the given set of managed objects. 
[**property_collector_create_property_collector**](PropertyCollectorApi.md#property_collector_create_property_collector) | **POST** /PropertyCollector/{moId}/CreatePropertyCollector | Creates a new session-specific *PropertyCollector* that can be used to retrieve property updates independent of any other *PropertyCollector*. 
[**property_collector_destroy_property_collector**](PropertyCollectorApi.md#property_collector_destroy_property_collector) | **POST** /PropertyCollector/{moId}/DestroyPropertyCollector | Destroys this *PropertyCollector*. 
[**property_collector_get_filter**](PropertyCollectorApi.md#property_collector_get_filter) | **GET** /PropertyCollector/{moId}/filter | The filters that this *PropertyCollector* uses to determine the list of properties for which it detects incremental changes. 
[**property_collector_retrieve_properties**](PropertyCollectorApi.md#property_collector_retrieve_properties) | **POST** /PropertyCollector/{moId}/RetrieveProperties | Retrieves the specified properties of the specified managed objects. 
[**property_collector_retrieve_properties_ex**](PropertyCollectorApi.md#property_collector_retrieve_properties_ex) | **POST** /PropertyCollector/{moId}/RetrievePropertiesEx | Retrieves the specified properties of the specified managed objects. 
[**property_collector_wait_for_updates**](PropertyCollectorApi.md#property_collector_wait_for_updates) | **POST** /PropertyCollector/{moId}/WaitForUpdates | Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates. 
[**property_collector_wait_for_updates_ex**](PropertyCollectorApi.md#property_collector_wait_for_updates_ex) | **POST** /PropertyCollector/{moId}/WaitForUpdatesEx | Calculate the set of updates for each existing filter in the session. 


# **property_collector_cancel_retrieve_properties_ex**
> property_collector_cancel_retrieve_properties_ex(mo_id, cancel_retrieve_properties_ex_request_type)

Discards remaining results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 

Discards remaining results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cancel_retrieve_properties_ex_request_type import CancelRetrievePropertiesExRequestType
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cancel_retrieve_properties_ex_request_type = vmware_vi.CancelRetrievePropertiesExRequestType() # CancelRetrievePropertiesExRequestType | 

    try:
        # Discards remaining results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 
        api_instance.property_collector_cancel_retrieve_properties_ex(mo_id, cancel_retrieve_properties_ex_request_type)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_cancel_retrieve_properties_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cancel_retrieve_properties_ex_request_type** | [**CancelRetrievePropertiesExRequestType**](CancelRetrievePropertiesExRequestType.md)|  | 

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
**500** | ***InvalidArgument***: If the token does not match the token from the previous *RetrieveResult* returned on the same session by the same *PropertyCollector*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_cancel_wait_for_updates**
> property_collector_cancel_wait_for_updates(mo_id)

Attempts to cancel outstanding calls to *PropertyCollector.WaitForUpdates* or *PropertyCollector.WaitForUpdatesEx* in the current session. 

Attempts to cancel outstanding calls to *PropertyCollector.WaitForUpdates* or *PropertyCollector.WaitForUpdatesEx* in the current session.  If an update calculation is in process this method has no effect. If an update calculation is not in process any waiting calls complete quickly and report a *RequestCanceled* fault.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Attempts to cancel outstanding calls to *PropertyCollector.WaitForUpdates* or *PropertyCollector.WaitForUpdatesEx* in the current session. 
        api_instance.property_collector_cancel_wait_for_updates(mo_id)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_cancel_wait_for_updates: %s\n" % e)
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

# **property_collector_check_for_updates**
> UpdateSet property_collector_check_for_updates(mo_id, check_for_updates_request_type)

Checks for updates on properties specified by the union of all current filters. 

Deprecated as of vSphere API 4.1, use *PropertyCollector.WaitForUpdatesEx* with a *WaitOptions.maxWaitSeconds* of 0.  Checks for updates on properties specified by the union of all current filters.  If no updates are pending, this method returns null.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_for_updates_request_type import CheckForUpdatesRequestType
from vmware_vi.models.update_set import UpdateSet
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_for_updates_request_type = vmware_vi.CheckForUpdatesRequestType() # CheckForUpdatesRequestType | 

    try:
        # Checks for updates on properties specified by the union of all current filters. 
        api_response = api_instance.property_collector_check_for_updates(mo_id, check_for_updates_request_type)
        print("The response of PropertyCollectorApi->property_collector_check_for_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_check_for_updates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_for_updates_request_type** | [**CheckForUpdatesRequestType**](CheckForUpdatesRequestType.md)|  | 

### Return type

[**UpdateSet**](UpdateSet.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes since the passed in data version. If no updates are pending, then this method returns null.  |  -  |
**500** | ***InvalidCollectorVersion***: if the data version does not meet the requirements above.  ***RequestCanceled***: if *PropertyCollector.CancelWaitForUpdates* has been called or the session was closed or the *PropertyCollector* was destroyed at some point after the call was received but before the update calculation was actually started  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_continue_retrieve_properties_ex**
> RetrieveResult property_collector_continue_retrieve_properties_ex(mo_id, continue_retrieve_properties_ex_request_type)

Retrieves additional results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 

Retrieves additional results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.continue_retrieve_properties_ex_request_type import ContinueRetrievePropertiesExRequestType
from vmware_vi.models.retrieve_result import RetrieveResult
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    continue_retrieve_properties_ex_request_type = vmware_vi.ContinueRetrievePropertiesExRequestType() # ContinueRetrievePropertiesExRequestType | 

    try:
        # Retrieves additional results from a retrieval started by *PropertyCollector.RetrievePropertiesEx* on the same session on the same *PropertyCollector*. 
        api_response = api_instance.property_collector_continue_retrieve_properties_ex(mo_id, continue_retrieve_properties_ex_request_type)
        print("The response of PropertyCollectorApi->property_collector_continue_retrieve_properties_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_continue_retrieve_properties_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **continue_retrieve_properties_ex_request_type** | [**ContinueRetrievePropertiesExRequestType**](ContinueRetrievePropertiesExRequestType.md)|  | 

### Return type

[**RetrieveResult**](RetrieveResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | retrieved objects.  |  -  |
**500** | ***InvalidArgument***: If the token does not match the token from the previous *RetrieveResult* returned on the same session by the same *PropertyCollector*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_create_filter**
> ManagedObjectReference property_collector_create_filter(mo_id, create_filter_request_type)

Creates a new filter for the given set of managed objects. 

Creates a new filter for the given set of managed objects.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_filter_request_type import CreateFilterRequestType
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_filter_request_type = vmware_vi.CreateFilterRequestType() # CreateFilterRequestType | 

    try:
        # Creates a new filter for the given set of managed objects. 
        api_response = api_instance.property_collector_create_filter(mo_id, create_filter_request_type)
        print("The response of PropertyCollectorApi->property_collector_create_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_create_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_filter_request_type** | [**CreateFilterRequestType**](CreateFilterRequestType.md)|  | 

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
**200** | A reference to the new filter.  Refers instance of *PropertyFilter*.  |  -  |
**500** | ***InvalidArgument***: if any of the following is true: - \&quot;spec\&quot; is empty. - \&quot;spec\&quot; contains a selection with properties not defined on its   type.    ***InvalidProperty***: if \&quot;spec\&quot; has a property that is not defined on one of the objects.  ***InvalidType***: if \&quot;spec\&quot; contains, directly or indirectly, a type name that does not refer to a known type.  ***ManagedObjectNotFound***: See *PropertyFilterSpec.reportMissingObjectsInResults*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_create_property_collector**
> ManagedObjectReference property_collector_create_property_collector(mo_id)

Creates a new session-specific *PropertyCollector* that can be used to retrieve property updates independent of any other *PropertyCollector*. 

Creates a new session-specific *PropertyCollector* that can be used to retrieve property updates independent of any other *PropertyCollector*.  The newly created *PropertyCollector* is not tied to the creating *PropertyCollector* in any way and exists until it is destroyed by a call to *PropertyCollector.DestroyPropertyCollector* or until the session on which the PropertyCollector was created is closed. This is in contrast to the default *PropertyCollector*, which always exists, but still has session-specific data such as filters and unfinished update calculations that are discarded when the associated session is closed.  A new *PropertyCollector* can be useful when multiple modules or even multiple clients that share the same session need to create their own *PropertyFilter* objects and process updates independently. They may also be useful to allow important updates to be seen on one *PropertyCollector* while a large update is being calculated on another. The underlying issue that this addresses is that any call to *PropertyCollector.WaitForUpdates*, *PropertyCollector.CheckForUpdates*, or *PropertyCollector.WaitForUpdatesEx* does updates on all the filters created on a given *PropertyCollector* on a given session.  A more subtle use of multiple *PropertyCollector* objects is implied by the fact that the returned version value for the various updates calculations is strongly ordered. The only way this can make sense is that two different versions calculated on the same *PropertyCollector* on the same session cannot ever be created in parallel. This means that multiple calls to *PropertyCollector.WaitForUpdates*, *PropertyCollector.CheckForUpdates*, or *PropertyCollector.WaitForUpdatesEx* made to the same *PropertyCollector* on the same session on different threads of the same client, or even on different clients that share the same session are still handled on the server serially. Use of different *PropertyCollector* instances allows the server to handle these calculations in parallel.  Typically a service that supports the *PropertyCollector* managed object type will automatically create a default *PropertyCollector* and provide some way to obtain a reference to this *PropertyCollector*. If not, it will have to provide some service-specific way to create the a *PropertyCollector*.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Creates a new session-specific *PropertyCollector* that can be used to retrieve property updates independent of any other *PropertyCollector*. 
        api_response = api_instance.property_collector_create_property_collector(mo_id)
        print("The response of PropertyCollectorApi->property_collector_create_property_collector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_create_property_collector: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A reference to the new *PropertyCollector*.  Refers instance of *PropertyCollector*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_destroy_property_collector**
> property_collector_destroy_property_collector(mo_id)

Destroys this *PropertyCollector*. 

Destroys this *PropertyCollector*.  A *PropertyCollector* that was created by *PropertyCollector.CreatePropertyCollector* is automatically destroyed when the session on which it was created is closed. This method can be used to destroy them explicitly.  An automatically created *PropertyCollector* provided by a service is not session specific and may not be destroyed.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this *PropertyCollector*. 
        api_instance.property_collector_destroy_property_collector(mo_id)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_destroy_property_collector: %s\n" % e)
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

# **property_collector_get_filter**
> List[ManagedObjectReference] property_collector_get_filter(mo_id)

The filters that this *PropertyCollector* uses to determine the list of properties for which it detects incremental changes. 

The filters that this *PropertyCollector* uses to determine the list of properties for which it detects incremental changes.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The filters that this *PropertyCollector* uses to determine the list of properties for which it detects incremental changes. 
        api_response = api_instance.property_collector_get_filter(mo_id)
        print("The response of PropertyCollectorApi->property_collector_get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_get_filter: %s\n" % e)
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
**200** | Refers instances of *PropertyFilter*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_retrieve_properties**
> List[ObjectContent] property_collector_retrieve_properties(mo_id, retrieve_properties_request_type)

Retrieves the specified properties of the specified managed objects. 

Deprecated as of vSphere API 4.1, use *PropertyCollector.RetrievePropertiesEx*.  Retrieves the specified properties of the specified managed objects.  This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.  The filter creation step can throw all of the same faults as *PropertyCollector.CreateFilter*.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.object_content import ObjectContent
from vmware_vi.models.retrieve_properties_request_type import RetrievePropertiesRequestType
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_properties_request_type = vmware_vi.RetrievePropertiesRequestType() # RetrievePropertiesRequestType | 

    try:
        # Retrieves the specified properties of the specified managed objects. 
        api_response = api_instance.property_collector_retrieve_properties(mo_id, retrieve_properties_request_type)
        print("The response of PropertyCollectorApi->property_collector_retrieve_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_retrieve_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_properties_request_type** | [**RetrievePropertiesRequestType**](RetrievePropertiesRequestType.md)|  | 

### Return type

[**List[ObjectContent]**](ObjectContent.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data contents of the specified objects.  |  -  |
**500** | ***InvalidArgument***: See *PropertyCollector.CreateFilter*  ***InvalidProperty***: See *PropertyCollector.CreateFilter*  ***InvalidType***: See *PropertyCollector.CreateFilter*  ***ManagedObjectNotFound***: See *PropertyCollector.CreateFilter*  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_retrieve_properties_ex**
> RetrieveResult property_collector_retrieve_properties_ex(mo_id, retrieve_properties_ex_request_type)

Retrieves the specified properties of the specified managed objects. 

Retrieves the specified properties of the specified managed objects.  This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.  The filter creation step can throw all of the same faults as *PropertyCollector.CreateFilter*.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_properties_ex_request_type import RetrievePropertiesExRequestType
from vmware_vi.models.retrieve_result import RetrieveResult
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_properties_ex_request_type = vmware_vi.RetrievePropertiesExRequestType() # RetrievePropertiesExRequestType | 

    try:
        # Retrieves the specified properties of the specified managed objects. 
        api_response = api_instance.property_collector_retrieve_properties_ex(mo_id, retrieve_properties_ex_request_type)
        print("The response of PropertyCollectorApi->property_collector_retrieve_properties_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_retrieve_properties_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_properties_ex_request_type** | [**RetrievePropertiesExRequestType**](RetrievePropertiesExRequestType.md)|  | 

### Return type

[**RetrieveResult**](RetrieveResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | retrieved objects or null if there are no matching objects.  |  -  |
**500** | ***InvalidArgument***: if any of the following is true: See *PropertyCollector.CreateFilter*  ***InvalidProperty***: See *PropertyCollector.CreateFilter*  ***InvalidType***: See *PropertyCollector.CreateFilter*  ***ManagedObjectNotFound***: See *PropertyCollector.CreateFilter*  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_wait_for_updates**
> UpdateSet property_collector_wait_for_updates(mo_id, wait_for_updates_request_type)

Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates. 

Deprecated as of vSphere API 4.1, use *PropertyCollector.WaitForUpdatesEx*.  Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_set import UpdateSet
from vmware_vi.models.wait_for_updates_request_type import WaitForUpdatesRequestType
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    wait_for_updates_request_type = vmware_vi.WaitForUpdatesRequestType() # WaitForUpdatesRequestType | 

    try:
        # Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates. 
        api_response = api_instance.property_collector_wait_for_updates(mo_id, wait_for_updates_request_type)
        print("The response of PropertyCollectorApi->property_collector_wait_for_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_wait_for_updates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **wait_for_updates_request_type** | [**WaitForUpdatesRequestType**](WaitForUpdatesRequestType.md)|  | 

### Return type

[**UpdateSet**](UpdateSet.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes since the passed in data version.  |  -  |
**500** | ***InvalidCollectorVersion***: if the data version does not meet the requirements above.  ***RequestCanceled***: if *PropertyCollector.CancelWaitForUpdates* has been called or the session was closed or the *PropertyCollector* was destroyed at some point after the call was received  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_collector_wait_for_updates_ex**
> UpdateSet property_collector_wait_for_updates_ex(mo_id, wait_for_updates_ex_request_type)

Calculate the set of updates for each existing filter in the session. 

Calculate the set of updates for each existing filter in the session.  *PropertyCollector.WaitForUpdatesEx* may return only partial update calculations. See *UpdateSet.truncated* for a more detailed explanation. *PropertyCollector.WaitForUpdatesEx* may also return null after a timeout, either as requested by *WaitOptions.maxWaitSeconds* or due to *PropertyCollector* policy.  If an application uses waitForUpdatesEx it is strongly recommended that it not make concurrent calls to *PropertyCollector.WaitForUpdates*, *PropertyCollector.CheckForUpdates*, or *PropertyCollector.WaitForUpdatesEx* in the same session. Concurrent calls may cause suspended change calculations to be discarded.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_set import UpdateSet
from vmware_vi.models.wait_for_updates_ex_request_type import WaitForUpdatesExRequestType
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
    api_instance = vmware_vi.PropertyCollectorApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    wait_for_updates_ex_request_type = vmware_vi.WaitForUpdatesExRequestType() # WaitForUpdatesExRequestType | 

    try:
        # Calculate the set of updates for each existing filter in the session. 
        api_response = api_instance.property_collector_wait_for_updates_ex(mo_id, wait_for_updates_ex_request_type)
        print("The response of PropertyCollectorApi->property_collector_wait_for_updates_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyCollectorApi->property_collector_wait_for_updates_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **wait_for_updates_ex_request_type** | [**WaitForUpdatesExRequestType**](WaitForUpdatesExRequestType.md)|  | 

### Return type

[**UpdateSet**](UpdateSet.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes since the passed in version or null if there are no changes.  |  -  |
**500** | ***InvalidCollectorVersion***: if the data version does not meet the requirements above.  ***RequestCanceled***: if *PropertyCollector.CancelWaitForUpdates* has been called or the session was closed or the *PropertyCollector* was destroyed at some point after the call was received  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

