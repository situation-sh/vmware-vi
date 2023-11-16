# vmware_vi.HostNvdimmSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_nvdimm_system_create_nvdimm_namespace_task**](HostNvdimmSystemApi.md#host_nvdimm_system_create_nvdimm_namespace_task) | **POST** /HostNvdimmSystem/{moId}/CreateNvdimmNamespace_Task | A new block or persistent namespace can be created on the NVDIMM(s) when the system is in maintenance mode. 
[**host_nvdimm_system_create_nvdimm_p_mem_namespace_task**](HostNvdimmSystemApi.md#host_nvdimm_system_create_nvdimm_p_mem_namespace_task) | **POST** /HostNvdimmSystem/{moId}/CreateNvdimmPMemNamespace_Task | Create persistent memory mode nvd namespace from information passed in PMemNamespaceCreationSpec. 
[**host_nvdimm_system_delete_nvdimm_block_namespaces_task**](HostNvdimmSystemApi.md#host_nvdimm_system_delete_nvdimm_block_namespaces_task) | **POST** /HostNvdimmSystem/{moId}/DeleteNvdimmBlockNamespaces_Task | Delete all block mode namespaces in the system. 
[**host_nvdimm_system_delete_nvdimm_namespace_task**](HostNvdimmSystemApi.md#host_nvdimm_system_delete_nvdimm_namespace_task) | **POST** /HostNvdimmSystem/{moId}/DeleteNvdimmNamespace_Task | Delete nvd namespace whose uuid matches passed parameter. 
[**host_nvdimm_system_get_nvdimm_system_info**](HostNvdimmSystemApi.md#host_nvdimm_system_get_nvdimm_system_info) | **GET** /HostNvdimmSystem/{moId}/nvdimmSystemInfo | Host NVDIMM information. 


# **host_nvdimm_system_create_nvdimm_namespace_task**
> ManagedObjectReference host_nvdimm_system_create_nvdimm_namespace_task(mo_id, create_nvdimm_namespace_request_type)

A new block or persistent namespace can be created on the NVDIMM(s) when the system is in maintenance mode. 

Deprecated as of vSphere 6.7u1, use createPMemNamespace Create nvd namespace from information passed in NamespaceCreationSpec.  A new block or persistent namespace can be created on the NVDIMM(s) when the system is in maintenance mode.  If all the parameters passed are valid and system is in maintenance mode, then a DSM (Device Specific Method) call is made to create the namespace. DSM calls are blockable and slow operations and hence the use of task.  If a new namespace is created, its UUID is returned.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Host.Config.Nvdimm 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_nvdimm_namespace_request_type import CreateNvdimmNamespaceRequestType
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
    api_instance = vmware_vi.HostNvdimmSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_nvdimm_namespace_request_type = vmware_vi.CreateNvdimmNamespaceRequestType() # CreateNvdimmNamespaceRequestType | 

    try:
        # A new block or persistent namespace can be created on the NVDIMM(s) when the system is in maintenance mode. 
        api_response = api_instance.host_nvdimm_system_create_nvdimm_namespace_task(mo_id, create_nvdimm_namespace_request_type)
        print("The response of HostNvdimmSystemApi->host_nvdimm_system_create_nvdimm_namespace_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNvdimmSystemApi->host_nvdimm_system_create_nvdimm_namespace_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_nvdimm_namespace_request_type** | [**CreateNvdimmNamespaceRequestType**](CreateNvdimmNamespaceRequestType.md)|  | 

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
**200** | This method returns a *Task* object which is used to monitor this operation. The task result (*Task.info*.*TaskInfo.result*) contains a *NvdimmGuid* object that has the UUID of the newly created namespace.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if an argument to create namespace is invalid.  ***NotSupported***: if no NVDIMMs are found, namespace type is not supported or if operation does not have DSM method.  ***InvalidHostState***: if operation is not allowed as system is not in maintenance mode.  ***AlreadyExists***: if the namespace of type already exists.  ***SystemError***: for other system errors along with localized reason for failure.  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_nvdimm_system_create_nvdimm_p_mem_namespace_task**
> ManagedObjectReference host_nvdimm_system_create_nvdimm_p_mem_namespace_task(mo_id, create_nvdimm_p_mem_namespace_request_type)

Create persistent memory mode nvd namespace from information passed in PMemNamespaceCreationSpec. 

Create persistent memory mode nvd namespace from information passed in PMemNamespaceCreationSpec.  A new persistent namespace can be created on the NVDIMM(s) when the system is in maintenance mode. If all the parameters passed are valid and system is in maintenance mode, then a DSM (Device Specific Method) call is made to create the namespace. DSM calls are blockable and slow operations and hence the use of task.  If a new namespace is created, its UUID is returned.  ***Since:*** vSphere API 6.7.1  ***Required privileges:*** Host.Config.Nvdimm 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_nvdimm_p_mem_namespace_request_type import CreateNvdimmPMemNamespaceRequestType
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
    api_instance = vmware_vi.HostNvdimmSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_nvdimm_p_mem_namespace_request_type = vmware_vi.CreateNvdimmPMemNamespaceRequestType() # CreateNvdimmPMemNamespaceRequestType | 

    try:
        # Create persistent memory mode nvd namespace from information passed in PMemNamespaceCreationSpec. 
        api_response = api_instance.host_nvdimm_system_create_nvdimm_p_mem_namespace_task(mo_id, create_nvdimm_p_mem_namespace_request_type)
        print("The response of HostNvdimmSystemApi->host_nvdimm_system_create_nvdimm_p_mem_namespace_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNvdimmSystemApi->host_nvdimm_system_create_nvdimm_p_mem_namespace_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_nvdimm_p_mem_namespace_request_type** | [**CreateNvdimmPMemNamespaceRequestType**](CreateNvdimmPMemNamespaceRequestType.md)|  | 

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
**200** | This method returns a *Task* object which is used to monitor this operation. The task result (*Task.info*.*TaskInfo.result*) contains a *NvdimmGuid* object that has the UUID of the newly created namespace.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if an argument to create namespace is invalid.  ***NotSupported***: if no NVDIMMs are found or if operation does not have the supporting DSM method.  ***InvalidHostState***: if operation is not allowed as system is not in maintenance mode.  ***AlreadyExists***: if the namespace of type already exists.  ***SystemError***: for other system errors along with localized reason for failure.  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_nvdimm_system_delete_nvdimm_block_namespaces_task**
> ManagedObjectReference host_nvdimm_system_delete_nvdimm_block_namespaces_task(mo_id)

Delete all block mode namespaces in the system. 

Delete all block mode namespaces in the system.  Existing block namespace(s) can be deleted from all NVDIMMs, if the system is in maintenance mode. If paramters passed are valid and the system is in maintenance mode, then DSM calls are made to delete these namespaces. DSM calls are blockable, slow operations and hence the use of task.  If a particular block namespace is to be deleted, use *HostNvdimmSystem.DeleteNvdimmNamespace_Task* by passing it the UUID of the block namespace.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Host.Config.Nvdimm 

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
    api_instance = vmware_vi.HostNvdimmSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Delete all block mode namespaces in the system. 
        api_response = api_instance.host_nvdimm_system_delete_nvdimm_block_namespaces_task(mo_id)
        print("The response of HostNvdimmSystemApi->host_nvdimm_system_delete_nvdimm_block_namespaces_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNvdimmSystemApi->host_nvdimm_system_delete_nvdimm_block_namespaces_task: %s\n" % e)
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
**200** | This method returns a *Task* object which is used to monitor this operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if UUID of namespace to be created is invalid.  ***NotFound***: if the namespace to be deleted is not found.  ***NotSupported***: if no NVDIMMs are found and if operation does not have DSM method.  ***InvalidHostState***: if operation is not allowed as system is not in maintenance mode.  ***SystemError***: for any other system error along with localized reason for failure.  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_nvdimm_system_delete_nvdimm_namespace_task**
> ManagedObjectReference host_nvdimm_system_delete_nvdimm_namespace_task(mo_id, delete_nvdimm_namespace_request_type)

Delete nvd namespace whose uuid matches passed parameter. 

Delete nvd namespace whose uuid matches passed parameter.  An existing namespace of type block or persistent mode can be deleted from NVDIMM(s), if the system is in maintenance mode. If paramters passed are valid and the system is in maintenance mode, then a DSM call is made to delete this namespace. DSM calls are blockable, slow operations and hence the use of task.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Host.Config.Nvdimm 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_nvdimm_namespace_request_type import DeleteNvdimmNamespaceRequestType
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
    api_instance = vmware_vi.HostNvdimmSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_nvdimm_namespace_request_type = vmware_vi.DeleteNvdimmNamespaceRequestType() # DeleteNvdimmNamespaceRequestType | 

    try:
        # Delete nvd namespace whose uuid matches passed parameter. 
        api_response = api_instance.host_nvdimm_system_delete_nvdimm_namespace_task(mo_id, delete_nvdimm_namespace_request_type)
        print("The response of HostNvdimmSystemApi->host_nvdimm_system_delete_nvdimm_namespace_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNvdimmSystemApi->host_nvdimm_system_delete_nvdimm_namespace_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_nvdimm_namespace_request_type** | [**DeleteNvdimmNamespaceRequestType**](DeleteNvdimmNamespaceRequestType.md)|  | 

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
**200** | This method returns a *Task* object which is used to monitor this operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if UUID of namespace to be created is invalid.  ***NotFound***: if the namespace to be deleted is not found.  ***NotSupported***: if no NVDIMMs are found or if operation does not have DSM method.  ***InvalidHostState***: if operation is not allowed as system is not in maintenance mode.  ***SystemError***: for any other system error along with localized reason for failure.  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_nvdimm_system_get_nvdimm_system_info**
> NvdimmSystemInfo host_nvdimm_system_get_nvdimm_system_info(mo_id)

Host NVDIMM information. 

Host NVDIMM information.  \\- Summary of all dimms on the host. \\- Array of all DIMMs on the host. \\- Array of DIMM information and health for all dimms on the host. \\- Array of interleave set for all sets on the host. \\- Array of interleave set information for all sets on the host. \\- Array of namespace IDs for all dimms on the host. \\- Array of namespace details of all dimms on the host.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Host.Config.Nvdimm 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.nvdimm_system_info import NvdimmSystemInfo
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
    api_instance = vmware_vi.HostNvdimmSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Host NVDIMM information. 
        api_response = api_instance.host_nvdimm_system_get_nvdimm_system_info(mo_id)
        print("The response of HostNvdimmSystemApi->host_nvdimm_system_get_nvdimm_system_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostNvdimmSystemApi->host_nvdimm_system_get_nvdimm_system_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**NvdimmSystemInfo**](NvdimmSystemInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return set of all NVDIMM related information.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

