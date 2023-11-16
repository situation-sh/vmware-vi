# vmware_vi.HealthUpdateManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_update_manager_add_filter**](HealthUpdateManagerApi.md#health_update_manager_add_filter) | **POST** /HealthUpdateManager/{moId}/AddFilter | Adds health update filters. 
[**health_update_manager_add_filter_entities**](HealthUpdateManagerApi.md#health_update_manager_add_filter_entities) | **POST** /HealthUpdateManager/{moId}/AddFilterEntities | Add entities on which this filter is configured. 
[**health_update_manager_add_monitored_entities**](HealthUpdateManagerApi.md#health_update_manager_add_monitored_entities) | **POST** /HealthUpdateManager/{moId}/AddMonitoredEntities | The provider monitors additional managed entities. 
[**health_update_manager_has_monitored_entity**](HealthUpdateManagerApi.md#health_update_manager_has_monitored_entity) | **POST** /HealthUpdateManager/{moId}/HasMonitoredEntity | Check if the managed entity is monitored by the provider. 
[**health_update_manager_has_provider**](HealthUpdateManagerApi.md#health_update_manager_has_provider) | **POST** /HealthUpdateManager/{moId}/HasProvider | Verifies if the given provider is registered. 
[**health_update_manager_post_health_updates**](HealthUpdateManagerApi.md#health_update_manager_post_health_updates) | **POST** /HealthUpdateManager/{moId}/PostHealthUpdates | Report a change in health status. 
[**health_update_manager_query_filter_entities**](HealthUpdateManagerApi.md#health_update_manager_query_filter_entities) | **POST** /HealthUpdateManager/{moId}/QueryFilterEntities | Returns the list of entities on which this filter is configured. 
[**health_update_manager_query_filter_info_ids**](HealthUpdateManagerApi.md#health_update_manager_query_filter_info_ids) | **POST** /HealthUpdateManager/{moId}/QueryFilterInfoIds | Returns the list of HealthUpdateInfos configured for this filter. 
[**health_update_manager_query_filter_list**](HealthUpdateManagerApi.md#health_update_manager_query_filter_list) | **POST** /HealthUpdateManager/{moId}/QueryFilterList | Returns the list of filters. 
[**health_update_manager_query_filter_name**](HealthUpdateManagerApi.md#health_update_manager_query_filter_name) | **POST** /HealthUpdateManager/{moId}/QueryFilterName | Returns the filter name. 
[**health_update_manager_query_health_update_infos**](HealthUpdateManagerApi.md#health_update_manager_query_health_update_infos) | **POST** /HealthUpdateManager/{moId}/QueryHealthUpdateInfos | Returns the list of HealthUpdateInfo configured for the given provider. 
[**health_update_manager_query_health_updates**](HealthUpdateManagerApi.md#health_update_manager_query_health_updates) | **POST** /HealthUpdateManager/{moId}/QueryHealthUpdates | Returns the list of health updates reported by the given provider. 
[**health_update_manager_query_monitored_entities**](HealthUpdateManagerApi.md#health_update_manager_query_monitored_entities) | **POST** /HealthUpdateManager/{moId}/QueryMonitoredEntities | Returns the list of managed entities monitored by the given provider. 
[**health_update_manager_query_provider_list**](HealthUpdateManagerApi.md#health_update_manager_query_provider_list) | **POST** /HealthUpdateManager/{moId}/QueryProviderList | The providers. 
[**health_update_manager_query_provider_name**](HealthUpdateManagerApi.md#health_update_manager_query_provider_name) | **POST** /HealthUpdateManager/{moId}/QueryProviderName | Query the name of the provider. 
[**health_update_manager_query_unmonitored_hosts**](HealthUpdateManagerApi.md#health_update_manager_query_unmonitored_hosts) | **POST** /HealthUpdateManager/{moId}/QueryUnmonitoredHosts | The set of hosts that are in the cluster, but not monitored by the provider. 
[**health_update_manager_register_health_update_provider**](HealthUpdateManagerApi.md#health_update_manager_register_health_update_provider) | **POST** /HealthUpdateManager/{moId}/RegisterHealthUpdateProvider | Registers provider. 
[**health_update_manager_remove_filter**](HealthUpdateManagerApi.md#health_update_manager_remove_filter) | **POST** /HealthUpdateManager/{moId}/RemoveFilter | Removes the specified filter. 
[**health_update_manager_remove_filter_entities**](HealthUpdateManagerApi.md#health_update_manager_remove_filter_entities) | **POST** /HealthUpdateManager/{moId}/RemoveFilterEntities | Remove entities on which this filter is configured. 
[**health_update_manager_remove_monitored_entities**](HealthUpdateManagerApi.md#health_update_manager_remove_monitored_entities) | **POST** /HealthUpdateManager/{moId}/RemoveMonitoredEntities | The provider monitors fewer managed entities. 
[**health_update_manager_unregister_health_update_provider**](HealthUpdateManagerApi.md#health_update_manager_unregister_health_update_provider) | **POST** /HealthUpdateManager/{moId}/UnregisterHealthUpdateProvider | Unregisters the specified provider, if it exists. 


# **health_update_manager_add_filter**
> str health_update_manager_add_filter(mo_id, add_filter_request_type)

Adds health update filters. 

Adds health update filters.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_filter_request_type import AddFilterRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_filter_request_type = vmware_vi.AddFilterRequestType() # AddFilterRequestType | 

    try:
        # Adds health update filters. 
        api_response = api_instance.health_update_manager_add_filter(mo_id, add_filter_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_add_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_add_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_filter_request_type** | [**AddFilterRequestType**](AddFilterRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The filter identifier.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  ***InvalidArgument***: - If filter name exceeds the maximum length limit of 56 characters. \\- If a filter with this name already exists for this provider. \\- If infoIds list contains a HealthUpdateInfo id which is not associated with the specified provider. \\- If there are duplicate HealthUpdateInfo ids in the infoIds list.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_add_filter_entities**
> health_update_manager_add_filter_entities(mo_id, add_filter_entities_request_type)

Add entities on which this filter is configured. 

Add entities on which this filter is configured.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_filter_entities_request_type import AddFilterEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_filter_entities_request_type = vmware_vi.AddFilterEntitiesRequestType() # AddFilterEntitiesRequestType | 

    try:
        # Add entities on which this filter is configured. 
        api_instance.health_update_manager_add_filter_entities(mo_id, add_filter_entities_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_add_filter_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_filter_entities_request_type** | [**AddFilterEntitiesRequestType**](AddFilterEntitiesRequestType.md)|  | 

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
**500** | ***NotFound***: If no filter with this id is registered.  ***InvalidArgument***: - If any of the entities is already associated with the specified filter. \\- If there are duplicate entities in the given entities list. \\- If the entities list contains an entity of type other than HostSystem and ClusterComputeResource.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_add_monitored_entities**
> health_update_manager_add_monitored_entities(mo_id, add_monitored_entities_request_type)

The provider monitors additional managed entities. 

The provider monitors additional managed entities.  A particular managed entity can be monitored by multiple providers.  ***Since:*** vSphere API 6.5  ***Required privileges:*** HealthUpdateProvider.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_monitored_entities_request_type import AddMonitoredEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_monitored_entities_request_type = vmware_vi.AddMonitoredEntitiesRequestType() # AddMonitoredEntitiesRequestType | 

    try:
        # The provider monitors additional managed entities. 
        api_instance.health_update_manager_add_monitored_entities(mo_id, add_monitored_entities_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_add_monitored_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_monitored_entities_request_type** | [**AddMonitoredEntitiesRequestType**](AddMonitoredEntitiesRequestType.md)|  | 

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
**500** | ***NotFound***: If no provider with this id is registered.  ***NotSupported***: If the http session user does not match the user who registered the provider, or if the http session cannot be retrieved.  ***InvalidArgument***: - If any of the entities is not of type HostSystem. \\- If there are duplicate entities in the given entities list. \\- If any of the entities is already monitored by the specified provider.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_has_monitored_entity**
> bool health_update_manager_has_monitored_entity(mo_id, has_monitored_entity_request_type)

Check if the managed entity is monitored by the provider. 

Check if the managed entity is monitored by the provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.has_monitored_entity_request_type import HasMonitoredEntityRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    has_monitored_entity_request_type = vmware_vi.HasMonitoredEntityRequestType() # HasMonitoredEntityRequestType | 

    try:
        # Check if the managed entity is monitored by the provider. 
        api_response = api_instance.health_update_manager_has_monitored_entity(mo_id, has_monitored_entity_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_has_monitored_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_has_monitored_entity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **has_monitored_entity_request_type** | [**HasMonitoredEntityRequestType**](HasMonitoredEntityRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True iff the entity is monitored by this provider.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  ***InvalidArgument***: If the specified entity is not of type HostSystem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_has_provider**
> bool health_update_manager_has_provider(mo_id, has_provider_request_type)

Verifies if the given provider is registered. 

Verifies if the given provider is registered.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.has_provider_request_type import HasProviderRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    has_provider_request_type = vmware_vi.HasProviderRequestType() # HasProviderRequestType | 

    try:
        # Verifies if the given provider is registered. 
        api_response = api_instance.health_update_manager_has_provider(mo_id, has_provider_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_has_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_has_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **has_provider_request_type** | [**HasProviderRequestType**](HasProviderRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True iff the provider is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_post_health_updates**
> health_update_manager_post_health_updates(mo_id, post_health_updates_request_type)

Report a change in health status. 

Report a change in health status.  ***Since:*** vSphere API 6.5  ***Required privileges:*** HealthUpdateProvider.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.post_health_updates_request_type import PostHealthUpdatesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    post_health_updates_request_type = vmware_vi.PostHealthUpdatesRequestType() # PostHealthUpdatesRequestType | 

    try:
        # Report a change in health status. 
        api_instance.health_update_manager_post_health_updates(mo_id, post_health_updates_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_post_health_updates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **post_health_updates_request_type** | [**PostHealthUpdatesRequestType**](PostHealthUpdatesRequestType.md)|  | 

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
**500** | ***NotFound***: If no provider with this id is registered.  ***NotSupported***: If the http session user does not match the user who registered the provider, or if the http session cannot be retrieved.  ***InvalidArgument***: - If an unknown HealthUpdate id is given. \\- If updates list contains a HealthUpdate for a host which is not monitored by the specified provider. \\- If updates list contains multiple HealthUpdates with the same id. \\- If an existing HealthUpdate id is used in the given updates. \\- If there is a HealthUpdate with green status and non-empty remediation. \\- If there is a HealthUpdate with gray status.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_filter_entities**
> List[ManagedObjectReference] health_update_manager_query_filter_entities(mo_id, query_filter_entities_request_type)

Returns the list of entities on which this filter is configured. 

Returns the list of entities on which this filter is configured.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_filter_entities_request_type import QueryFilterEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_filter_entities_request_type = vmware_vi.QueryFilterEntitiesRequestType() # QueryFilterEntitiesRequestType | 

    try:
        # Returns the list of entities on which this filter is configured. 
        api_response = api_instance.health_update_manager_query_filter_entities(mo_id, query_filter_entities_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_filter_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_filter_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_filter_entities_request_type** | [**QueryFilterEntitiesRequestType**](QueryFilterEntitiesRequestType.md)|  | 

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
**200** | The list of managed entities.  Refers instances of *ManagedEntity*.  |  -  |
**500** | ***NotFound***: If no filter with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_filter_info_ids**
> List[str] health_update_manager_query_filter_info_ids(mo_id, query_filter_info_ids_request_type)

Returns the list of HealthUpdateInfos configured for this filter. 

Returns the list of HealthUpdateInfos configured for this filter.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_filter_info_ids_request_type import QueryFilterInfoIdsRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_filter_info_ids_request_type = vmware_vi.QueryFilterInfoIdsRequestType() # QueryFilterInfoIdsRequestType | 

    try:
        # Returns the list of HealthUpdateInfos configured for this filter. 
        api_response = api_instance.health_update_manager_query_filter_info_ids(mo_id, query_filter_info_ids_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_filter_info_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_filter_info_ids: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_filter_info_ids_request_type** | [**QueryFilterInfoIdsRequestType**](QueryFilterInfoIdsRequestType.md)|  | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of identifiers of the configured HealthUpdateInfos.  |  -  |
**500** | ***NotFound***: If no filter with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_filter_list**
> List[str] health_update_manager_query_filter_list(mo_id, query_filter_list_request_type)

Returns the list of filters. 

Returns the list of filters.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_filter_list_request_type import QueryFilterListRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_filter_list_request_type = vmware_vi.QueryFilterListRequestType() # QueryFilterListRequestType | 

    try:
        # Returns the list of filters. 
        api_response = api_instance.health_update_manager_query_filter_list(mo_id, query_filter_list_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_filter_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_filter_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_filter_list_request_type** | [**QueryFilterListRequestType**](QueryFilterListRequestType.md)|  | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of filters identifiers.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_filter_name**
> str health_update_manager_query_filter_name(mo_id, query_filter_name_request_type)

Returns the filter name. 

Returns the filter name.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_filter_name_request_type import QueryFilterNameRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_filter_name_request_type = vmware_vi.QueryFilterNameRequestType() # QueryFilterNameRequestType | 

    try:
        # Returns the filter name. 
        api_response = api_instance.health_update_manager_query_filter_name(mo_id, query_filter_name_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_filter_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_filter_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_filter_name_request_type** | [**QueryFilterNameRequestType**](QueryFilterNameRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The name of the filter.  |  -  |
**500** | ***NotFound***: If no filter with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_health_update_infos**
> List[HealthUpdateInfo] health_update_manager_query_health_update_infos(mo_id, query_health_update_infos_request_type)

Returns the list of HealthUpdateInfo configured for the given provider. 

Returns the list of HealthUpdateInfo configured for the given provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.health_update_info import HealthUpdateInfo
from vmware_vi.models.query_health_update_infos_request_type import QueryHealthUpdateInfosRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_health_update_infos_request_type = vmware_vi.QueryHealthUpdateInfosRequestType() # QueryHealthUpdateInfosRequestType | 

    try:
        # Returns the list of HealthUpdateInfo configured for the given provider. 
        api_response = api_instance.health_update_manager_query_health_update_infos(mo_id, query_health_update_infos_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_health_update_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_health_update_infos: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_health_update_infos_request_type** | [**QueryHealthUpdateInfosRequestType**](QueryHealthUpdateInfosRequestType.md)|  | 

### Return type

[**List[HealthUpdateInfo]**](HealthUpdateInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of configured HealthUpdateInfo.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_health_updates**
> List[HealthUpdate] health_update_manager_query_health_updates(mo_id, query_health_updates_request_type)

Returns the list of health updates reported by the given provider. 

Returns the list of health updates reported by the given provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.health_update import HealthUpdate
from vmware_vi.models.query_health_updates_request_type import QueryHealthUpdatesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_health_updates_request_type = vmware_vi.QueryHealthUpdatesRequestType() # QueryHealthUpdatesRequestType | 

    try:
        # Returns the list of health updates reported by the given provider. 
        api_response = api_instance.health_update_manager_query_health_updates(mo_id, query_health_updates_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_health_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_health_updates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_health_updates_request_type** | [**QueryHealthUpdatesRequestType**](QueryHealthUpdatesRequestType.md)|  | 

### Return type

[**List[HealthUpdate]**](HealthUpdate.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of current health updates by this provider.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_monitored_entities**
> List[ManagedObjectReference] health_update_manager_query_monitored_entities(mo_id, query_monitored_entities_request_type)

Returns the list of managed entities monitored by the given provider. 

Returns the list of managed entities monitored by the given provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_monitored_entities_request_type import QueryMonitoredEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_monitored_entities_request_type = vmware_vi.QueryMonitoredEntitiesRequestType() # QueryMonitoredEntitiesRequestType | 

    try:
        # Returns the list of managed entities monitored by the given provider. 
        api_response = api_instance.health_update_manager_query_monitored_entities(mo_id, query_monitored_entities_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_monitored_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_monitored_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_monitored_entities_request_type** | [**QueryMonitoredEntitiesRequestType**](QueryMonitoredEntitiesRequestType.md)|  | 

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
**200** | The list of monitored managed entities.  Refers instances of *ManagedEntity*.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_provider_list**
> List[str] health_update_manager_query_provider_list(mo_id)

The providers. 

The providers.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The providers. 
        api_response = api_instance.health_update_manager_query_provider_list(mo_id)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_provider_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_provider_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of identifiers of registered providers.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_provider_name**
> str health_update_manager_query_provider_name(mo_id, query_provider_name_request_type)

Query the name of the provider. 

Query the name of the provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_provider_name_request_type import QueryProviderNameRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_provider_name_request_type = vmware_vi.QueryProviderNameRequestType() # QueryProviderNameRequestType | 

    try:
        # Query the name of the provider. 
        api_response = api_instance.health_update_manager_query_provider_name(mo_id, query_provider_name_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_provider_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_provider_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_provider_name_request_type** | [**QueryProviderNameRequestType**](QueryProviderNameRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The name of the provider.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_query_unmonitored_hosts**
> List[ManagedObjectReference] health_update_manager_query_unmonitored_hosts(mo_id, query_unmonitored_hosts_request_type)

The set of hosts that are in the cluster, but not monitored by the provider. 

The set of hosts that are in the cluster, but not monitored by the provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_unmonitored_hosts_request_type import QueryUnmonitoredHostsRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_unmonitored_hosts_request_type = vmware_vi.QueryUnmonitoredHostsRequestType() # QueryUnmonitoredHostsRequestType | 

    try:
        # The set of hosts that are in the cluster, but not monitored by the provider. 
        api_response = api_instance.health_update_manager_query_unmonitored_hosts(mo_id, query_unmonitored_hosts_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_query_unmonitored_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_query_unmonitored_hosts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_unmonitored_hosts_request_type** | [**QueryUnmonitoredHostsRequestType**](QueryUnmonitoredHostsRequestType.md)|  | 

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
**200** | The hosts in the cluster that are not monitored by the provider.  Refers instances of *HostSystem*.  |  -  |
**500** | ***NotFound***: If no provider with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_register_health_update_provider**
> str health_update_manager_register_health_update_provider(mo_id, register_health_update_provider_request_type)

Registers provider. 

Registers provider.  ***Since:*** vSphere API 6.5  ***Required privileges:*** HealthUpdateProvider.Register 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.register_health_update_provider_request_type import RegisterHealthUpdateProviderRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_health_update_provider_request_type = vmware_vi.RegisterHealthUpdateProviderRequestType() # RegisterHealthUpdateProviderRequestType | 

    try:
        # Registers provider. 
        api_response = api_instance.health_update_manager_register_health_update_provider(mo_id, register_health_update_provider_request_type)
        print("The response of HealthUpdateManagerApi->health_update_manager_register_health_update_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_register_health_update_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_health_update_provider_request_type** | [**RegisterHealthUpdateProviderRequestType**](RegisterHealthUpdateProviderRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifier for the registered provider.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_remove_filter**
> health_update_manager_remove_filter(mo_id, remove_filter_request_type)

Removes the specified filter. 

Removes the specified filter.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_filter_request_type import RemoveFilterRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_filter_request_type = vmware_vi.RemoveFilterRequestType() # RemoveFilterRequestType | 

    try:
        # Removes the specified filter. 
        api_instance.health_update_manager_remove_filter(mo_id, remove_filter_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_remove_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_filter_request_type** | [**RemoveFilterRequestType**](RemoveFilterRequestType.md)|  | 

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
**500** | ***NotFound***: If no filter with this id is registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_remove_filter_entities**
> health_update_manager_remove_filter_entities(mo_id, remove_filter_entities_request_type)

Remove entities on which this filter is configured. 

Remove entities on which this filter is configured.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_filter_entities_request_type import RemoveFilterEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_filter_entities_request_type = vmware_vi.RemoveFilterEntitiesRequestType() # RemoveFilterEntitiesRequestType | 

    try:
        # Remove entities on which this filter is configured. 
        api_instance.health_update_manager_remove_filter_entities(mo_id, remove_filter_entities_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_remove_filter_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_filter_entities_request_type** | [**RemoveFilterEntitiesRequestType**](RemoveFilterEntitiesRequestType.md)|  | 

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
**500** | ***NotFound***: If no filter with this id is registered.  ***InvalidArgument***: - If there are duplicate managed entities in the given entities list. \\- If there is a managed entity of type other than HostSystem and ClusterComputeResource. \\- If the entities list contains an entity which is not associated with the specified filter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_remove_monitored_entities**
> health_update_manager_remove_monitored_entities(mo_id, remove_monitored_entities_request_type)

The provider monitors fewer managed entities. 

The provider monitors fewer managed entities.  ***Since:*** vSphere API 6.5  ***Required privileges:*** HealthUpdateProvider.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_monitored_entities_request_type import RemoveMonitoredEntitiesRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_monitored_entities_request_type = vmware_vi.RemoveMonitoredEntitiesRequestType() # RemoveMonitoredEntitiesRequestType | 

    try:
        # The provider monitors fewer managed entities. 
        api_instance.health_update_manager_remove_monitored_entities(mo_id, remove_monitored_entities_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_remove_monitored_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_monitored_entities_request_type** | [**RemoveMonitoredEntitiesRequestType**](RemoveMonitoredEntitiesRequestType.md)|  | 

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
**500** | ***NotFound***: If no provider with this id is registered.  ***InvalidState***: If any of the entities is a part of an InfraUpdateHa cluster that has the provider enabled.  ***NotSupported***: If the http session user does not match the user who registered the provider, or if the http session cannot be retrieved.  ***InvalidArgument***: - If any of the specified entities is not of type HostSystem. \\- If there are duplicate entities in the given entities list. \\- If any of the entities is already not being monitored by the specified provider.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_update_manager_unregister_health_update_provider**
> health_update_manager_unregister_health_update_provider(mo_id, unregister_health_update_provider_request_type)

Unregisters the specified provider, if it exists. 

Unregisters the specified provider, if it exists.  A VirtualCenter Server restart implicitly unregisters all providers.  ***Since:*** vSphere API 6.5  ***Required privileges:*** HealthUpdateProvider.Unregister 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unregister_health_update_provider_request_type import UnregisterHealthUpdateProviderRequestType
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
    api_instance = vmware_vi.HealthUpdateManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unregister_health_update_provider_request_type = vmware_vi.UnregisterHealthUpdateProviderRequestType() # UnregisterHealthUpdateProviderRequestType | 

    try:
        # Unregisters the specified provider, if it exists. 
        api_instance.health_update_manager_unregister_health_update_provider(mo_id, unregister_health_update_provider_request_type)
    except Exception as e:
        print("Exception when calling HealthUpdateManagerApi->health_update_manager_unregister_health_update_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unregister_health_update_provider_request_type** | [**UnregisterHealthUpdateProviderRequestType**](UnregisterHealthUpdateProviderRequestType.md)|  | 

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
**500** | ***NotFound***: If the specified provider is not registered.  ***InvalidState***: If the specified provider is still used in an InfraUpdateHa cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

