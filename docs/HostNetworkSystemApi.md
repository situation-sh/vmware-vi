# vmware_vi.HostNetworkSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_network_system_add_port_group**](HostNetworkSystemApi.md#host_network_system_add_port_group) | **POST** /HostNetworkSystem/{moId}/AddPortGroup | Adds a port group to the virtual switch. 
[**host_network_system_add_service_console_virtual_nic**](HostNetworkSystemApi.md#host_network_system_add_service_console_virtual_nic) | **POST** /HostNetworkSystem/{moId}/AddServiceConsoleVirtualNic | Adds a virtual service console network adapter. 
[**host_network_system_add_virtual_nic**](HostNetworkSystemApi.md#host_network_system_add_virtual_nic) | **POST** /HostNetworkSystem/{moId}/AddVirtualNic | Adds a virtual host/VMkernel network adapter. 
[**host_network_system_add_virtual_switch**](HostNetworkSystemApi.md#host_network_system_add_virtual_switch) | **POST** /HostNetworkSystem/{moId}/AddVirtualSwitch | Adds a new virtual switch to the system with the given name. 
[**host_network_system_get_available_field**](HostNetworkSystemApi.md#host_network_system_get_available_field) | **GET** /HostNetworkSystem/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**host_network_system_get_capabilities**](HostNetworkSystemApi.md#host_network_system_get_capabilities) | **GET** /HostNetworkSystem/{moId}/capabilities | Capability vector indicating the available product features. 
[**host_network_system_get_console_ip_route_config**](HostNetworkSystemApi.md#host_network_system_get_console_ip_route_config) | **GET** /HostNetworkSystem/{moId}/consoleIpRouteConfig | IP route configuration for the service console. 
[**host_network_system_get_dns_config**](HostNetworkSystemApi.md#host_network_system_get_dns_config) | **GET** /HostNetworkSystem/{moId}/dnsConfig | Client-side DNS configuration. 
[**host_network_system_get_ip_route_config**](HostNetworkSystemApi.md#host_network_system_get_ip_route_config) | **GET** /HostNetworkSystem/{moId}/ipRouteConfig | The IP route configuration. 
[**host_network_system_get_network_config**](HostNetworkSystemApi.md#host_network_system_get_network_config) | **GET** /HostNetworkSystem/{moId}/networkConfig | Network configuration information. 
[**host_network_system_get_network_info**](HostNetworkSystemApi.md#host_network_system_get_network_info) | **GET** /HostNetworkSystem/{moId}/networkInfo | The network configuration and runtime information. 
[**host_network_system_get_offload_capabilities**](HostNetworkSystemApi.md#host_network_system_get_offload_capabilities) | **GET** /HostNetworkSystem/{moId}/offloadCapabilities | The offload capabilities available on this server. 
[**host_network_system_get_value**](HostNetworkSystemApi.md#host_network_system_get_value) | **GET** /HostNetworkSystem/{moId}/value | List of custom field values. 
[**host_network_system_query_network_hint**](HostNetworkSystemApi.md#host_network_system_query_network_hint) | **POST** /HostNetworkSystem/{moId}/QueryNetworkHint | Requests network hint information for a physical network adapter. 
[**host_network_system_refresh_network_system**](HostNetworkSystemApi.md#host_network_system_refresh_network_system) | **POST** /HostNetworkSystem/{moId}/RefreshNetworkSystem | Refresh the network information and settings to pick up any changes that might have occurred. 
[**host_network_system_remove_port_group**](HostNetworkSystemApi.md#host_network_system_remove_port_group) | **POST** /HostNetworkSystem/{moId}/RemovePortGroup | Removes port group from the virtual switch. 
[**host_network_system_remove_service_console_virtual_nic**](HostNetworkSystemApi.md#host_network_system_remove_service_console_virtual_nic) | **POST** /HostNetworkSystem/{moId}/RemoveServiceConsoleVirtualNic | Removes a virtual service console network adapter. 
[**host_network_system_remove_virtual_nic**](HostNetworkSystemApi.md#host_network_system_remove_virtual_nic) | **POST** /HostNetworkSystem/{moId}/RemoveVirtualNic | Removes a virtual host/VMkernel network adapter. 
[**host_network_system_remove_virtual_switch**](HostNetworkSystemApi.md#host_network_system_remove_virtual_switch) | **POST** /HostNetworkSystem/{moId}/RemoveVirtualSwitch | Removes an existing virtual switch from the system. 
[**host_network_system_restart_service_console_virtual_nic**](HostNetworkSystemApi.md#host_network_system_restart_service_console_virtual_nic) | **POST** /HostNetworkSystem/{moId}/RestartServiceConsoleVirtualNic | Restart the service console virtual network adapter interface. 
[**host_network_system_set_custom_value**](HostNetworkSystemApi.md#host_network_system_set_custom_value) | **POST** /HostNetworkSystem/{moId}/setCustomValue | Assigns a value to a custom field. 
[**host_network_system_update_console_ip_route_config**](HostNetworkSystemApi.md#host_network_system_update_console_ip_route_config) | **POST** /HostNetworkSystem/{moId}/UpdateConsoleIpRouteConfig | Applies the IP route configuration for the service console. 
[**host_network_system_update_dns_config**](HostNetworkSystemApi.md#host_network_system_update_dns_config) | **POST** /HostNetworkSystem/{moId}/UpdateDnsConfig | Applies the client-side DNS configuration. 
[**host_network_system_update_ip_route_config**](HostNetworkSystemApi.md#host_network_system_update_ip_route_config) | **POST** /HostNetworkSystem/{moId}/UpdateIpRouteConfig | Applies the IP route configuration. 
[**host_network_system_update_ip_route_table_config**](HostNetworkSystemApi.md#host_network_system_update_ip_route_table_config) | **POST** /HostNetworkSystem/{moId}/UpdateIpRouteTableConfig | Applies the IP route table configuration. 
[**host_network_system_update_network_config**](HostNetworkSystemApi.md#host_network_system_update_network_config) | **POST** /HostNetworkSystem/{moId}/UpdateNetworkConfig | Applies the network configuration. 
[**host_network_system_update_physical_nic_link_speed**](HostNetworkSystemApi.md#host_network_system_update_physical_nic_link_speed) | **POST** /HostNetworkSystem/{moId}/UpdatePhysicalNicLinkSpeed | Configures link speed and duplexity. 
[**host_network_system_update_port_group**](HostNetworkSystemApi.md#host_network_system_update_port_group) | **POST** /HostNetworkSystem/{moId}/UpdatePortGroup | Reconfigures a port group on the virtual switch. 
[**host_network_system_update_service_console_virtual_nic**](HostNetworkSystemApi.md#host_network_system_update_service_console_virtual_nic) | **POST** /HostNetworkSystem/{moId}/UpdateServiceConsoleVirtualNic | Configures the IP configuration for a virtual service console network adapter. 
[**host_network_system_update_virtual_nic**](HostNetworkSystemApi.md#host_network_system_update_virtual_nic) | **POST** /HostNetworkSystem/{moId}/UpdateVirtualNic | Configures virtual host/VMkernel network adapter. 
[**host_network_system_update_virtual_switch**](HostNetworkSystemApi.md#host_network_system_update_virtual_switch) | **POST** /HostNetworkSystem/{moId}/UpdateVirtualSwitch | Updates the properties of the virtual switch. 


# **host_network_system_add_port_group**
> host_network_system_add_port_group(mo_id, add_port_group_request_type)

Adds a port group to the virtual switch. 

Adds a port group to the virtual switch.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_port_group_request_type import AddPortGroupRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_port_group_request_type = vmware_vi.AddPortGroupRequestType() # AddPortGroupRequestType | 

    try:
        # Adds a port group to the virtual switch. 
        api_instance.host_network_system_add_port_group(mo_id, add_port_group_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_add_port_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_port_group_request_type** | [**AddPortGroupRequestType**](AddPortGroupRequestType.md)|  | 

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
**500** | ***AlreadyExists***: if the port group already exists.  ***NotFound***: if the virtual switch does not exist.  ***InvalidArgument***: if the PortGroup vlanId is invalid. Valid vlanIds range from \\[0,4095\\], where 0 means no vlan tagging. Exception is also thrown if network policy is invalid.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_add_service_console_virtual_nic**
> str host_network_system_add_service_console_virtual_nic(mo_id, add_service_console_virtual_nic_request_type)

Adds a virtual service console network adapter. 

Adds a virtual service console network adapter.  Returns the device of the VirtualNic.  IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host  See also *HostNetCapabilities.usesServiceConsoleNic*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_service_console_virtual_nic_request_type import AddServiceConsoleVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_service_console_virtual_nic_request_type = vmware_vi.AddServiceConsoleVirtualNicRequestType() # AddServiceConsoleVirtualNicRequestType | 

    try:
        # Adds a virtual service console network adapter. 
        api_response = api_instance.host_network_system_add_service_console_virtual_nic(mo_id, add_service_console_virtual_nic_request_type)
        print("The response of HostNetworkSystemApi->host_network_system_add_service_console_virtual_nic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_add_service_console_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_service_console_virtual_nic_request_type** | [**AddServiceConsoleVirtualNicRequestType**](AddServiceConsoleVirtualNicRequestType.md)|  | 

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
**200** | OK  |  -  |
**500** | ***InvalidArgument***: if the IP address or subnet mask in the IP configuration are invalid or the named PortGroup does not exist.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_add_virtual_nic**
> str host_network_system_add_virtual_nic(mo_id, add_virtual_nic_request_type)

Adds a virtual host/VMkernel network adapter. 

Adds a virtual host/VMkernel network adapter.  Returns the device of the virtual network adapter.  IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_virtual_nic_request_type import AddVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_virtual_nic_request_type = vmware_vi.AddVirtualNicRequestType() # AddVirtualNicRequestType | 

    try:
        # Adds a virtual host/VMkernel network adapter. 
        api_response = api_instance.host_network_system_add_virtual_nic(mo_id, add_virtual_nic_request_type)
        print("The response of HostNetworkSystemApi->host_network_system_add_virtual_nic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_add_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_virtual_nic_request_type** | [**AddVirtualNicRequestType**](AddVirtualNicRequestType.md)|  | 

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
**200** | OK  |  -  |
**500** | ***AlreadyExists***: if the portgroup already has a virtual network adapter.  ***InvalidArgument***: if the IP address or subnet mask in the IP configuration are invalid. In the case of an ESX Server system, DHCP is not supported and this exception will be thrown if DHCP is specified. Exception may also be thrown if the named PortGroup does not exist.  ***InvalidState***: if the an ipv6 address is specified in an ipv4 only system  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_add_virtual_switch**
> host_network_system_add_virtual_switch(mo_id, add_virtual_switch_request_type)

Adds a new virtual switch to the system with the given name. 

Adds a new virtual switch to the system with the given name.  The name must be unique with respect to other virtual switches on the host and is limited to 32 characters.  See also *HostNetworkSystem.UpdateVirtualSwitch*.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_virtual_switch_request_type import AddVirtualSwitchRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_virtual_switch_request_type = vmware_vi.AddVirtualSwitchRequestType() # AddVirtualSwitchRequestType | 

    try:
        # Adds a new virtual switch to the system with the given name. 
        api_instance.host_network_system_add_virtual_switch(mo_id, add_virtual_switch_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_add_virtual_switch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_virtual_switch_request_type** | [**AddVirtualSwitchRequestType**](AddVirtualSwitchRequestType.md)|  | 

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
**500** | ***AlreadyExists***: if the virtual switch already exists.  ***InvalidArgument***: if network vswitchName exceeds the maximum allowed length, or the number of ports specified falls out of valid range, or the network policy is invalid, or beacon configuration is invalid.  ***ResourceInUse***: if the physical network adapter being bridged is already in use.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_get_available_field**
> List[CustomFieldDef] host_network_system_get_available_field(mo_id)

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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.host_network_system_get_available_field(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_available_field: %s\n" % e)
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

# **host_network_system_get_capabilities**
> HostNetCapabilities host_network_system_get_capabilities(mo_id)

Capability vector indicating the available product features. 

Capability vector indicating the available product features. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_net_capabilities import HostNetCapabilities
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Capability vector indicating the available product features. 
        api_response = api_instance.host_network_system_get_capabilities(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_capabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostNetCapabilities**](HostNetCapabilities.md)

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

# **host_network_system_get_console_ip_route_config**
> HostIpRouteConfig host_network_system_get_console_ip_route_config(mo_id)

IP route configuration for the service console. 

IP route configuration for the service console.  The IP route configuration is global to the entire host. This property is set only if IP routing can be configured for the service console. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_ip_route_config import HostIpRouteConfig
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # IP route configuration for the service console. 
        api_response = api_instance.host_network_system_get_console_ip_route_config(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_console_ip_route_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_console_ip_route_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostIpRouteConfig**](HostIpRouteConfig.md)

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

# **host_network_system_get_dns_config**
> HostDnsConfig host_network_system_get_dns_config(mo_id)

Client-side DNS configuration. 

Deprecated as of vSphere API 5.5, which is moved to each NetStackInstance. This only works on the default NetStackInstance.  Client-side DNS configuration. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_dns_config import HostDnsConfig
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Client-side DNS configuration. 
        api_response = api_instance.host_network_system_get_dns_config(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_dns_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_dns_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostDnsConfig**](HostDnsConfig.md)

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

# **host_network_system_get_ip_route_config**
> HostIpRouteConfig host_network_system_get_ip_route_config(mo_id)

The IP route configuration. 

Deprecated as of vSphere API 5.5, which is moved to each NetStackInstance. This only works on the default NetStackInstance.  The IP route configuration. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_ip_route_config import HostIpRouteConfig
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The IP route configuration. 
        api_response = api_instance.host_network_system_get_ip_route_config(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_ip_route_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_ip_route_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostIpRouteConfig**](HostIpRouteConfig.md)

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

# **host_network_system_get_network_config**
> HostNetworkConfig host_network_system_get_network_config(mo_id)

Network configuration information. 

Network configuration information.  This information can be applied using the *updateNetworkConfig()* method. The information is a strict subset of the information available in NetworkInfo.  See also *HostNetworkInfo*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_network_config import HostNetworkConfig
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Network configuration information. 
        api_response = api_instance.host_network_system_get_network_config(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_network_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_network_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostNetworkConfig**](HostNetworkConfig.md)

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

# **host_network_system_get_network_info**
> HostNetworkInfo host_network_system_get_network_info(mo_id)

The network configuration and runtime information. 

The network configuration and runtime information. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_network_info import HostNetworkInfo
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The network configuration and runtime information. 
        api_response = api_instance.host_network_system_get_network_info(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_network_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_network_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostNetworkInfo**](HostNetworkInfo.md)

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

# **host_network_system_get_offload_capabilities**
> HostNetOffloadCapabilities host_network_system_get_offload_capabilities(mo_id)

The offload capabilities available on this server. 

Deprecated as of VI API 4.0, the system defaults will be used.  The offload capabilities available on this server. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_net_offload_capabilities import HostNetOffloadCapabilities
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The offload capabilities available on this server. 
        api_response = api_instance.host_network_system_get_offload_capabilities(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_offload_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_offload_capabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostNetOffloadCapabilities**](HostNetOffloadCapabilities.md)

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

# **host_network_system_get_value**
> List[CustomFieldValue] host_network_system_get_value(mo_id)

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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.host_network_system_get_value(mo_id)
        print("The response of HostNetworkSystemApi->host_network_system_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_get_value: %s\n" % e)
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

# **host_network_system_query_network_hint**
> List[PhysicalNicHintInfo] host_network_system_query_network_hint(mo_id, query_network_hint_request_type)

Requests network hint information for a physical network adapter. 

Requests network hint information for a physical network adapter.  A network hint is some information about the network to which the physical network adapter is attached. The method receives in a list of physical network adapter devices and returns an equal number of hints if some devices are provided. If the list of devices is empty, then the method accesses hints for all physical network adapters.  See also *HostNetCapabilities.supportsNetworkHints*, *PhysicalNic.device*.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.physical_nic_hint_info import PhysicalNicHintInfo
from vmware_vi.models.query_network_hint_request_type import QueryNetworkHintRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_network_hint_request_type = vmware_vi.QueryNetworkHintRequestType() # QueryNetworkHintRequestType | 

    try:
        # Requests network hint information for a physical network adapter. 
        api_response = api_instance.host_network_system_query_network_hint(mo_id, query_network_hint_request_type)
        print("The response of HostNetworkSystemApi->host_network_system_query_network_hint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_query_network_hint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_network_hint_request_type** | [**QueryNetworkHintRequestType**](QueryNetworkHintRequestType.md)|  | 

### Return type

[**List[PhysicalNicHintInfo]**](PhysicalNicHintInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotFound***: if a specified physical network adapter does not exist.  ***InvalidArgument***: if the speed and duplexity combination is not valid for the current link driver.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_refresh_network_system**
> host_network_system_refresh_network_system(mo_id)

Refresh the network information and settings to pick up any changes that might have occurred. 

Refresh the network information and settings to pick up any changes that might have occurred.  ***Required privileges:*** Host.Config.Network 

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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Refresh the network information and settings to pick up any changes that might have occurred. 
        api_instance.host_network_system_refresh_network_system(mo_id)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_refresh_network_system: %s\n" % e)
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

# **host_network_system_remove_port_group**
> host_network_system_remove_port_group(mo_id, remove_port_group_request_type)

Removes port group from the virtual switch. 

Removes port group from the virtual switch.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_port_group_request_type import RemovePortGroupRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_port_group_request_type = vmware_vi.RemovePortGroupRequestType() # RemovePortGroupRequestType | 

    try:
        # Removes port group from the virtual switch. 
        api_instance.host_network_system_remove_port_group(mo_id, remove_port_group_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_remove_port_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_port_group_request_type** | [**RemovePortGroupRequestType**](RemovePortGroupRequestType.md)|  | 

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
**500** | ***NotFound***: if the port group or virtual switch does not exist.  ***ResourceInUse***: if the port group can not be removed because there are virtual network adapters associated with it.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_remove_service_console_virtual_nic**
> host_network_system_remove_service_console_virtual_nic(mo_id, remove_service_console_virtual_nic_request_type)

Removes a virtual service console network adapter. 

Removes a virtual service console network adapter.  See also *HostNetCapabilities.usesServiceConsoleNic*.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_service_console_virtual_nic_request_type import RemoveServiceConsoleVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_service_console_virtual_nic_request_type = vmware_vi.RemoveServiceConsoleVirtualNicRequestType() # RemoveServiceConsoleVirtualNicRequestType | 

    try:
        # Removes a virtual service console network adapter. 
        api_instance.host_network_system_remove_service_console_virtual_nic(mo_id, remove_service_console_virtual_nic_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_remove_service_console_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_service_console_virtual_nic_request_type** | [**RemoveServiceConsoleVirtualNicRequestType**](RemoveServiceConsoleVirtualNicRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual network adapter cannot be found.  ***NotSupported***: if the host is not an ESX Server system.  ***ResourceInUse***: if the network adapter is currently used by DHCP DNS.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_remove_virtual_nic**
> host_network_system_remove_virtual_nic(mo_id, remove_virtual_nic_request_type)

Removes a virtual host/VMkernel network adapter. 

Removes a virtual host/VMkernel network adapter.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_virtual_nic_request_type import RemoveVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_virtual_nic_request_type = vmware_vi.RemoveVirtualNicRequestType() # RemoveVirtualNicRequestType | 

    try:
        # Removes a virtual host/VMkernel network adapter. 
        api_instance.host_network_system_remove_virtual_nic(mo_id, remove_virtual_nic_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_remove_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_virtual_nic_request_type** | [**RemoveVirtualNicRequestType**](RemoveVirtualNicRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual network adapter cannot be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_remove_virtual_switch**
> host_network_system_remove_virtual_switch(mo_id, remove_virtual_switch_request_type)

Removes an existing virtual switch from the system. 

Removes an existing virtual switch from the system.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_virtual_switch_request_type import RemoveVirtualSwitchRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_virtual_switch_request_type = vmware_vi.RemoveVirtualSwitchRequestType() # RemoveVirtualSwitchRequestType | 

    try:
        # Removes an existing virtual switch from the system. 
        api_instance.host_network_system_remove_virtual_switch(mo_id, remove_virtual_switch_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_remove_virtual_switch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_virtual_switch_request_type** | [**RemoveVirtualSwitchRequestType**](RemoveVirtualSwitchRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual switch does not exist.  ***ResourceInUse***: if there are virtual network adapters associated with the virtual switch.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_restart_service_console_virtual_nic**
> host_network_system_restart_service_console_virtual_nic(mo_id, restart_service_console_virtual_nic_request_type)

Restart the service console virtual network adapter interface. 

Restart the service console virtual network adapter interface.  If the service console virtual network adapter uses DHCP, restarting the interface may result it with a different IP configuration, or even fail to be brought up depending on the host system network configuration.  See also *HostNetCapabilities.usesServiceConsoleNic*.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.restart_service_console_virtual_nic_request_type import RestartServiceConsoleVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    restart_service_console_virtual_nic_request_type = vmware_vi.RestartServiceConsoleVirtualNicRequestType() # RestartServiceConsoleVirtualNicRequestType | 

    try:
        # Restart the service console virtual network adapter interface. 
        api_instance.host_network_system_restart_service_console_virtual_nic(mo_id, restart_service_console_virtual_nic_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_restart_service_console_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **restart_service_console_virtual_nic_request_type** | [**RestartServiceConsoleVirtualNicRequestType**](RestartServiceConsoleVirtualNicRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual network adapter cannot be found.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_set_custom_value**
> host_network_system_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.host_network_system_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_set_custom_value: %s\n" % e)
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

# **host_network_system_update_console_ip_route_config**
> host_network_system_update_console_ip_route_config(mo_id, update_console_ip_route_config_request_type)

Applies the IP route configuration for the service console. 

Applies the IP route configuration for the service console.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_console_ip_route_config_request_type import UpdateConsoleIpRouteConfigRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_console_ip_route_config_request_type = vmware_vi.UpdateConsoleIpRouteConfigRequestType() # UpdateConsoleIpRouteConfigRequestType | 

    try:
        # Applies the IP route configuration for the service console. 
        api_instance.host_network_system_update_console_ip_route_config(mo_id, update_console_ip_route_config_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_console_ip_route_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_console_ip_route_config_request_type** | [**UpdateConsoleIpRouteConfigRequestType**](UpdateConsoleIpRouteConfigRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if any of the IP addresses are invalid.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_dns_config**
> host_network_system_update_dns_config(mo_id, update_dns_config_request_type)

Applies the client-side DNS configuration. 

Deprecated as of vSphere API 5.5, which is moved to each NetStackInstance. This API only works on the default NetStackInstance.  Applies the client-side DNS configuration.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_dns_config_request_type import UpdateDnsConfigRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_dns_config_request_type = vmware_vi.UpdateDnsConfigRequestType() # UpdateDnsConfigRequestType | 

    try:
        # Applies the client-side DNS configuration. 
        api_instance.host_network_system_update_dns_config(mo_id, update_dns_config_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_dns_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_dns_config_request_type** | [**UpdateDnsConfigRequestType**](UpdateDnsConfigRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if any of the IP addresses are invalid, or for a DHCP DNS, if the DHCP virtual network adapter is not specified or the virtual network adapter specified is not DHCP enabled.  ***NotFound***: when the DHCP virtual network adapter specified does not exist.  ***NotSupported***: if the host is not an ESX Server system.  ***HostInDomain***: if an attempt is made to change the host or domain name while the host is part of a Windows domain.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_ip_route_config**
> host_network_system_update_ip_route_config(mo_id, update_ip_route_config_request_type)

Applies the IP route configuration. 

Deprecated as of vSphere API 5.5, which is moved to each NetStackInstance. This API only works on the default NetStackInstance.  Applies the IP route configuration.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_ip_route_config_request_type import UpdateIpRouteConfigRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_ip_route_config_request_type = vmware_vi.UpdateIpRouteConfigRequestType() # UpdateIpRouteConfigRequestType | 

    try:
        # Applies the IP route configuration. 
        api_instance.host_network_system_update_ip_route_config(mo_id, update_ip_route_config_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_ip_route_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_ip_route_config_request_type** | [**UpdateIpRouteConfigRequestType**](UpdateIpRouteConfigRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if any of the IP addresses are invalid.  ***InvalidState***: if the an ipv6 address is specified in an ipv4 only system  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_ip_route_table_config**
> host_network_system_update_ip_route_table_config(mo_id, update_ip_route_table_config_request_type)

Applies the IP route table configuration. 

Deprecated as of vSphere API 5.5, which is moved to each NetStackInstance. This API only works on the default NetStackInstance.  Applies the IP route table configuration.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_ip_route_table_config_request_type import UpdateIpRouteTableConfigRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_ip_route_table_config_request_type = vmware_vi.UpdateIpRouteTableConfigRequestType() # UpdateIpRouteTableConfigRequestType | 

    try:
        # Applies the IP route table configuration. 
        api_instance.host_network_system_update_ip_route_table_config(mo_id, update_ip_route_table_config_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_ip_route_table_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_ip_route_table_config_request_type** | [**UpdateIpRouteTableConfigRequestType**](UpdateIpRouteTableConfigRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if any of the IP addresses are invalid.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_network_config**
> HostNetworkConfigResult host_network_system_update_network_config(mo_id, update_network_config_request_type)

Applies the network configuration. 

Applies the network configuration.  This method operates primarily in two modes: **replace** or **modify** mode.  **replace**   When called in **replace** mode, this method applies the fully specified networking configuration to the networking system.  Upon successful completion of the call, the state of networking will match the configuration specified in **config**. In general, objects are created or destroyed to match the elements in the array of configurations. The identifier field in each element in an array of configurations is used to match an existing network entity. The state of existing network entities is patched to match that of the configuration.  An exception to this approach applies to the array of PhysicalNic.Config objects. The cardinality of physical network adapters cannot be changed through this operation. Thus, the identifier of every element in the array must match an existing PhysicalNic. If there are fewer elements in the array than there are existing PhysicalNics, then no change is made on the unreferenced PhysicalNic objects.  If the call fails, the networking error is returned as an exception and the state of networking reverts to the state prior to the start of the call.  **modify** When called in **modify** mode, only changes that are specified are made. For singleton entities like DnsConfig, the state is changed only if the data object is set. For array elements, there is an Operation field that indicates if the element should be added, removed, or edited. In the case of editing or removal, the entity must exist or an exception is thrown. In the case of adding, a specification needs to be provided.  It returns device names of vmkernel and service console virtual network adapter added to the system.  Currently, the only mode that is implemented is incremental mode. Only add operations are supported for instances. Singleton configuration is not supported. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host  See also *HostConfigChangeMode_enum*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_network_config_result import HostNetworkConfigResult
from vmware_vi.models.update_network_config_request_type import UpdateNetworkConfigRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_network_config_request_type = vmware_vi.UpdateNetworkConfigRequestType() # UpdateNetworkConfigRequestType | 

    try:
        # Applies the network configuration. 
        api_response = api_instance.host_network_system_update_network_config(mo_id, update_network_config_request_type)
        print("The response of HostNetworkSystemApi->host_network_system_update_network_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_network_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_network_config_request_type** | [**UpdateNetworkConfigRequestType**](UpdateNetworkConfigRequestType.md)|  | 

### Return type

[**HostNetworkConfigResult**](HostNetworkConfigResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***AlreadyExists***: when a network entity specified in the configuration already exists.  ***NotFound***: when a network entity specified in the configuration already exists.  ***InvalidArgument***: if an invalid parameter is passed in for one of the networking objects.  ***NotSupported***: if modify mode is not used, a remove or set operation is specified for an instance, or a singleton entity is configured.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_physical_nic_link_speed**
> host_network_system_update_physical_nic_link_speed(mo_id, update_physical_nic_link_speed_request_type)

Configures link speed and duplexity. 

Configures link speed and duplexity.  If linkSpeed is not specified, physical network adapter will be set to autonegotiate.  See also *HostNetCapabilities.canSetPhysicalNicLinkSpeed*.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_physical_nic_link_speed_request_type import UpdatePhysicalNicLinkSpeedRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_physical_nic_link_speed_request_type = vmware_vi.UpdatePhysicalNicLinkSpeedRequestType() # UpdatePhysicalNicLinkSpeedRequestType | 

    try:
        # Configures link speed and duplexity. 
        api_instance.host_network_system_update_physical_nic_link_speed(mo_id, update_physical_nic_link_speed_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_physical_nic_link_speed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_physical_nic_link_speed_request_type** | [**UpdatePhysicalNicLinkSpeedRequestType**](UpdatePhysicalNicLinkSpeedRequestType.md)|  | 

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
**500** | ***NotFound***: if the physical network adapter does not exist.  ***NotSupported***: if the host is not an ESX Server system.  ***InvalidArgument***: if the speed and duplexity is not one of the valid configurations.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_port_group**
> host_network_system_update_port_group(mo_id, update_port_group_request_type)

Reconfigures a port group on the virtual switch. 

Reconfigures a port group on the virtual switch.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_port_group_request_type import UpdatePortGroupRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_port_group_request_type = vmware_vi.UpdatePortGroupRequestType() # UpdatePortGroupRequestType | 

    try:
        # Reconfigures a port group on the virtual switch. 
        api_instance.host_network_system_update_port_group(mo_id, update_port_group_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_port_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_port_group_request_type** | [**UpdatePortGroupRequestType**](UpdatePortGroupRequestType.md)|  | 

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
**500** | ***AlreadyExists***: if the update causes the port group to conflict with an existing port group.  ***NotFound***: if the port group or virtual switch does not exist.  ***InvalidArgument***: if the PortGroup vlanId is invalid. Valid vlanIds range from \\[0,4095\\], where 0 means no vlan tagging. Exception is also thrown if network policy is invalid.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_service_console_virtual_nic**
> host_network_system_update_service_console_virtual_nic(mo_id, update_service_console_virtual_nic_request_type)

Configures the IP configuration for a virtual service console network adapter. 

Configures the IP configuration for a virtual service console network adapter.  IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will check that the users have Network.Assign privilege on the DVPortGroup or the DVS if the port resides on a DVPortGroup or is a stand-alone DVS port.  See also *HostNetCapabilities.usesServiceConsoleNic*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_service_console_virtual_nic_request_type import UpdateServiceConsoleVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_service_console_virtual_nic_request_type = vmware_vi.UpdateServiceConsoleVirtualNicRequestType() # UpdateServiceConsoleVirtualNicRequestType | 

    try:
        # Configures the IP configuration for a virtual service console network adapter. 
        api_instance.host_network_system_update_service_console_virtual_nic(mo_id, update_service_console_virtual_nic_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_service_console_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_service_console_virtual_nic_request_type** | [**UpdateServiceConsoleVirtualNicRequestType**](UpdateServiceConsoleVirtualNicRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual network adapter cannot be found.  ***InvalidArgument***: if the IP address or subnet mask in the IP configuration are invalid or the named PortGroup does not exist.  ***NotSupported***: if the host is not an ESX Server system.  ***ResourceInUse***: if tries to turn of DHCP while the network adapter is currently used by DHCP DNS.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_virtual_nic**
> host_network_system_update_virtual_nic(mo_id, update_virtual_nic_request_type)

Configures virtual host/VMkernel network adapter. 

Configures virtual host/VMkernel network adapter.  IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_virtual_nic_request_type import UpdateVirtualNicRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_virtual_nic_request_type = vmware_vi.UpdateVirtualNicRequestType() # UpdateVirtualNicRequestType | 

    try:
        # Configures virtual host/VMkernel network adapter. 
        api_instance.host_network_system_update_virtual_nic(mo_id, update_virtual_nic_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_virtual_nic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_virtual_nic_request_type** | [**UpdateVirtualNicRequestType**](UpdateVirtualNicRequestType.md)|  | 

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
**500** | ***NotFound***: if the virtual network adapter cannot be found.  ***InvalidArgument***: if the IP address or subnet mask in the IP configuration are invalid. In the case of an ESX Server system, DHCP is not supported and this exception is thrown if DHCP is specified. Exception may also be thrown if the named PortGroup does not exist.  ***InvalidState***: if the an ipv6 address is specified in an ipv4 only system  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_network_system_update_virtual_switch**
> host_network_system_update_virtual_switch(mo_id, update_virtual_switch_request_type)

Updates the properties of the virtual switch. 

Updates the properties of the virtual switch.  If the bridge is NULL, the configuration will be unset.  If a network adapter is listed in the active or standby list, then changing the set of network adapters to which the physical network adapter is associated may have a side effect of changing the network adapter order policy. If a network adapter is removed from the bridge configuration, then the network adapter is removed from the network adapter teaming order.  The BondBridge configuration is the only valid bridge configuration for an ESX Server system.  See also *HostNicOrderPolicy*.  ***Required privileges:*** Host.Config.Network 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_virtual_switch_request_type import UpdateVirtualSwitchRequestType
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
    api_instance = vmware_vi.HostNetworkSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_virtual_switch_request_type = vmware_vi.UpdateVirtualSwitchRequestType() # UpdateVirtualSwitchRequestType | 

    try:
        # Updates the properties of the virtual switch. 
        api_instance.host_network_system_update_virtual_switch(mo_id, update_virtual_switch_request_type)
    except Exception as e:
        print("Exception when calling HostNetworkSystemApi->host_network_system_update_virtual_switch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_virtual_switch_request_type** | [**UpdateVirtualSwitchRequestType**](UpdateVirtualSwitchRequestType.md)|  | 

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
**500** | ***ResourceInUse***: if the physical network adapter being bridged is already in use.  ***NotFound***: if the virtual switch does not exist.  ***InvalidArgument***: if the bridge parameter is bad or the network policy is invalid or does not exist or the number of ports specified falls out of valid range, or the beacon configuration is invalid.  ***NotSupported***: if network adapter teaming policy is set but is not supported.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

