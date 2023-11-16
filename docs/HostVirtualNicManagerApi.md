# vmware_vi.HostVirtualNicManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_virtual_nic_manager_deselect_vnic_for_nic_type**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_deselect_vnic_for_nic_type) | **POST** /HostVirtualNicManager/{moId}/DeselectVnicForNicType | Deselect the VirtualNic to be a special type. 
[**host_virtual_nic_manager_get_available_field**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_get_available_field) | **GET** /HostVirtualNicManager/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**host_virtual_nic_manager_get_info**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_get_info) | **GET** /HostVirtualNicManager/{moId}/info | Network configuration. 
[**host_virtual_nic_manager_get_value**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_get_value) | **GET** /HostVirtualNicManager/{moId}/value | List of custom field values. 
[**host_virtual_nic_manager_query_net_config**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_query_net_config) | **POST** /HostVirtualNicManager/{moId}/QueryNetConfig | Get the NetConfig for the specified nicType 
[**host_virtual_nic_manager_select_vnic_for_nic_type**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_select_vnic_for_nic_type) | **POST** /HostVirtualNicManager/{moId}/SelectVnicForNicType | Select the NicType of the VirtualNic. 
[**host_virtual_nic_manager_set_custom_value**](HostVirtualNicManagerApi.md#host_virtual_nic_manager_set_custom_value) | **POST** /HostVirtualNicManager/{moId}/setCustomValue | Assigns a value to a custom field. 


# **host_virtual_nic_manager_deselect_vnic_for_nic_type**
> host_virtual_nic_manager_deselect_vnic_for_nic_type(mo_id, deselect_vnic_for_nic_type_request_type)

Deselect the VirtualNic to be a special type. 

Deselect the VirtualNic to be a special type.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.deselect_vnic_for_nic_type_request_type import DeselectVnicForNicTypeRequestType
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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    deselect_vnic_for_nic_type_request_type = vmware_vi.DeselectVnicForNicTypeRequestType() # DeselectVnicForNicTypeRequestType | 

    try:
        # Deselect the VirtualNic to be a special type. 
        api_instance.host_virtual_nic_manager_deselect_vnic_for_nic_type(mo_id, deselect_vnic_for_nic_type_request_type)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_deselect_vnic_for_nic_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **deselect_vnic_for_nic_type_request_type** | [**DeselectVnicForNicTypeRequestType**](DeselectVnicForNicTypeRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if nicType is invalid, device represents a nonexistent or invalid VirtualNic, or the VirtualNic is not selected  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_virtual_nic_manager_get_available_field**
> List[CustomFieldDef] host_virtual_nic_manager_get_available_field(mo_id)

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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.host_virtual_nic_manager_get_available_field(mo_id)
        print("The response of HostVirtualNicManagerApi->host_virtual_nic_manager_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_get_available_field: %s\n" % e)
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

# **host_virtual_nic_manager_get_info**
> HostVirtualNicManagerInfo host_virtual_nic_manager_get_info(mo_id)

Network configuration. 

Network configuration.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_virtual_nic_manager_info import HostVirtualNicManagerInfo
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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Network configuration. 
        api_response = api_instance.host_virtual_nic_manager_get_info(mo_id)
        print("The response of HostVirtualNicManagerApi->host_virtual_nic_manager_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostVirtualNicManagerInfo**](HostVirtualNicManagerInfo.md)

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

# **host_virtual_nic_manager_get_value**
> List[CustomFieldValue] host_virtual_nic_manager_get_value(mo_id)

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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.host_virtual_nic_manager_get_value(mo_id)
        print("The response of HostVirtualNicManagerApi->host_virtual_nic_manager_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_get_value: %s\n" % e)
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

# **host_virtual_nic_manager_query_net_config**
> VirtualNicManagerNetConfig host_virtual_nic_manager_query_net_config(mo_id, query_net_config_request_type)

Get the NetConfig for the specified nicType 

Get the NetConfig for the specified nicType  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_net_config_request_type import QueryNetConfigRequestType
from vmware_vi.models.virtual_nic_manager_net_config import VirtualNicManagerNetConfig
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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_net_config_request_type = vmware_vi.QueryNetConfigRequestType() # QueryNetConfigRequestType | 

    try:
        # Get the NetConfig for the specified nicType 
        api_response = api_instance.host_virtual_nic_manager_query_net_config(mo_id, query_net_config_request_type)
        print("The response of HostVirtualNicManagerApi->host_virtual_nic_manager_query_net_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_query_net_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_net_config_request_type** | [**QueryNetConfigRequestType**](QueryNetConfigRequestType.md)|  | 

### Return type

[**VirtualNicManagerNetConfig**](VirtualNicManagerNetConfig.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidArgument***: if nicType is invalid  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_virtual_nic_manager_select_vnic_for_nic_type**
> host_virtual_nic_manager_select_vnic_for_nic_type(mo_id, select_vnic_for_nic_type_request_type)

Select the NicType of the VirtualNic. 

Select the NicType of the VirtualNic.  Selecting a device automatically deselects the previous selection if *VirtualNicManagerNetConfig.multiSelectAllowed* is false for the specified nicType. Else, the device is added to the list of selected nics.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.select_vnic_for_nic_type_request_type import SelectVnicForNicTypeRequestType
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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    select_vnic_for_nic_type_request_type = vmware_vi.SelectVnicForNicTypeRequestType() # SelectVnicForNicTypeRequestType | 

    try:
        # Select the NicType of the VirtualNic. 
        api_instance.host_virtual_nic_manager_select_vnic_for_nic_type(mo_id, select_vnic_for_nic_type_request_type)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_select_vnic_for_nic_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **select_vnic_for_nic_type_request_type** | [**SelectVnicForNicTypeRequestType**](SelectVnicForNicTypeRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if nicType is invalid, or device represents a nonexistent or invalid VirtualNic  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_virtual_nic_manager_set_custom_value**
> host_virtual_nic_manager_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.HostVirtualNicManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.host_virtual_nic_manager_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling HostVirtualNicManagerApi->host_virtual_nic_manager_set_custom_value: %s\n" % e)
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

