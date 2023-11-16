# vmware_vi.HostDatastoreSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_datastore_system_configure_datastore_principal**](HostDatastoreSystemApi.md#host_datastore_system_configure_datastore_principal) | **POST** /HostDatastoreSystem/{moId}/ConfigureDatastorePrincipal | Configures datastore principal user for the host. 
[**host_datastore_system_create_local_datastore**](HostDatastoreSystemApi.md#host_datastore_system_create_local_datastore) | **POST** /HostDatastoreSystem/{moId}/CreateLocalDatastore | Creates a new local datastore. 
[**host_datastore_system_create_nas_datastore**](HostDatastoreSystemApi.md#host_datastore_system_create_nas_datastore) | **POST** /HostDatastoreSystem/{moId}/CreateNasDatastore | Creates a new network-attached storage datastore. 
[**host_datastore_system_create_vmfs_datastore**](HostDatastoreSystemApi.md#host_datastore_system_create_vmfs_datastore) | **POST** /HostDatastoreSystem/{moId}/CreateVmfsDatastore | Creates a new VMFS datastore. 
[**host_datastore_system_create_vvol_datastore**](HostDatastoreSystemApi.md#host_datastore_system_create_vvol_datastore) | **POST** /HostDatastoreSystem/{moId}/CreateVvolDatastore | Create a Virtual-Volume based datastore 
[**host_datastore_system_disable_clustered_vmdk_support**](HostDatastoreSystemApi.md#host_datastore_system_disable_clustered_vmdk_support) | **POST** /HostDatastoreSystem/{moId}/DisableClusteredVmdkSupport | Disable the clustered vmdk support on specified datastore. 
[**host_datastore_system_enable_clustered_vmdk_support**](HostDatastoreSystemApi.md#host_datastore_system_enable_clustered_vmdk_support) | **POST** /HostDatastoreSystem/{moId}/EnableClusteredVmdkSupport | Enable the clustered vmdk support on specified datastore. 
[**host_datastore_system_expand_vmfs_datastore**](HostDatastoreSystemApi.md#host_datastore_system_expand_vmfs_datastore) | **POST** /HostDatastoreSystem/{moId}/ExpandVmfsDatastore | Increases the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 
[**host_datastore_system_extend_vmfs_datastore**](HostDatastoreSystemApi.md#host_datastore_system_extend_vmfs_datastore) | **POST** /HostDatastoreSystem/{moId}/ExtendVmfsDatastore | Increases the capacity of an existing VMFS datastore by adding new extents to the datastore. 
[**host_datastore_system_get_capabilities**](HostDatastoreSystemApi.md#host_datastore_system_get_capabilities) | **GET** /HostDatastoreSystem/{moId}/capabilities | Capability vector indicating the available product features. 
[**host_datastore_system_get_datastore**](HostDatastoreSystemApi.md#host_datastore_system_get_datastore) | **GET** /HostDatastoreSystem/{moId}/datastore | List of datastores on this host. 
[**host_datastore_system_query_available_disks_for_vmfs**](HostDatastoreSystemApi.md#host_datastore_system_query_available_disks_for_vmfs) | **POST** /HostDatastoreSystem/{moId}/QueryAvailableDisksForVmfs | Query to list disks that can be used to contain VMFS datastore extents. 
[**host_datastore_system_query_max_queue_depth**](HostDatastoreSystemApi.md#host_datastore_system_query_max_queue_depth) | **POST** /HostDatastoreSystem/{moId}/QueryMaxQueueDepth | Query max queue depth for a specified NFS datastore. 
[**host_datastore_system_query_unresolved_vmfs_volumes**](HostDatastoreSystemApi.md#host_datastore_system_query_unresolved_vmfs_volumes) | **POST** /HostDatastoreSystem/{moId}/QueryUnresolvedVmfsVolumes | Get the list of unbound VMFS volumes. 
[**host_datastore_system_query_vmfs_datastore_create_options**](HostDatastoreSystemApi.md#host_datastore_system_query_vmfs_datastore_create_options) | **POST** /HostDatastoreSystem/{moId}/QueryVmfsDatastoreCreateOptions | Queries options for creating a new VMFS datastore for a disk. 
[**host_datastore_system_query_vmfs_datastore_expand_options**](HostDatastoreSystemApi.md#host_datastore_system_query_vmfs_datastore_expand_options) | **POST** /HostDatastoreSystem/{moId}/QueryVmfsDatastoreExpandOptions | Queries for options for increasing the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 
[**host_datastore_system_query_vmfs_datastore_extend_options**](HostDatastoreSystemApi.md#host_datastore_system_query_vmfs_datastore_extend_options) | **POST** /HostDatastoreSystem/{moId}/QueryVmfsDatastoreExtendOptions | Queries for options for increasing the capacity of an existing VMFS datastore by adding new extents using space from the specified disk. 
[**host_datastore_system_remove_datastore**](HostDatastoreSystemApi.md#host_datastore_system_remove_datastore) | **POST** /HostDatastoreSystem/{moId}/RemoveDatastore | Removes a datastore from a host. 
[**host_datastore_system_remove_datastore_ex_task**](HostDatastoreSystemApi.md#host_datastore_system_remove_datastore_ex_task) | **POST** /HostDatastoreSystem/{moId}/RemoveDatastoreEx_Task | Remove one or more datastores. 
[**host_datastore_system_resignature_unresolved_vmfs_volume_task**](HostDatastoreSystemApi.md#host_datastore_system_resignature_unresolved_vmfs_volume_task) | **POST** /HostDatastoreSystem/{moId}/ResignatureUnresolvedVmfsVolume_Task | Resignature an unbound VMFS volume. 
[**host_datastore_system_set_max_queue_depth**](HostDatastoreSystemApi.md#host_datastore_system_set_max_queue_depth) | **POST** /HostDatastoreSystem/{moId}/SetMaxQueueDepth | Set max queue depth for a specified NFS datastore. 
[**host_datastore_system_update_local_swap_datastore**](HostDatastoreSystemApi.md#host_datastore_system_update_local_swap_datastore) | **POST** /HostDatastoreSystem/{moId}/UpdateLocalSwapDatastore | Choose the *localSwapDatastore* for this host. 


# **host_datastore_system_configure_datastore_principal**
> host_datastore_system_configure_datastore_principal(mo_id, configure_datastore_principal_request_type)

Configures datastore principal user for the host. 

Configures datastore principal user for the host.  All virtual machine-related file I/O is performed under this user. Configuring datastore principal user will result in all virtual machine files (configuration, disk, and so on) being checked for proper access. If necessary, ownership and permissions are modified. Note that in some environments, file ownership and permissions modification may not be possible. For example, virtual machine files stored on NFS cannot be modified for ownership and permissions if root squashing is enabled. Ownership and permissions for these files must be manually changed by a system administrator. In general, if server process does not have rights to change ownership and file permissions of virtual machine files, they must be modified manually. If a virtual machine files are not read/writeable by this user, virtual machine related operations such as power on/off, configuration, and so on will fail. This operation must be performed while in maintenance mode and requires host reboot.  ***Required privileges:*** Host.Config.Maintenance 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_datastore_principal_request_type import ConfigureDatastorePrincipalRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_datastore_principal_request_type = vmware_vi.ConfigureDatastorePrincipalRequestType() # ConfigureDatastorePrincipalRequestType | 

    try:
        # Configures datastore principal user for the host. 
        api_instance.host_datastore_system_configure_datastore_principal(mo_id, configure_datastore_principal_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_configure_datastore_principal: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_datastore_principal_request_type** | [**ConfigureDatastorePrincipalRequestType**](ConfigureDatastorePrincipalRequestType.md)|  | 

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
**500** | ***InvalidState***: if the host is not in maintenance mode.  ***InvalidArgument***: if userName or password is not valid.  ***NotSupported***: if this feature is not supported on the host.  ***HostConfigFault***: if unable to configure the datastore principal.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_create_local_datastore**
> ManagedObjectReference host_datastore_system_create_local_datastore(mo_id, create_local_datastore_request_type)

Creates a new local datastore. 

Creates a new local datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_local_datastore_request_type import CreateLocalDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_local_datastore_request_type = vmware_vi.CreateLocalDatastoreRequestType() # CreateLocalDatastoreRequestType | 

    try:
        # Creates a new local datastore. 
        api_response = api_instance.host_datastore_system_create_local_datastore(mo_id, create_local_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_create_local_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_create_local_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_local_datastore_request_type** | [**CreateLocalDatastoreRequestType**](CreateLocalDatastoreRequestType.md)|  | 

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
**200** | Refers instance of *Datastore*.  |  -  |
**500** | ***DuplicateName***: if a datastore with the same name already exists.  ***HostConfigFault***: if unable to create the datastore on host.  ***InvalidName***: if name is not valid datastore name  ***FileNotFound***: if path doesn&#39;t exist  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_create_nas_datastore**
> ManagedObjectReference host_datastore_system_create_nas_datastore(mo_id, create_nas_datastore_request_type)

Creates a new network-attached storage datastore. 

Creates a new network-attached storage datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_nas_datastore_request_type import CreateNasDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_nas_datastore_request_type = vmware_vi.CreateNasDatastoreRequestType() # CreateNasDatastoreRequestType | 

    try:
        # Creates a new network-attached storage datastore. 
        api_response = api_instance.host_datastore_system_create_nas_datastore(mo_id, create_nas_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_create_nas_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_create_nas_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_nas_datastore_request_type** | [**CreateNasDatastoreRequestType**](CreateNasDatastoreRequestType.md)|  | 

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
**200** | The newly created datastore.  Refers instance of *Datastore*.  |  -  |
**500** | ***DuplicateName***: if a datastore with the same name already exists.  ***InvalidArgument***: if the datastore name is invalid, or the spec is invalid.  ***NoVirtualNic***: if VMkernel TCPIP stack is not configured.  ***NoGateway***: if VMkernel gateway is not configured.  ***AlreadyExists***: if the local path already exists on the host, or the remote path is already mounted on the host.  ***HostConfigFault***: if unable to mount the NAS volume.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_create_vmfs_datastore**
> ManagedObjectReference host_datastore_system_create_vmfs_datastore(mo_id, create_vmfs_datastore_request_type)

Creates a new VMFS datastore. 

Creates a new VMFS datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_vmfs_datastore_request_type import CreateVmfsDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_vmfs_datastore_request_type = vmware_vi.CreateVmfsDatastoreRequestType() # CreateVmfsDatastoreRequestType | 

    try:
        # Creates a new VMFS datastore. 
        api_response = api_instance.host_datastore_system_create_vmfs_datastore(mo_id, create_vmfs_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_create_vmfs_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_create_vmfs_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_vmfs_datastore_request_type** | [**CreateVmfsDatastoreRequestType**](CreateVmfsDatastoreRequestType.md)|  | 

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
**200** | The newly created datastore.  Refers instance of *Datastore*.  |  -  |
**500** | ***DuplicateName***: if a datastore with the same name already exists.  ***InvalidArgument***: if the datastore name is invalid, or the spec is invalid.  ***NotSupported***: if the host is not an ESX Server system.  ***HostConfigFault***: if unable to format the VMFS volume or gather information about the created volume.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_create_vvol_datastore**
> ManagedObjectReference host_datastore_system_create_vvol_datastore(mo_id, create_vvol_datastore_request_type)

Create a Virtual-Volume based datastore 

Create a Virtual-Volume based datastore  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_vvol_datastore_request_type import CreateVvolDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_vvol_datastore_request_type = vmware_vi.CreateVvolDatastoreRequestType() # CreateVvolDatastoreRequestType | 

    try:
        # Create a Virtual-Volume based datastore 
        api_response = api_instance.host_datastore_system_create_vvol_datastore(mo_id, create_vvol_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_create_vvol_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_create_vvol_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_vvol_datastore_request_type** | [**CreateVvolDatastoreRequestType**](CreateVvolDatastoreRequestType.md)|  | 

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
**200** | The newly created datastore.  Refers instance of *Datastore*.  |  -  |
**500** | ***NotFound***: if the storage container could not be found.  ***DuplicateName***: if a datastore with the same name already exists.  ***HostConfigFault***: if unable to create the datastore on host.  ***InvalidName***: if name is not valid datastore name  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_disable_clustered_vmdk_support**
> host_datastore_system_disable_clustered_vmdk_support(mo_id, disable_clustered_vmdk_support_request_type)

Disable the clustered vmdk support on specified datastore. 

Disable the clustered vmdk support on specified datastore.  This API will fail if there are running VMs on the datastore which are configured to use clustered VMDK feature.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disable_clustered_vmdk_support_request_type import DisableClusteredVmdkSupportRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disable_clustered_vmdk_support_request_type = vmware_vi.DisableClusteredVmdkSupportRequestType() # DisableClusteredVmdkSupportRequestType | 

    try:
        # Disable the clustered vmdk support on specified datastore. 
        api_instance.host_datastore_system_disable_clustered_vmdk_support(mo_id, disable_clustered_vmdk_support_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_disable_clustered_vmdk_support: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disable_clustered_vmdk_support_request_type** | [**DisableClusteredVmdkSupportRequestType**](DisableClusteredVmdkSupportRequestType.md)|  | 

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
**500** | ***NotFound***: if a datastore with the name could not be found.  ***HostConfigFault***: if unable to disable clustered vmdk support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_enable_clustered_vmdk_support**
> host_datastore_system_enable_clustered_vmdk_support(mo_id, enable_clustered_vmdk_support_request_type)

Enable the clustered vmdk support on specified datastore. 

Enable the clustered vmdk support on specified datastore.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_clustered_vmdk_support_request_type import EnableClusteredVmdkSupportRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_clustered_vmdk_support_request_type = vmware_vi.EnableClusteredVmdkSupportRequestType() # EnableClusteredVmdkSupportRequestType | 

    try:
        # Enable the clustered vmdk support on specified datastore. 
        api_instance.host_datastore_system_enable_clustered_vmdk_support(mo_id, enable_clustered_vmdk_support_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_enable_clustered_vmdk_support: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_clustered_vmdk_support_request_type** | [**EnableClusteredVmdkSupportRequestType**](EnableClusteredVmdkSupportRequestType.md)|  | 

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
**500** | ***NotFound***: if a datastore with the name could not be found.  ***HostConfigFault***: if unable to enable clustered vmdk support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_expand_vmfs_datastore**
> ManagedObjectReference host_datastore_system_expand_vmfs_datastore(mo_id, expand_vmfs_datastore_request_type)

Increases the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 

Increases the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.expand_vmfs_datastore_request_type import ExpandVmfsDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    expand_vmfs_datastore_request_type = vmware_vi.ExpandVmfsDatastoreRequestType() # ExpandVmfsDatastoreRequestType | 

    try:
        # Increases the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 
        api_response = api_instance.host_datastore_system_expand_vmfs_datastore(mo_id, expand_vmfs_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_expand_vmfs_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_expand_vmfs_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **expand_vmfs_datastore_request_type** | [**ExpandVmfsDatastoreRequestType**](ExpandVmfsDatastoreRequestType.md)|  | 

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
**200** | The expanded datastore.  Refers instance of *Datastore*.  |  -  |
**500** | ***NotFound***: if a datastore with the name could not be found.  ***NotSupported***: if the host is not an ESX Server.  ***HostConfigFault***: if unable to expand the VMFS volume.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_extend_vmfs_datastore**
> ManagedObjectReference host_datastore_system_extend_vmfs_datastore(mo_id, extend_vmfs_datastore_request_type)

Increases the capacity of an existing VMFS datastore by adding new extents to the datastore. 

Increases the capacity of an existing VMFS datastore by adding new extents to the datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extend_vmfs_datastore_request_type import ExtendVmfsDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    extend_vmfs_datastore_request_type = vmware_vi.ExtendVmfsDatastoreRequestType() # ExtendVmfsDatastoreRequestType | 

    try:
        # Increases the capacity of an existing VMFS datastore by adding new extents to the datastore. 
        api_response = api_instance.host_datastore_system_extend_vmfs_datastore(mo_id, extend_vmfs_datastore_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_extend_vmfs_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_extend_vmfs_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **extend_vmfs_datastore_request_type** | [**ExtendVmfsDatastoreRequestType**](ExtendVmfsDatastoreRequestType.md)|  | 

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
**200** | The extended datastore.  Refers instance of *Datastore*.  |  -  |
**500** | ***NotFound***: if a datastore with the name could not be found.  ***NotSupported***: if the host is not an ESX Server.  ***HostConfigFault***: if unable to extend the VMFS volume.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_get_capabilities**
> HostDatastoreSystemCapabilities host_datastore_system_get_capabilities(mo_id)

Capability vector indicating the available product features. 

Capability vector indicating the available product features.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_datastore_system_capabilities import HostDatastoreSystemCapabilities
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Capability vector indicating the available product features. 
        api_response = api_instance.host_datastore_system_get_capabilities(mo_id)
        print("The response of HostDatastoreSystemApi->host_datastore_system_get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_get_capabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostDatastoreSystemCapabilities**](HostDatastoreSystemCapabilities.md)

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

# **host_datastore_system_get_datastore**
> List[ManagedObjectReference] host_datastore_system_get_datastore(mo_id)

List of datastores on this host. 

List of datastores on this host.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of datastores on this host. 
        api_response = api_instance.host_datastore_system_get_datastore(mo_id)
        print("The response of HostDatastoreSystemApi->host_datastore_system_get_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_get_datastore: %s\n" % e)
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
**200** | Refers instances of *Datastore*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_available_disks_for_vmfs**
> List[HostScsiDisk] host_datastore_system_query_available_disks_for_vmfs(mo_id, query_available_disks_for_vmfs_request_type)

Query to list disks that can be used to contain VMFS datastore extents. 

Query to list disks that can be used to contain VMFS datastore extents.  If the optional parameter name is supplied, queries for disks that can be used to contain extents for a VMFS datastore identified by the supplied name. Otherwise, the method retrieves disks that can be used to contain new VMFS datastores.  This operation will filter out disks that are currently in use by an existing VMFS unless the VMFS using the disk is one being extended. It will also filter out management LUNs and disks that are referenced by RDMs. These disk LUNs are also unsuited for use by a VMFS.  Disk LUNs referenced by RDMs are found by examining all virtual machines known to the system and visiting their virtual disk backends. If a virtual disk backend uses an RDM that is referencing a disk LUN, the disk LUN becomes ineligible for use by a VMFS datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_scsi_disk import HostScsiDisk
from vmware_vi.models.query_available_disks_for_vmfs_request_type import QueryAvailableDisksForVmfsRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_available_disks_for_vmfs_request_type = vmware_vi.QueryAvailableDisksForVmfsRequestType() # QueryAvailableDisksForVmfsRequestType | 

    try:
        # Query to list disks that can be used to contain VMFS datastore extents. 
        api_response = api_instance.host_datastore_system_query_available_disks_for_vmfs(mo_id, query_available_disks_for_vmfs_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_available_disks_for_vmfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_available_disks_for_vmfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_available_disks_for_vmfs_request_type** | [**QueryAvailableDisksForVmfsRequestType**](QueryAvailableDisksForVmfsRequestType.md)|  | 

### Return type

[**List[HostScsiDisk]**](HostScsiDisk.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of data objects describing SCSI disks.  |  -  |
**500** | ***NotSupported***: if the host is not an ESX Server.  ***NotFound***: if the named VMFS datastore is not found.  ***InvalidArgument***: if named VMFS datastore is not a VMFS datastore.  ***HostConfigFault***: if unable to query disk information.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_max_queue_depth**
> int host_datastore_system_query_max_queue_depth(mo_id, query_max_queue_depth_request_type)

Query max queue depth for a specified NFS datastore. 

Query max queue depth for a specified NFS datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_max_queue_depth_request_type import QueryMaxQueueDepthRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_max_queue_depth_request_type = vmware_vi.QueryMaxQueueDepthRequestType() # QueryMaxQueueDepthRequestType | 

    try:
        # Query max queue depth for a specified NFS datastore. 
        api_response = api_instance.host_datastore_system_query_max_queue_depth(mo_id, query_max_queue_depth_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_max_queue_depth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_max_queue_depth: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_max_queue_depth_request_type** | [**QueryMaxQueueDepthRequestType**](QueryMaxQueueDepthRequestType.md)|  | 

### Return type

**int**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***NotFound***: if the datastore could not be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_unresolved_vmfs_volumes**
> List[HostUnresolvedVmfsVolume] host_datastore_system_query_unresolved_vmfs_volumes(mo_id)

Get the list of unbound VMFS volumes. 

Get the list of unbound VMFS volumes.  For sharing a volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_unresolved_vmfs_volume import HostUnresolvedVmfsVolume
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the list of unbound VMFS volumes. 
        api_response = api_instance.host_datastore_system_query_unresolved_vmfs_volumes(mo_id)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_unresolved_vmfs_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_unresolved_vmfs_volumes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostUnresolvedVmfsVolume]**](HostUnresolvedVmfsVolume.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of unbound VMFS datastore  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_vmfs_datastore_create_options**
> List[VmfsDatastoreOption] host_datastore_system_query_vmfs_datastore_create_options(mo_id, query_vmfs_datastore_create_options_request_type)

Queries options for creating a new VMFS datastore for a disk. 

Queries options for creating a new VMFS datastore for a disk.  See also *HostScsiDisk.devicePath*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vmfs_datastore_create_options_request_type import QueryVmfsDatastoreCreateOptionsRequestType
from vmware_vi.models.vmfs_datastore_option import VmfsDatastoreOption
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vmfs_datastore_create_options_request_type = vmware_vi.QueryVmfsDatastoreCreateOptionsRequestType() # QueryVmfsDatastoreCreateOptionsRequestType | 

    try:
        # Queries options for creating a new VMFS datastore for a disk. 
        api_response = api_instance.host_datastore_system_query_vmfs_datastore_create_options(mo_id, query_vmfs_datastore_create_options_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_create_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_create_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vmfs_datastore_create_options_request_type** | [**QueryVmfsDatastoreCreateOptionsRequestType**](QueryVmfsDatastoreCreateOptionsRequestType.md)|  | 

### Return type

[**List[VmfsDatastoreOption]**](VmfsDatastoreOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of VMFS datastore provisioning options that can be applied on a disk.  |  -  |
**500** | ***NotSupported***: if the host is not an ESX Server.  ***NotFound***: if the device is not found.  ***HostConfigFault***: if unable to get the current partition information for the device.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_vmfs_datastore_expand_options**
> List[VmfsDatastoreOption] host_datastore_system_query_vmfs_datastore_expand_options(mo_id, query_vmfs_datastore_expand_options_request_type)

Queries for options for increasing the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 

Queries for options for increasing the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vmfs_datastore_expand_options_request_type import QueryVmfsDatastoreExpandOptionsRequestType
from vmware_vi.models.vmfs_datastore_option import VmfsDatastoreOption
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vmfs_datastore_expand_options_request_type = vmware_vi.QueryVmfsDatastoreExpandOptionsRequestType() # QueryVmfsDatastoreExpandOptionsRequestType | 

    try:
        # Queries for options for increasing the capacity of an existing VMFS datastore by expanding (increasing the size of) an existing extent of the datastore. 
        api_response = api_instance.host_datastore_system_query_vmfs_datastore_expand_options(mo_id, query_vmfs_datastore_expand_options_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_expand_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_expand_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vmfs_datastore_expand_options_request_type** | [**QueryVmfsDatastoreExpandOptionsRequestType**](QueryVmfsDatastoreExpandOptionsRequestType.md)|  | 

### Return type

[**List[VmfsDatastoreOption]**](VmfsDatastoreOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of VMFS datastore expansion options that can be applied.  |  -  |
**500** | ***NotFound***: if the specified datastore could not be found or is unmounted.  ***HostConfigFault***: if unable to get partition information for the devices on which the extents reside  ***NotSupported***: if the host is not an ESX Server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_query_vmfs_datastore_extend_options**
> List[VmfsDatastoreOption] host_datastore_system_query_vmfs_datastore_extend_options(mo_id, query_vmfs_datastore_extend_options_request_type)

Queries for options for increasing the capacity of an existing VMFS datastore by adding new extents using space from the specified disk. 

Queries for options for increasing the capacity of an existing VMFS datastore by adding new extents using space from the specified disk.  See also *HostScsiDisk.devicePath*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vmfs_datastore_extend_options_request_type import QueryVmfsDatastoreExtendOptionsRequestType
from vmware_vi.models.vmfs_datastore_option import VmfsDatastoreOption
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vmfs_datastore_extend_options_request_type = vmware_vi.QueryVmfsDatastoreExtendOptionsRequestType() # QueryVmfsDatastoreExtendOptionsRequestType | 

    try:
        # Queries for options for increasing the capacity of an existing VMFS datastore by adding new extents using space from the specified disk. 
        api_response = api_instance.host_datastore_system_query_vmfs_datastore_extend_options(mo_id, query_vmfs_datastore_extend_options_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_extend_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_query_vmfs_datastore_extend_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vmfs_datastore_extend_options_request_type** | [**QueryVmfsDatastoreExtendOptionsRequestType**](QueryVmfsDatastoreExtendOptionsRequestType.md)|  | 

### Return type

[**List[VmfsDatastoreOption]**](VmfsDatastoreOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of VMFS datastore provisioning options that can be applied on a disk.  |  -  |
**500** | ***NotFound***: if a datastore or device with the given name could not be found or if the datastore is unmounted.  ***HostConfigFault***: if unable to get the current partition information for the device.  ***NotSupported***: if the host is not an ESX Server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_remove_datastore**
> host_datastore_system_remove_datastore(mo_id, remove_datastore_request_type)

Removes a datastore from a host. 

Removes a datastore from a host.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_datastore_request_type import RemoveDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_datastore_request_type = vmware_vi.RemoveDatastoreRequestType() # RemoveDatastoreRequestType | 

    try:
        # Removes a datastore from a host. 
        api_instance.host_datastore_system_remove_datastore(mo_id, remove_datastore_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_remove_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_datastore_request_type** | [**RemoveDatastoreRequestType**](RemoveDatastoreRequestType.md)|  | 

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
**500** | ***NotFound***: if the datastore could not be found.  ***HostConfigFault***: if unable to umount the NAS volume for NAS datastore, or gather the existing volume information.  ***ResourceInUse***: for a VMFS volume if there is any VM registered on any host attached to this datastore.  ***ResourceInUse***: for a NFS volume if there is any VM residing on this datastore and registered on this host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_remove_datastore_ex_task**
> ManagedObjectReference host_datastore_system_remove_datastore_ex_task(mo_id, remove_datastore_ex_request_type)

Remove one or more datastores. 

Remove one or more datastores.  This is an asynchronous, batch operation of removeDatastore. Please see *HostDatastoreSystem.RemoveDatastore* for operational details. Note: This API currently supports removal of only NFS datastores.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.remove_datastore_ex_request_type import RemoveDatastoreExRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_datastore_ex_request_type = vmware_vi.RemoveDatastoreExRequestType() # RemoveDatastoreExRequestType | 

    try:
        # Remove one or more datastores. 
        api_response = api_instance.host_datastore_system_remove_datastore_ex_task(mo_id, remove_datastore_ex_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_remove_datastore_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_remove_datastore_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_datastore_ex_request_type** | [**RemoveDatastoreExRequestType**](RemoveDatastoreExRequestType.md)|  | 

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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_resignature_unresolved_vmfs_volume_task**
> ManagedObjectReference host_datastore_system_resignature_unresolved_vmfs_volume_task(mo_id, resignature_unresolved_vmfs_volume_request_type)

Resignature an unbound VMFS volume. 

Resignature an unbound VMFS volume.  To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.  With 'Resignature' operation, a new Vmfs Uuid is assigned to the volume but its contents are kept intact. Resignature results in a new Vmfs volume on the host. Users can specify a list of hosts on which the volume will be auto-mounted.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.resignature_unresolved_vmfs_volume_request_type import ResignatureUnresolvedVmfsVolumeRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    resignature_unresolved_vmfs_volume_request_type = vmware_vi.ResignatureUnresolvedVmfsVolumeRequestType() # ResignatureUnresolvedVmfsVolumeRequestType | 

    try:
        # Resignature an unbound VMFS volume. 
        api_response = api_instance.host_datastore_system_resignature_unresolved_vmfs_volume_task(mo_id, resignature_unresolved_vmfs_volume_request_type)
        print("The response of HostDatastoreSystemApi->host_datastore_system_resignature_unresolved_vmfs_volume_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_resignature_unresolved_vmfs_volume_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **resignature_unresolved_vmfs_volume_request_type** | [**ResignatureUnresolvedVmfsVolumeRequestType**](ResignatureUnresolvedVmfsVolumeRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task result (*Task.info*.*TaskInfo.result*) contains a *HostResignatureRescanResult* object that identifies the newly created VMFS datastore.  Refers instance of *Task*.  |  -  |
**500** | ***VmfsAmbiguousMount***: when ESX is unable to resolve the extents of a VMFS volume unambiguously. This is thrown only when a VMFS volume has multiple extents and multiple copies of non-head extents are detected, and the user has not specified one copy of every extent. Please note that some versions of ESX may not support resolving the situation where multiple copies of non-head extents are detected, even if one copy of every extent is specified in the method parameter. To resolve such a situation, the user is expected to change the configuration (for example, using array management tools) so that only one copy of each non-head extent is presented to ESX.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_set_max_queue_depth**
> host_datastore_system_set_max_queue_depth(mo_id, set_max_queue_depth_request_type)

Set max queue depth for a specified NFS datastore. 

Set max queue depth for a specified NFS datastore.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_max_queue_depth_request_type import SetMaxQueueDepthRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_max_queue_depth_request_type = vmware_vi.SetMaxQueueDepthRequestType() # SetMaxQueueDepthRequestType | 

    try:
        # Set max queue depth for a specified NFS datastore. 
        api_instance.host_datastore_system_set_max_queue_depth(mo_id, set_max_queue_depth_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_set_max_queue_depth: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_max_queue_depth_request_type** | [**SetMaxQueueDepthRequestType**](SetMaxQueueDepthRequestType.md)|  | 

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
**500** | ***NotFound***: if the datastore could not be found.  ***InvalidArgument***: if max queue depth is not within range.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_datastore_system_update_local_swap_datastore**
> host_datastore_system_update_local_swap_datastore(mo_id, update_local_swap_datastore_request_type)

Choose the *localSwapDatastore* for this host. 

Choose the *localSwapDatastore* for this host.  Any change to this setting will affect virtual machines that subsequently power on or resume from a suspended state at this host, or that migrate to this host while powered on; virtual machines that are currently powered on at this host will not yet be affected.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_local_swap_datastore_request_type import UpdateLocalSwapDatastoreRequestType
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
    api_instance = vmware_vi.HostDatastoreSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_local_swap_datastore_request_type = vmware_vi.UpdateLocalSwapDatastoreRequestType() # UpdateLocalSwapDatastoreRequestType | 

    try:
        # Choose the *localSwapDatastore* for this host. 
        api_instance.host_datastore_system_update_local_swap_datastore(mo_id, update_local_swap_datastore_request_type)
    except Exception as e:
        print("Exception when calling HostDatastoreSystemApi->host_datastore_system_update_local_swap_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_local_swap_datastore_request_type** | [**UpdateLocalSwapDatastoreRequestType**](UpdateLocalSwapDatastoreRequestType.md)|  | 

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
**500** | ***NotSupported***: if the datastore argument is set and the *localSwapDatastoreSupported* capability is not true for the host.  ***InaccessibleDatastore***: if the datastore argument is set and the host cannot access the indicated datastore.  ***DatastoreNotWritableOnHost***: if the datastore argument is set and the host cannot write to the indicated datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

