# vmware_vi.InventoryViewApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_view_close_inventory_view_folder**](InventoryViewApi.md#inventory_view_close_inventory_view_folder) | **POST** /InventoryView/{moId}/CloseInventoryViewFolder | Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent. 
[**inventory_view_destroy_view**](InventoryViewApi.md#inventory_view_destroy_view) | **POST** /InventoryView/{moId}/DestroyView | Destroy this view. 
[**inventory_view_get_view**](InventoryViewApi.md#inventory_view_get_view) | **GET** /InventoryView/{moId}/view | The list of references to objects mapped by this view. 
[**inventory_view_open_inventory_view_folder**](InventoryViewApi.md#inventory_view_open_inventory_view_folder) | **POST** /InventoryView/{moId}/OpenInventoryViewFolder | Adds the child objects of a given managed entity to the view. 


# **inventory_view_close_inventory_view_folder**
> List[ManagedObjectReference] inventory_view_close_inventory_view_folder(mo_id, close_inventory_view_folder_request_type)

Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent. 

Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent.  The associated child objects are removed from the view. The containers themselves will still be retained as open objects until their parent is closed.  May partially succeed if some entities could not be resolved. The operation will still succeed for all entities that could be resolved, and the list of those that failed is returned as the result.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.close_inventory_view_folder_request_type import CloseInventoryViewFolderRequestType
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
    api_instance = vmware_vi.InventoryViewApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    close_inventory_view_folder_request_type = vmware_vi.CloseInventoryViewFolderRequestType() # CloseInventoryViewFolderRequestType | 

    try:
        # Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent. 
        api_response = api_instance.inventory_view_close_inventory_view_folder(mo_id, close_inventory_view_folder_request_type)
        print("The response of InventoryViewApi->inventory_view_close_inventory_view_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryViewApi->inventory_view_close_inventory_view_folder: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **close_inventory_view_folder_request_type** | [**CloseInventoryViewFolderRequestType**](CloseInventoryViewFolderRequestType.md)|  | 

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
**200** | A list containing any entities in the argument could not be resolved.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_view_destroy_view**
> inventory_view_destroy_view(mo_id)

Destroy this view. 

Destroy this view.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.InventoryViewApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroy this view. 
        api_instance.inventory_view_destroy_view(mo_id)
    except Exception as e:
        print("Exception when calling InventoryViewApi->inventory_view_destroy_view: %s\n" % e)
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

# **inventory_view_get_view**
> List[ManagedObjectReference] inventory_view_get_view(mo_id)

The list of references to objects mapped by this view. 

The list of references to objects mapped by this view.  ***Since:*** VI API 2.5 

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
    api_instance = vmware_vi.InventoryViewApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of references to objects mapped by this view. 
        api_response = api_instance.inventory_view_get_view(mo_id)
        print("The response of InventoryViewApi->inventory_view_get_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryViewApi->inventory_view_get_view: %s\n" % e)
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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_view_open_inventory_view_folder**
> List[ManagedObjectReference] inventory_view_open_inventory_view_folder(mo_id, open_inventory_view_folder_request_type)

Adds the child objects of a given managed entity to the view. 

Adds the child objects of a given managed entity to the view.  If a *Datacenter* is returned as a child, the implicit virtual machine folder and host folder objects are also returned. If a *ComputeResource* is returned, the implicit root *ResourcePool* and *HostSystem* objects are also returned.  May partially succeed if some entities could not be resolved. The operation will still succeed for all entities which could be resolved, and the list of those which failed is returned as the result.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.open_inventory_view_folder_request_type import OpenInventoryViewFolderRequestType
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
    api_instance = vmware_vi.InventoryViewApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    open_inventory_view_folder_request_type = vmware_vi.OpenInventoryViewFolderRequestType() # OpenInventoryViewFolderRequestType | 

    try:
        # Adds the child objects of a given managed entity to the view. 
        api_response = api_instance.inventory_view_open_inventory_view_folder(mo_id, open_inventory_view_folder_request_type)
        print("The response of InventoryViewApi->inventory_view_open_inventory_view_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryViewApi->inventory_view_open_inventory_view_folder: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **open_inventory_view_folder_request_type** | [**OpenInventoryViewFolderRequestType**](OpenInventoryViewFolderRequestType.md)|  | 

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
**200** | A list containing any entities in the argument could not be resolved.  Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

