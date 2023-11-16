# vmware_vi.TenantTenantManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_tenant_manager_mark_service_provider_entities**](TenantTenantManagerApi.md#tenant_tenant_manager_mark_service_provider_entities) | **POST** /TenantTenantManager/{moId}/MarkServiceProviderEntities | Define a set of ManagedEntity objects as used for tenant management. 
[**tenant_tenant_manager_retrieve_service_provider_entities**](TenantTenantManagerApi.md#tenant_tenant_manager_retrieve_service_provider_entities) | **POST** /TenantTenantManager/{moId}/RetrieveServiceProviderEntities | Retrieves the list of tenant management entities. 
[**tenant_tenant_manager_unmark_service_provider_entities**](TenantTenantManagerApi.md#tenant_tenant_manager_unmark_service_provider_entities) | **POST** /TenantTenantManager/{moId}/UnmarkServiceProviderEntities | Resets the management type of an array of ManagedEntity objects. 


# **tenant_tenant_manager_mark_service_provider_entities**
> tenant_tenant_manager_mark_service_provider_entities(mo_id, mark_service_provider_entities_request_type)

Define a set of ManagedEntity objects as used for tenant management. 

Define a set of ManagedEntity objects as used for tenant management.  Those entities are a starting point of an inventory hierarchy (sub-tree) that functionally exists in the tenant's inventory but are owned by the system user of the vCenter Server. The operations which the tenant may perform on these objects depend on the permissions granted to the tenant by the SaaS provisioning layer. Permissions that the tenant may create on the parent objects of the management entities do not propagate to the hierarchies of management entities and thus have no effect on them. This operation will fail for all the entities if any of them does not exist. The method behaviour is transactional - either all entities are marked or none if an error occurs while processing them. The user calling this method should hold TenantManager.Update on the root folder and TenantManager.Update on each entity currently being marked as a service provider one. These are strict privilege requirements allowing only administrators to call the method.  ***Since:*** vSphere API 6.9.1  ***Required privileges:*** TenantManager.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mark_service_provider_entities_request_type import MarkServiceProviderEntitiesRequestType
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
    api_instance = vmware_vi.TenantTenantManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_service_provider_entities_request_type = vmware_vi.MarkServiceProviderEntitiesRequestType() # MarkServiceProviderEntitiesRequestType | 

    try:
        # Define a set of ManagedEntity objects as used for tenant management. 
        api_instance.tenant_tenant_manager_mark_service_provider_entities(mo_id, mark_service_provider_entities_request_type)
    except Exception as e:
        print("Exception when calling TenantTenantManagerApi->tenant_tenant_manager_mark_service_provider_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_service_provider_entities_request_type** | [**MarkServiceProviderEntitiesRequestType**](MarkServiceProviderEntitiesRequestType.md)|  | 

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
**500** | ***ManagedObjectNotFound***: if any of the entities doesn&#39;t exist.  ***AuthMinimumAdminPermission***: if this change will leave the system with no Administrator permission on the root folder of the service provider inventory.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_tenant_manager_retrieve_service_provider_entities**
> List[ManagedObjectReference] tenant_tenant_manager_retrieve_service_provider_entities(mo_id)

Retrieves the list of tenant management entities. 

Retrieves the list of tenant management entities.  ***Since:*** vSphere API 6.9.1  ***Required privileges:*** TenantManager.Query 

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
    api_instance = vmware_vi.TenantTenantManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieves the list of tenant management entities. 
        api_response = api_instance.tenant_tenant_manager_retrieve_service_provider_entities(mo_id)
        print("The response of TenantTenantManagerApi->tenant_tenant_manager_retrieve_service_provider_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTenantManagerApi->tenant_tenant_manager_retrieve_service_provider_entities: %s\n" % e)
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
**200** | the array of tenant management resources.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_tenant_manager_unmark_service_provider_entities**
> tenant_tenant_manager_unmark_service_provider_entities(mo_id, unmark_service_provider_entities_request_type)

Resets the management type of an array of ManagedEntity objects. 

Resets the management type of an array of ManagedEntity objects.  This operation will fail if any of the entities does not exist. The method behaviour is transactional - either all entities are unmarked or none if an error occurs while processing them. The user calling this method should hold TenantManager.Update on the root folder and TenantManager.Update on each entity currently being unmarked as a service provider one. These are strict privilege requirements allowing only administrators to call the method.  ***Since:*** vSphere API 6.9.1  ***Required privileges:*** TenantManager.Update 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unmark_service_provider_entities_request_type import UnmarkServiceProviderEntitiesRequestType
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
    api_instance = vmware_vi.TenantTenantManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmark_service_provider_entities_request_type = vmware_vi.UnmarkServiceProviderEntitiesRequestType() # UnmarkServiceProviderEntitiesRequestType | 

    try:
        # Resets the management type of an array of ManagedEntity objects. 
        api_instance.tenant_tenant_manager_unmark_service_provider_entities(mo_id, unmark_service_provider_entities_request_type)
    except Exception as e:
        print("Exception when calling TenantTenantManagerApi->tenant_tenant_manager_unmark_service_provider_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmark_service_provider_entities_request_type** | [**UnmarkServiceProviderEntitiesRequestType**](UnmarkServiceProviderEntitiesRequestType.md)|  | 

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
**500** | ***ManagedObjectNotFound***: if any of the entities doesn&#39;t exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

