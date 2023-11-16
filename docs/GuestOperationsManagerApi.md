# vmware_vi.GuestOperationsManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_operations_manager_get_alias_manager**](GuestOperationsManagerApi.md#guest_operations_manager_get_alias_manager) | **GET** /GuestOperationsManager/{moId}/aliasManager | A managed object that provides methods to support single sign-on in the guest operating system. 
[**guest_operations_manager_get_auth_manager**](GuestOperationsManagerApi.md#guest_operations_manager_get_auth_manager) | **GET** /GuestOperationsManager/{moId}/authManager | A singleton managed object that provides methods for guest authentication operations. 
[**guest_operations_manager_get_file_manager**](GuestOperationsManagerApi.md#guest_operations_manager_get_file_manager) | **GET** /GuestOperationsManager/{moId}/fileManager | A singleton managed object that provides methods for guest file operations. 
[**guest_operations_manager_get_guest_windows_registry_manager**](GuestOperationsManagerApi.md#guest_operations_manager_get_guest_windows_registry_manager) | **GET** /GuestOperationsManager/{moId}/guestWindowsRegistryManager | A singleton managed object that provides methods for guest windows registry operations. 
[**guest_operations_manager_get_process_manager**](GuestOperationsManagerApi.md#guest_operations_manager_get_process_manager) | **GET** /GuestOperationsManager/{moId}/processManager | A singleton managed object that provides methods for guest process operations. 


# **guest_operations_manager_get_alias_manager**
> ManagedObjectReference guest_operations_manager_get_alias_manager(mo_id)

A managed object that provides methods to support single sign-on in the guest operating system. 

A managed object that provides methods to support single sign-on in the guest operating system.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Anonymous 

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
    api_instance = vmware_vi.GuestOperationsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A managed object that provides methods to support single sign-on in the guest operating system. 
        api_response = api_instance.guest_operations_manager_get_alias_manager(mo_id)
        print("The response of GuestOperationsManagerApi->guest_operations_manager_get_alias_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestOperationsManagerApi->guest_operations_manager_get_alias_manager: %s\n" % e)
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
**200** | Refers instance of *GuestAliasManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_operations_manager_get_auth_manager**
> ManagedObjectReference guest_operations_manager_get_auth_manager(mo_id)

A singleton managed object that provides methods for guest authentication operations. 

A singleton managed object that provides methods for guest authentication operations.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Anonymous 

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
    api_instance = vmware_vi.GuestOperationsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A singleton managed object that provides methods for guest authentication operations. 
        api_response = api_instance.guest_operations_manager_get_auth_manager(mo_id)
        print("The response of GuestOperationsManagerApi->guest_operations_manager_get_auth_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestOperationsManagerApi->guest_operations_manager_get_auth_manager: %s\n" % e)
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
**200** | Refers instance of *GuestAuthManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_operations_manager_get_file_manager**
> ManagedObjectReference guest_operations_manager_get_file_manager(mo_id)

A singleton managed object that provides methods for guest file operations. 

A singleton managed object that provides methods for guest file operations.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Anonymous 

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
    api_instance = vmware_vi.GuestOperationsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A singleton managed object that provides methods for guest file operations. 
        api_response = api_instance.guest_operations_manager_get_file_manager(mo_id)
        print("The response of GuestOperationsManagerApi->guest_operations_manager_get_file_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestOperationsManagerApi->guest_operations_manager_get_file_manager: %s\n" % e)
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
**200** | Refers instance of *GuestFileManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_operations_manager_get_guest_windows_registry_manager**
> ManagedObjectReference guest_operations_manager_get_guest_windows_registry_manager(mo_id)

A singleton managed object that provides methods for guest windows registry operations. 

A singleton managed object that provides methods for guest windows registry operations.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Anonymous 

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
    api_instance = vmware_vi.GuestOperationsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A singleton managed object that provides methods for guest windows registry operations. 
        api_response = api_instance.guest_operations_manager_get_guest_windows_registry_manager(mo_id)
        print("The response of GuestOperationsManagerApi->guest_operations_manager_get_guest_windows_registry_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestOperationsManagerApi->guest_operations_manager_get_guest_windows_registry_manager: %s\n" % e)
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
**200** | Refers instance of *GuestWindowsRegistryManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_operations_manager_get_process_manager**
> ManagedObjectReference guest_operations_manager_get_process_manager(mo_id)

A singleton managed object that provides methods for guest process operations. 

A singleton managed object that provides methods for guest process operations.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Anonymous 

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
    api_instance = vmware_vi.GuestOperationsManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A singleton managed object that provides methods for guest process operations. 
        api_response = api_instance.guest_operations_manager_get_process_manager(mo_id)
        print("The response of GuestOperationsManagerApi->guest_operations_manager_get_process_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestOperationsManagerApi->guest_operations_manager_get_process_manager: %s\n" % e)
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
**200** | Refers instance of *GuestProcessManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

