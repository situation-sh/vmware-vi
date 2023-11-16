# vmware_vi.EnvironmentBrowserApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_browser_get_datastore_browser**](EnvironmentBrowserApi.md#environment_browser_get_datastore_browser) | **GET** /EnvironmentBrowser/{moId}/datastoreBrowser | DatastoreBrowser to browse datastores that are available on this entity. 
[**environment_browser_query_config_option**](EnvironmentBrowserApi.md#environment_browser_query_config_option) | **POST** /EnvironmentBrowser/{moId}/QueryConfigOption | Query for a specific virtual machine configuration option (the ConfigOption). 
[**environment_browser_query_config_option_descriptor**](EnvironmentBrowserApi.md#environment_browser_query_config_option_descriptor) | **POST** /EnvironmentBrowser/{moId}/QueryConfigOptionDescriptor | The list of ConfigOption keys available on this entity. 
[**environment_browser_query_config_option_ex**](EnvironmentBrowserApi.md#environment_browser_query_config_option_ex) | **POST** /EnvironmentBrowser/{moId}/QueryConfigOptionEx | Query for a virtual machine configuration *option* matching the key or host or both given in the *EnvironmentBrowserConfigOptionQuerySpec*. 
[**environment_browser_query_config_target**](EnvironmentBrowserApi.md#environment_browser_query_config_target) | **POST** /EnvironmentBrowser/{moId}/QueryConfigTarget | Queries for information about a specific target, a \&quot;physical\&quot; device that can be used to back virtual devices. 
[**environment_browser_query_target_capabilities**](EnvironmentBrowserApi.md#environment_browser_query_target_capabilities) | **POST** /EnvironmentBrowser/{moId}/QueryTargetCapabilities | Queries for information on the capabilities supported by the ComputeResource associated with the EnvironmentBrowser. 


# **environment_browser_get_datastore_browser**
> ManagedObjectReference environment_browser_get_datastore_browser(mo_id)

DatastoreBrowser to browse datastores that are available on this entity. 

DatastoreBrowser to browse datastores that are available on this entity.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # DatastoreBrowser to browse datastores that are available on this entity. 
        api_response = api_instance.environment_browser_get_datastore_browser(mo_id)
        print("The response of EnvironmentBrowserApi->environment_browser_get_datastore_browser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_get_datastore_browser: %s\n" % e)
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
**200** | Refers instance of *HostDatastoreBrowser*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_browser_query_config_option**
> VirtualMachineConfigOption environment_browser_query_config_option(mo_id, query_config_option_request_type)

Query for a specific virtual machine configuration option (the ConfigOption). 

Query for a specific virtual machine configuration option (the ConfigOption).  If the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, the key or host, or both arguments can be used to return the required config options. If a key is specified, then the ConfigOption corresponding to that key value is returned. If a host is specified, then the default ConfigOption for that host is returned. If key and host both are specified, the ConfigOption corresponding to the given key for that host is returned. If neither is specified, then the default ConfigOption for this environment browser is returned. Typically, the default contains the options for the most recent virtual hardware supported.  If the EnvironmentBrowser is from a VirtualMachine neither a host nor a key should be specified.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_config_option_request_type import QueryConfigOptionRequestType
from vmware_vi.models.virtual_machine_config_option import VirtualMachineConfigOption
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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_config_option_request_type = vmware_vi.QueryConfigOptionRequestType() # QueryConfigOptionRequestType | 

    try:
        # Query for a specific virtual machine configuration option (the ConfigOption). 
        api_response = api_instance.environment_browser_query_config_option(mo_id, query_config_option_request_type)
        print("The response of EnvironmentBrowserApi->environment_browser_query_config_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_query_config_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_config_option_request_type** | [**QueryConfigOptionRequestType**](QueryConfigOptionRequestType.md)|  | 

### Return type

[**VirtualMachineConfigOption**](VirtualMachineConfigOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the ConfigOption object. If invoked on a cluster with no hosts, or if the ConfigOption with given key is not found for the given host, null is returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_browser_query_config_option_descriptor**
> List[VirtualMachineConfigOptionDescriptor] environment_browser_query_config_option_descriptor(mo_id)

The list of ConfigOption keys available on this entity. 

The list of ConfigOption keys available on this entity.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_config_option_descriptor import VirtualMachineConfigOptionDescriptor
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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of ConfigOption keys available on this entity. 
        api_response = api_instance.environment_browser_query_config_option_descriptor(mo_id)
        print("The response of EnvironmentBrowserApi->environment_browser_query_config_option_descriptor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_query_config_option_descriptor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VirtualMachineConfigOptionDescriptor]**](VirtualMachineConfigOptionDescriptor.md)

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

# **environment_browser_query_config_option_ex**
> VirtualMachineConfigOption environment_browser_query_config_option_ex(mo_id, query_config_option_ex_request_type)

Query for a virtual machine configuration *option* matching the key or host or both given in the *EnvironmentBrowserConfigOptionQuerySpec*. 

Query for a virtual machine configuration *option* matching the key or host or both given in the *EnvironmentBrowserConfigOptionQuerySpec*.  For more details see *EnvironmentBrowser.QueryConfigOption*  If the Environment Browser belongs to a virtual machine and the spec argument is omitted, the method returns the ConfigOption object corresponding to the vmx version of the virutal machine and the *guestOSDescriptor* list contains only the guestId of the virutal machine.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_config_option_ex_request_type import QueryConfigOptionExRequestType
from vmware_vi.models.virtual_machine_config_option import VirtualMachineConfigOption
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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_config_option_ex_request_type = vmware_vi.QueryConfigOptionExRequestType() # QueryConfigOptionExRequestType | 

    try:
        # Query for a virtual machine configuration *option* matching the key or host or both given in the *EnvironmentBrowserConfigOptionQuerySpec*. 
        api_response = api_instance.environment_browser_query_config_option_ex(mo_id, query_config_option_ex_request_type)
        print("The response of EnvironmentBrowserApi->environment_browser_query_config_option_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_query_config_option_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_config_option_ex_request_type** | [**QueryConfigOptionExRequestType**](QueryConfigOptionExRequestType.md)|  | 

### Return type

[**VirtualMachineConfigOption**](VirtualMachineConfigOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the *VirtualMachineConfigOption* object. If invoked on a cluster with no hosts, or if the *VirtualMachineConfigOption* with given key is not found for the given host, null is returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_browser_query_config_target**
> ConfigTarget environment_browser_query_config_target(mo_id, query_config_target_request_type)

Queries for information about a specific target, a \"physical\" device that can be used to back virtual devices. 

Queries for information about a specific target, a \"physical\" device that can be used to back virtual devices.  The ConfigTarget that is returned specifies the set of values that can be used in the device backings to connect the virtual machine to physical (or logical) host devices.  If the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, the host argument can be used to return the ConfigTarget provided by a particular host in the compute resource or cluster. If host is not specified and the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, then the union of all the devices is returned and the vim.vm.TargetInfo.configurationTag field indicates how widely the device is available across the compute resource or cluster.  If the EnvironmentBrowser is from a VirtualMachine a host should not be specified.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.config_target import ConfigTarget
from vmware_vi.models.query_config_target_request_type import QueryConfigTargetRequestType
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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_config_target_request_type = vmware_vi.QueryConfigTargetRequestType() # QueryConfigTargetRequestType | 

    try:
        # Queries for information about a specific target, a \"physical\" device that can be used to back virtual devices. 
        api_response = api_instance.environment_browser_query_config_target(mo_id, query_config_target_request_type)
        print("The response of EnvironmentBrowserApi->environment_browser_query_config_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_query_config_target: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_config_target_request_type** | [**QueryConfigTargetRequestType**](QueryConfigTargetRequestType.md)|  | 

### Return type

[**ConfigTarget**](ConfigTarget.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the ConfigTarget object. If invoked on a cluster with no hosts, null is returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_browser_query_target_capabilities**
> HostCapability environment_browser_query_target_capabilities(mo_id, query_target_capabilities_request_type)

Queries for information on the capabilities supported by the ComputeResource associated with the EnvironmentBrowser. 

Queries for information on the capabilities supported by the ComputeResource associated with the EnvironmentBrowser.  If the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, the host argument can be used to return the capabilities associated with a specific host in the compute resource or cluster. If the host argument is not specified and the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, then the intersection of the capabilities supported by all the hosts in the cluster is returned. If the EnvironmentBrowser is from a VirtualMachine, the compute resource associated with the virtual machine will be queried for its capabilities.  If the EnvironmentBrowser is from a VirtualMachine a host should not be specified.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_capability import HostCapability
from vmware_vi.models.query_target_capabilities_request_type import QueryTargetCapabilitiesRequestType
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
    api_instance = vmware_vi.EnvironmentBrowserApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_target_capabilities_request_type = vmware_vi.QueryTargetCapabilitiesRequestType() # QueryTargetCapabilitiesRequestType | 

    try:
        # Queries for information on the capabilities supported by the ComputeResource associated with the EnvironmentBrowser. 
        api_response = api_instance.environment_browser_query_target_capabilities(mo_id, query_target_capabilities_request_type)
        print("The response of EnvironmentBrowserApi->environment_browser_query_target_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentBrowserApi->environment_browser_query_target_capabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_target_capabilities_request_type** | [**QueryTargetCapabilitiesRequestType**](QueryTargetCapabilitiesRequestType.md)|  | 

### Return type

[**HostCapability**](HostCapability.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the set of capabilities supported by the ComputeResource associated with the EnvironmentBrowser. If invoked on a cluster with no hosts, null is returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

