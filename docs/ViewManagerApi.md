# vmware_vi.ViewManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**view_manager_create_container_view**](ViewManagerApi.md#view_manager_create_container_view) | **POST** /ViewManager/{moId}/CreateContainerView | Create a *ContainerView* managed object for this session. 
[**view_manager_create_inventory_view**](ViewManagerApi.md#view_manager_create_inventory_view) | **POST** /ViewManager/{moId}/CreateInventoryView | Create a new *InventoryView* managed object for this session. 
[**view_manager_create_list_view**](ViewManagerApi.md#view_manager_create_list_view) | **POST** /ViewManager/{moId}/CreateListView | Create a *ListView* object for this session. 
[**view_manager_create_list_view_from_view**](ViewManagerApi.md#view_manager_create_list_view_from_view) | **POST** /ViewManager/{moId}/CreateListViewFromView | Create a *ListView* object for this session. 
[**view_manager_get_view_list**](ViewManagerApi.md#view_manager_get_view_list) | **GET** /ViewManager/{moId}/viewList | An array of view references. 


# **view_manager_create_container_view**
> ManagedObjectReference view_manager_create_container_view(mo_id, create_container_view_request_type)

Create a *ContainerView* managed object for this session. 

Create a *ContainerView* managed object for this session.  The method returns a reference to a *ContainerView* object that has a list of managed object references. The list references objects in the container and may include references to objects from additional containers. You can configure the resulting list of objects by specifying a type list and recursion. Once you have created the view, the object list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_container_view_request_type import CreateContainerViewRequestType
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
    api_instance = vmware_vi.ViewManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_container_view_request_type = vmware_vi.CreateContainerViewRequestType() # CreateContainerViewRequestType | 

    try:
        # Create a *ContainerView* managed object for this session. 
        api_response = api_instance.view_manager_create_container_view(mo_id, create_container_view_request_type)
        print("The response of ViewManagerApi->view_manager_create_container_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewManagerApi->view_manager_create_container_view: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_container_view_request_type** | [**CreateContainerViewRequestType**](CreateContainerViewRequestType.md)|  | 

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
**200** | Refers instance of *ContainerView*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_manager_create_inventory_view**
> ManagedObjectReference view_manager_create_inventory_view(mo_id)

Create a new *InventoryView* managed object for this session. 

Create a new *InventoryView* managed object for this session.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ViewManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Create a new *InventoryView* managed object for this session. 
        api_response = api_instance.view_manager_create_inventory_view(mo_id)
        print("The response of ViewManagerApi->view_manager_create_inventory_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewManagerApi->view_manager_create_inventory_view: %s\n" % e)
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
**200** | Refers instance of *InventoryView*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_manager_create_list_view**
> ManagedObjectReference view_manager_create_list_view(mo_id, create_list_view_request_type)

Create a *ListView* object for this session. 

Create a *ListView* object for this session.  The method returns a session object that has a list of managed object references. The list of references corresponds to the input object list. You can modify the resulting list after you have created the object.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_list_view_request_type import CreateListViewRequestType
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
    api_instance = vmware_vi.ViewManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_list_view_request_type = vmware_vi.CreateListViewRequestType() # CreateListViewRequestType | 

    try:
        # Create a *ListView* object for this session. 
        api_response = api_instance.view_manager_create_list_view(mo_id, create_list_view_request_type)
        print("The response of ViewManagerApi->view_manager_create_list_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewManagerApi->view_manager_create_list_view: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_list_view_request_type** | [**CreateListViewRequestType**](CreateListViewRequestType.md)|  | 

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
**200** | Refers instance of *ListView*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_manager_create_list_view_from_view**
> ManagedObjectReference view_manager_create_list_view_from_view(mo_id, create_list_view_from_view_request_type)

Create a *ListView* object for this session. 

Create a *ListView* object for this session.  This method uses an existing view to construct the object list for the new view.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_list_view_from_view_request_type import CreateListViewFromViewRequestType
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
    api_instance = vmware_vi.ViewManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_list_view_from_view_request_type = vmware_vi.CreateListViewFromViewRequestType() # CreateListViewFromViewRequestType | 

    try:
        # Create a *ListView* object for this session. 
        api_response = api_instance.view_manager_create_list_view_from_view(mo_id, create_list_view_from_view_request_type)
        print("The response of ViewManagerApi->view_manager_create_list_view_from_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewManagerApi->view_manager_create_list_view_from_view: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_list_view_from_view_request_type** | [**CreateListViewFromViewRequestType**](CreateListViewFromViewRequestType.md)|  | 

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
**200** | Refers instance of *ListView*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_manager_get_view_list**
> List[ManagedObjectReference] view_manager_get_view_list(mo_id)

An array of view references. 

An array of view references.  Each array entry is a managed object reference to a view created by this ViewManager.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ViewManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # An array of view references. 
        api_response = api_instance.view_manager_get_view_list(mo_id)
        print("The response of ViewManagerApi->view_manager_get_view_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewManagerApi->view_manager_get_view_list: %s\n" % e)
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
**200** | Refers instances of *View*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

