# vmware_vi.HostMemorySystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_memory_system_get_available_field**](HostMemorySystemApi.md#host_memory_system_get_available_field) | **GET** /HostMemorySystem/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**host_memory_system_get_console_reservation_info**](HostMemorySystemApi.md#host_memory_system_get_console_reservation_info) | **GET** /HostMemorySystem/{moId}/consoleReservationInfo | Service console reservation information for the memory manager. 
[**host_memory_system_get_value**](HostMemorySystemApi.md#host_memory_system_get_value) | **GET** /HostMemorySystem/{moId}/value | List of custom field values. 
[**host_memory_system_get_virtual_machine_reservation_info**](HostMemorySystemApi.md#host_memory_system_get_virtual_machine_reservation_info) | **GET** /HostMemorySystem/{moId}/virtualMachineReservationInfo | Virtual machine reservation information for the memory manager. 
[**host_memory_system_reconfigure_service_console_reservation**](HostMemorySystemApi.md#host_memory_system_reconfigure_service_console_reservation) | **POST** /HostMemorySystem/{moId}/ReconfigureServiceConsoleReservation | Sets the configured service console memory reservation. 
[**host_memory_system_reconfigure_virtual_machine_reservation**](HostMemorySystemApi.md#host_memory_system_reconfigure_virtual_machine_reservation) | **POST** /HostMemorySystem/{moId}/ReconfigureVirtualMachineReservation | Updates the virtual machine reservation information. 
[**host_memory_system_set_custom_value**](HostMemorySystemApi.md#host_memory_system_set_custom_value) | **POST** /HostMemorySystem/{moId}/setCustomValue | Assigns a value to a custom field. 


# **host_memory_system_get_available_field**
> List[CustomFieldDef] host_memory_system_get_available_field(mo_id)

List of custom field definitions that are valid for the object's type. 

List of custom field definitions that are valid for the object's type.  The fields are sorted by *CustomFieldDef.name*.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_def import CustomFieldDef
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.host_memory_system_get_available_field(mo_id)
        print("The response of HostMemorySystemApi->host_memory_system_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_get_available_field: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldDef]**](CustomFieldDef.md)

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

# **host_memory_system_get_console_reservation_info**
> ServiceConsoleReservationInfo host_memory_system_get_console_reservation_info(mo_id)

Service console reservation information for the memory manager. 

Service console reservation information for the memory manager.  The existence of this data object indicates if the service console memory reservation must be configured for this host. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.service_console_reservation_info import ServiceConsoleReservationInfo
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Service console reservation information for the memory manager. 
        api_response = api_instance.host_memory_system_get_console_reservation_info(mo_id)
        print("The response of HostMemorySystemApi->host_memory_system_get_console_reservation_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_get_console_reservation_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ServiceConsoleReservationInfo**](ServiceConsoleReservationInfo.md)

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

# **host_memory_system_get_value**
> List[CustomFieldValue] host_memory_system_get_value(mo_id)

List of custom field values. 

List of custom field values.  Each value uses a key to associate an instance of a *CustomFieldStringValue* with a custom field definition.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_value import CustomFieldValue
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.host_memory_system_get_value(mo_id)
        print("The response of HostMemorySystemApi->host_memory_system_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_get_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldValue]**](CustomFieldValue.md)

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

# **host_memory_system_get_virtual_machine_reservation_info**
> VirtualMachineMemoryReservationInfo host_memory_system_get_virtual_machine_reservation_info(mo_id)

Virtual machine reservation information for the memory manager. 

Virtual machine reservation information for the memory manager.  The existence of this data object indicates if the virtual machine memory reservation must be configured for this host.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_memory_reservation_info import VirtualMachineMemoryReservationInfo
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Virtual machine reservation information for the memory manager. 
        api_response = api_instance.host_memory_system_get_virtual_machine_reservation_info(mo_id)
        print("The response of HostMemorySystemApi->host_memory_system_get_virtual_machine_reservation_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_get_virtual_machine_reservation_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineMemoryReservationInfo**](VirtualMachineMemoryReservationInfo.md)

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

# **host_memory_system_reconfigure_service_console_reservation**
> host_memory_system_reconfigure_service_console_reservation(mo_id, reconfigure_service_console_reservation_request_type)

Sets the configured service console memory reservation. 

Sets the configured service console memory reservation.  This change affects only the serviceConsoleReservedCfg property. The configuration change propagates to the other properties after the next boot.  ***Required privileges:*** Host.Config.Memory 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfigure_service_console_reservation_request_type import ReconfigureServiceConsoleReservationRequestType
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_service_console_reservation_request_type = vmware_vi.ReconfigureServiceConsoleReservationRequestType() # ReconfigureServiceConsoleReservationRequestType | 

    try:
        # Sets the configured service console memory reservation. 
        api_instance.host_memory_system_reconfigure_service_console_reservation(mo_id, reconfigure_service_console_reservation_request_type)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_reconfigure_service_console_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_service_console_reservation_request_type** | [**ReconfigureServiceConsoleReservationRequestType**](ReconfigureServiceConsoleReservationRequestType.md)|  | 

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

# **host_memory_system_reconfigure_virtual_machine_reservation**
> host_memory_system_reconfigure_virtual_machine_reservation(mo_id, reconfigure_virtual_machine_reservation_request_type)

Updates the virtual machine reservation information. 

Updates the virtual machine reservation information.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Memory 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfigure_virtual_machine_reservation_request_type import ReconfigureVirtualMachineReservationRequestType
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_virtual_machine_reservation_request_type = vmware_vi.ReconfigureVirtualMachineReservationRequestType() # ReconfigureVirtualMachineReservationRequestType | 

    try:
        # Updates the virtual machine reservation information. 
        api_instance.host_memory_system_reconfigure_virtual_machine_reservation(mo_id, reconfigure_virtual_machine_reservation_request_type)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_reconfigure_virtual_machine_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_virtual_machine_reservation_request_type** | [**ReconfigureVirtualMachineReservationRequestType**](ReconfigureVirtualMachineReservationRequestType.md)|  | 

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

# **host_memory_system_set_custom_value**
> host_memory_system_set_custom_value(mo_id, set_custom_value_request_type)

Assigns a value to a custom field. 

Assigns a value to a custom field.  The setCustomValue method requires whichever updatePrivilege is defined as one of the *CustomFieldDef.fieldInstancePrivileges* for the CustomFieldDef whose value is being changed.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_custom_value_request_type import SetCustomValueRequestType
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
    api_instance = vmware_vi.HostMemorySystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.host_memory_system_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling HostMemorySystemApi->host_memory_system_set_custom_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_custom_value_request_type** | [**SetCustomValueRequestType**](SetCustomValueRequestType.md)|  | 

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

