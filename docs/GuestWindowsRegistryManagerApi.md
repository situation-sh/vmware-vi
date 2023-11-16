# vmware_vi.GuestWindowsRegistryManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_windows_registry_manager_create_registry_key_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_create_registry_key_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/CreateRegistryKeyInGuest | Create a registry key. 
[**guest_windows_registry_manager_delete_registry_key_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_delete_registry_key_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/DeleteRegistryKeyInGuest | Delete a registry key. 
[**guest_windows_registry_manager_delete_registry_value_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_delete_registry_value_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/DeleteRegistryValueInGuest | Delete a registry value. 
[**guest_windows_registry_manager_list_registry_keys_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_list_registry_keys_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/ListRegistryKeysInGuest | List all registry subkeys for a given registry key. 
[**guest_windows_registry_manager_list_registry_values_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_list_registry_values_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/ListRegistryValuesInGuest | List all registry values for a given registry key. 
[**guest_windows_registry_manager_set_registry_value_in_guest**](GuestWindowsRegistryManagerApi.md#guest_windows_registry_manager_set_registry_value_in_guest) | **POST** /GuestWindowsRegistryManager/{moId}/SetRegistryValueInGuest | Set/Create a registry value. 


# **guest_windows_registry_manager_create_registry_key_in_guest**
> guest_windows_registry_manager_create_registry_key_in_guest(mo_id, create_registry_key_in_guest_request_type)

Create a registry key. 

Create a registry key.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_registry_key_in_guest_request_type import CreateRegistryKeyInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_registry_key_in_guest_request_type = vmware_vi.CreateRegistryKeyInGuestRequestType() # CreateRegistryKeyInGuestRequestType | 

    try:
        # Create a registry key. 
        api_instance.guest_windows_registry_manager_create_registry_key_in_guest(mo_id, create_registry_key_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_create_registry_key_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_registry_key_in_guest_request_type** | [**CreateRegistryKeyInGuestRequestType**](CreateRegistryKeyInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestRegistryKeyAlreadyExists***: if the registry key already exists.  ***GuestRegistryKeyParentVolatile***: if trying to create a non-volatile registry subkey under a volatile registry parent key.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_windows_registry_manager_delete_registry_key_in_guest**
> guest_windows_registry_manager_delete_registry_key_in_guest(mo_id, delete_registry_key_in_guest_request_type)

Delete a registry key. 

Delete a registry key.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_registry_key_in_guest_request_type import DeleteRegistryKeyInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_registry_key_in_guest_request_type = vmware_vi.DeleteRegistryKeyInGuestRequestType() # DeleteRegistryKeyInGuestRequestType | 

    try:
        # Delete a registry key. 
        api_instance.guest_windows_registry_manager_delete_registry_key_in_guest(mo_id, delete_registry_key_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_delete_registry_key_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_registry_key_in_guest_request_type** | [**DeleteRegistryKeyInGuestRequestType**](DeleteRegistryKeyInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestRegistryKeyHasSubkeys***: if the parameter recursive is false and the key has subkeys.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_windows_registry_manager_delete_registry_value_in_guest**
> guest_windows_registry_manager_delete_registry_value_in_guest(mo_id, delete_registry_value_in_guest_request_type)

Delete a registry value. 

Delete a registry value.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_registry_value_in_guest_request_type import DeleteRegistryValueInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_registry_value_in_guest_request_type = vmware_vi.DeleteRegistryValueInGuestRequestType() # DeleteRegistryValueInGuestRequestType | 

    try:
        # Delete a registry value. 
        api_instance.guest_windows_registry_manager_delete_registry_value_in_guest(mo_id, delete_registry_value_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_delete_registry_value_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_registry_value_in_guest_request_type** | [**DeleteRegistryValueInGuestRequestType**](DeleteRegistryValueInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestRegistryValueNotFound***: if the registry value was not found.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_windows_registry_manager_list_registry_keys_in_guest**
> List[GuestRegKeyRecordSpec] guest_windows_registry_manager_list_registry_keys_in_guest(mo_id, list_registry_keys_in_guest_request_type)

List all registry subkeys for a given registry key. 

List all registry subkeys for a given registry key.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_reg_key_record_spec import GuestRegKeyRecordSpec
from vmware_vi.models.list_registry_keys_in_guest_request_type import ListRegistryKeysInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_registry_keys_in_guest_request_type = vmware_vi.ListRegistryKeysInGuestRequestType() # ListRegistryKeysInGuestRequestType | 

    try:
        # List all registry subkeys for a given registry key. 
        api_response = api_instance.guest_windows_registry_manager_list_registry_keys_in_guest(mo_id, list_registry_keys_in_guest_request_type)
        print("The response of GuestWindowsRegistryManagerApi->guest_windows_registry_manager_list_registry_keys_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_list_registry_keys_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_registry_keys_in_guest_request_type** | [**ListRegistryKeysInGuestRequestType**](ListRegistryKeysInGuestRequestType.md)|  | 

### Return type

[**List[GuestRegKeyRecordSpec]**](GuestRegKeyRecordSpec.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of subkeys is returned in an array of *GuestRegKeySpec* structures.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_windows_registry_manager_list_registry_values_in_guest**
> List[GuestRegValueSpec] guest_windows_registry_manager_list_registry_values_in_guest(mo_id, list_registry_values_in_guest_request_type)

List all registry values for a given registry key. 

List all registry values for a given registry key.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_reg_value_spec import GuestRegValueSpec
from vmware_vi.models.list_registry_values_in_guest_request_type import ListRegistryValuesInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_registry_values_in_guest_request_type = vmware_vi.ListRegistryValuesInGuestRequestType() # ListRegistryValuesInGuestRequestType | 

    try:
        # List all registry values for a given registry key. 
        api_response = api_instance.guest_windows_registry_manager_list_registry_values_in_guest(mo_id, list_registry_values_in_guest_request_type)
        print("The response of GuestWindowsRegistryManagerApi->guest_windows_registry_manager_list_registry_values_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_list_registry_values_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_registry_values_in_guest_request_type** | [**ListRegistryValuesInGuestRequestType**](ListRegistryValuesInGuestRequestType.md)|  | 

### Return type

[**List[GuestRegValueSpec]**](GuestRegValueSpec.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of values is returned in an array of *GuestRegValueSpec* structures.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_windows_registry_manager_set_registry_value_in_guest**
> guest_windows_registry_manager_set_registry_value_in_guest(mo_id, set_registry_value_in_guest_request_type)

Set/Create a registry value. 

Set/Create a registry value.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_registry_value_in_guest_request_type import SetRegistryValueInGuestRequestType
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
    api_instance = vmware_vi.GuestWindowsRegistryManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_registry_value_in_guest_request_type = vmware_vi.SetRegistryValueInGuestRequestType() # SetRegistryValueInGuestRequestType | 

    try:
        # Set/Create a registry value. 
        api_instance.guest_windows_registry_manager_set_registry_value_in_guest(mo_id, set_registry_value_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestWindowsRegistryManagerApi->guest_windows_registry_manager_set_registry_value_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_registry_value_in_guest_request_type** | [**SetRegistryValueInGuestRequestType**](SetRegistryValueInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestRegistryKeyInvalid***: if the registry key is not valid. Check the HKEY Root specified.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

