# vmware_vi.HostPciPassthruSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_pci_passthru_system_get_available_field**](HostPciPassthruSystemApi.md#host_pci_passthru_system_get_available_field) | **GET** /HostPciPassthruSystem/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**host_pci_passthru_system_get_pci_passthru_info**](HostPciPassthruSystemApi.md#host_pci_passthru_system_get_pci_passthru_info) | **GET** /HostPciPassthruSystem/{moId}/pciPassthruInfo | Array of PciPassthru information 
[**host_pci_passthru_system_get_sriov_device_pool_info**](HostPciPassthruSystemApi.md#host_pci_passthru_system_get_sriov_device_pool_info) | **GET** /HostPciPassthruSystem/{moId}/sriovDevicePoolInfo | Array of Sriov Device Pool information 
[**host_pci_passthru_system_get_value**](HostPciPassthruSystemApi.md#host_pci_passthru_system_get_value) | **GET** /HostPciPassthruSystem/{moId}/value | List of custom field values. 
[**host_pci_passthru_system_refresh**](HostPciPassthruSystemApi.md#host_pci_passthru_system_refresh) | **POST** /HostPciPassthruSystem/{moId}/Refresh | Refresh the available PciPassthru information. 
[**host_pci_passthru_system_set_custom_value**](HostPciPassthruSystemApi.md#host_pci_passthru_system_set_custom_value) | **POST** /HostPciPassthruSystem/{moId}/setCustomValue | Assigns a value to a custom field. 
[**host_pci_passthru_system_update_passthru_config**](HostPciPassthruSystemApi.md#host_pci_passthru_system_update_passthru_config) | **POST** /HostPciPassthruSystem/{moId}/UpdatePassthruConfig | Updates the PciPassthru configuration, this will get called for the dependent device with the enabled bool set 


# **host_pci_passthru_system_get_available_field**
> List[CustomFieldDef] host_pci_passthru_system_get_available_field(mo_id)

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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.host_pci_passthru_system_get_available_field(mo_id)
        print("The response of HostPciPassthruSystemApi->host_pci_passthru_system_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_get_available_field: %s\n" % e)
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

# **host_pci_passthru_system_get_pci_passthru_info**
> List[HostPciPassthruInfo] host_pci_passthru_system_get_pci_passthru_info(mo_id)

Array of PciPassthru information 

Array of PciPassthru information  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_pci_passthru_info import HostPciPassthruInfo
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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Array of PciPassthru information 
        api_response = api_instance.host_pci_passthru_system_get_pci_passthru_info(mo_id)
        print("The response of HostPciPassthruSystemApi->host_pci_passthru_system_get_pci_passthru_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_get_pci_passthru_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostPciPassthruInfo]**](HostPciPassthruInfo.md)

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

# **host_pci_passthru_system_get_sriov_device_pool_info**
> List[HostSriovDevicePoolInfo] host_pci_passthru_system_get_sriov_device_pool_info(mo_id)

Array of Sriov Device Pool information 

Array of Sriov Device Pool information  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_sriov_device_pool_info import HostSriovDevicePoolInfo
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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Array of Sriov Device Pool information 
        api_response = api_instance.host_pci_passthru_system_get_sriov_device_pool_info(mo_id)
        print("The response of HostPciPassthruSystemApi->host_pci_passthru_system_get_sriov_device_pool_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_get_sriov_device_pool_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostSriovDevicePoolInfo]**](HostSriovDevicePoolInfo.md)

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

# **host_pci_passthru_system_get_value**
> List[CustomFieldValue] host_pci_passthru_system_get_value(mo_id)

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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.host_pci_passthru_system_get_value(mo_id)
        print("The response of HostPciPassthruSystemApi->host_pci_passthru_system_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_get_value: %s\n" % e)
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

# **host_pci_passthru_system_refresh**
> host_pci_passthru_system_refresh(mo_id)

Refresh the available PciPassthru information. 

Refresh the available PciPassthru information.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Settings 

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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Refresh the available PciPassthru information. 
        api_instance.host_pci_passthru_system_refresh(mo_id)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_refresh: %s\n" % e)
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

# **host_pci_passthru_system_set_custom_value**
> host_pci_passthru_system_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.host_pci_passthru_system_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_set_custom_value: %s\n" % e)
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

# **host_pci_passthru_system_update_passthru_config**
> host_pci_passthru_system_update_passthru_config(mo_id, update_passthru_config_request_type)

Updates the PciPassthru configuration, this will get called for the dependent device with the enabled bool set 

Updates the PciPassthru configuration, this will get called for the dependent device with the enabled bool set  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.PciPassthru 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_passthru_config_request_type import UpdatePassthruConfigRequestType
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
    api_instance = vmware_vi.HostPciPassthruSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_passthru_config_request_type = vmware_vi.UpdatePassthruConfigRequestType() # UpdatePassthruConfigRequestType | 

    try:
        # Updates the PciPassthru configuration, this will get called for the dependent device with the enabled bool set 
        api_instance.host_pci_passthru_system_update_passthru_config(mo_id, update_passthru_config_request_type)
    except Exception as e:
        print("Exception when calling HostPciPassthruSystemApi->host_pci_passthru_system_update_passthru_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_passthru_config_request_type** | [**UpdatePassthruConfigRequestType**](UpdatePassthruConfigRequestType.md)|  | 

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
**500** | ***HostConfigFault***: if an error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

