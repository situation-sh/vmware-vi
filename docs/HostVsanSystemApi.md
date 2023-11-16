# vmware_vi.HostVsanSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_vsan_system_add_disks_task**](HostVsanSystemApi.md#host_vsan_system_add_disks_task) | **POST** /HostVsanSystem/{moId}/AddDisks_Task | Add the set of given disks for use by the VSAN service on this host. 
[**host_vsan_system_evacuate_vsan_node_task**](HostVsanSystemApi.md#host_vsan_system_evacuate_vsan_node_task) | **POST** /HostVsanSystem/{moId}/EvacuateVsanNode_Task | Evacuate this host from VSAN cluster. 
[**host_vsan_system_get_config**](HostVsanSystemApi.md#host_vsan_system_get_config) | **GET** /HostVsanSystem/{moId}/config | The current VSAN service configuration information for this host. 
[**host_vsan_system_initialize_disks_task**](HostVsanSystemApi.md#host_vsan_system_initialize_disks_task) | **POST** /HostVsanSystem/{moId}/InitializeDisks_Task | Initialize and use the sets of disks in the given *VsanHostDiskMapping* list for the VSAN service on this host. 
[**host_vsan_system_query_disks_for_vsan**](HostVsanSystemApi.md#host_vsan_system_query_disks_for_vsan) | **POST** /HostVsanSystem/{moId}/QueryDisksForVsan | Queries disks on this host for suitability to use with the VSAN service, and returns the result. 
[**host_vsan_system_query_host_status**](HostVsanSystemApi.md#host_vsan_system_query_host_status) | **POST** /HostVsanSystem/{moId}/QueryHostStatus | Queries this host&#39;s current runtime status for the VSAN service. 
[**host_vsan_system_recommission_vsan_node_task**](HostVsanSystemApi.md#host_vsan_system_recommission_vsan_node_task) | **POST** /HostVsanSystem/{moId}/RecommissionVsanNode_Task | Recommission this host to VSAN cluster. 
[**host_vsan_system_remove_disk_mapping_task**](HostVsanSystemApi.md#host_vsan_system_remove_disk_mapping_task) | **POST** /HostVsanSystem/{moId}/RemoveDiskMapping_Task | Delete given set of disk mappings from use by the VSAN service on this host. 
[**host_vsan_system_remove_disk_task**](HostVsanSystemApi.md#host_vsan_system_remove_disk_task) | **POST** /HostVsanSystem/{moId}/RemoveDisk_Task | Remove the set of given disks from use by the VSAN service on this host. 
[**host_vsan_system_unmount_disk_mapping_task**](HostVsanSystemApi.md#host_vsan_system_unmount_disk_mapping_task) | **POST** /HostVsanSystem/{moId}/UnmountDiskMapping_Task | Unmount the mounted *VsanHostDiskMapping*. 
[**host_vsan_system_update_vsan_task**](HostVsanSystemApi.md#host_vsan_system_update_vsan_task) | **POST** /HostVsanSystem/{moId}/UpdateVsan_Task | Update the VSAN service on this host according to the given host configuration specification. 


# **host_vsan_system_add_disks_task**
> ManagedObjectReference host_vsan_system_add_disks_task(mo_id, add_disks_request_type)

Add the set of given disks for use by the VSAN service on this host. 

Add the set of given disks for use by the VSAN service on this host.  Users may use this API to manually add disks for use by VSAN, without specifying an explicit *VsanHostDiskMapping*, when the VSAN service not configured to automatically claim storage. Any ineligible disk in the set of given disks and disks which would have exceeded the capacity will be ignored and will not be published in returned *TaskInfo.result*.  Mount a *VsanHostDiskMapping* if the specified disk belongs to the unmounted mapping and is of type *VsanHostDiskMapping.ssd*.  Upon successful completion of the returned *Task*, its *TaskInfo.result* field will be populated with a *VsanHostDiskMapResult*\\[\\] and caller must inspect *VsanHostDiskMapResult*\\[\\] to check result for individual *VsanHostDiskMapping*.  See also *HostVsanSystem.QueryDisksForVsan*, *VsanHostConfigInfoStorageInfo.autoClaimStorage*, *VsanHostDiskMapInfo.mounted*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_disks_request_type import AddDisksRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_disks_request_type = vmware_vi.AddDisksRequestType() # AddDisksRequestType | 

    try:
        # Add the set of given disks for use by the VSAN service on this host. 
        api_response = api_instance.host_vsan_system_add_disks_task(mo_id, add_disks_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_add_disks_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_add_disks_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_disks_request_type** | [**AddDisksRequestType**](AddDisksRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_evacuate_vsan_node_task**
> ManagedObjectReference host_vsan_system_evacuate_vsan_node_task(mo_id, evacuate_vsan_node_request_type)

Evacuate this host from VSAN cluster. 

Evacuate this host from VSAN cluster.  The task is cancellable.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.evacuate_vsan_node_request_type import EvacuateVsanNodeRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    evacuate_vsan_node_request_type = vmware_vi.EvacuateVsanNodeRequestType() # EvacuateVsanNodeRequestType | 

    try:
        # Evacuate this host from VSAN cluster. 
        api_response = api_instance.host_vsan_system_evacuate_vsan_node_task(mo_id, evacuate_vsan_node_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_evacuate_vsan_node_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_evacuate_vsan_node_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **evacuate_vsan_node_request_type** | [**EvacuateVsanNodeRequestType**](EvacuateVsanNodeRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: If the host is entering maintenance mode or evacuating data.  ***RequestCanceled***: if the operation is canceled.  ***Timedout***: if the operation timed out.  ***VsanFault***: if operation fails with VSAN-specific error.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_get_config**
> VsanHostConfigInfo host_vsan_system_get_config(mo_id)

The current VSAN service configuration information for this host. 

The current VSAN service configuration information for this host.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.vsan_host_config_info import VsanHostConfigInfo
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The current VSAN service configuration information for this host. 
        api_response = api_instance.host_vsan_system_get_config(mo_id)
        print("The response of HostVsanSystemApi->host_vsan_system_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VsanHostConfigInfo**](VsanHostConfigInfo.md)

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

# **host_vsan_system_initialize_disks_task**
> ManagedObjectReference host_vsan_system_initialize_disks_task(mo_id, initialize_disks_request_type)

Initialize and use the sets of disks in the given *VsanHostDiskMapping* list for the VSAN service on this host. 

Initialize and use the sets of disks in the given *VsanHostDiskMapping* list for the VSAN service on this host.  Users may use this API to specify or change disk mappings when the VSAN service is not configured to automatically claim storage. For appending new non-SSDs to an existing *VsanHostDiskMapping*, users need to specify only the new non-SSDs with its *VsanHostDiskMapping.ssd*.  Mount a *VsanHostDiskMapping* if the specified *VsanHostDiskMapping* is not mounted in this host.  Upon successful completion of the returned *Task*, its *TaskInfo.result* field will be populated with a *VsanHostDiskMapResult*\\[\\] and caller must inspect *VsanHostDiskMapResult*\\[\\] to check result for individual *VsanHostDiskMapping*.  See also *HostVsanSystem.QueryDisksForVsan*, *VsanHostConfigInfoStorageInfo.autoClaimStorage*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.initialize_disks_request_type import InitializeDisksRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    initialize_disks_request_type = vmware_vi.InitializeDisksRequestType() # InitializeDisksRequestType | 

    try:
        # Initialize and use the sets of disks in the given *VsanHostDiskMapping* list for the VSAN service on this host. 
        api_response = api_instance.host_vsan_system_initialize_disks_task(mo_id, initialize_disks_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_initialize_disks_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_initialize_disks_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **initialize_disks_request_type** | [**InitializeDisksRequestType**](InitializeDisksRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_query_disks_for_vsan**
> List[VsanHostDiskResult] host_vsan_system_query_disks_for_vsan(mo_id, query_disks_for_vsan_request_type)

Queries disks on this host for suitability to use with the VSAN service, and returns the result. 

Queries disks on this host for suitability to use with the VSAN service, and returns the result.  See also *ScsiLun.canonicalName*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_disks_for_vsan_request_type import QueryDisksForVsanRequestType
from vmware_vi.models.vsan_host_disk_result import VsanHostDiskResult
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_disks_for_vsan_request_type = vmware_vi.QueryDisksForVsanRequestType() # QueryDisksForVsanRequestType | 

    try:
        # Queries disks on this host for suitability to use with the VSAN service, and returns the result. 
        api_response = api_instance.host_vsan_system_query_disks_for_vsan(mo_id, query_disks_for_vsan_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_query_disks_for_vsan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_query_disks_for_vsan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_disks_for_vsan_request_type** | [**QueryDisksForVsanRequestType**](QueryDisksForVsanRequestType.md)|  | 

### Return type

[**List[VsanHostDiskResult]**](VsanHostDiskResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of populated *VsanHostDiskResult* entries  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_query_host_status**
> VsanHostClusterStatus host_vsan_system_query_host_status(mo_id)

Queries this host's current runtime status for the VSAN service. 

Queries this host's current runtime status for the VSAN service.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.vsan_host_cluster_status import VsanHostClusterStatus
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Queries this host's current runtime status for the VSAN service. 
        api_response = api_instance.host_vsan_system_query_host_status(mo_id)
        print("The response of HostVsanSystemApi->host_vsan_system_query_host_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_query_host_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VsanHostClusterStatus**](VsanHostClusterStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a populated *VsanHostClusterStatus* entry  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_recommission_vsan_node_task**
> ManagedObjectReference host_vsan_system_recommission_vsan_node_task(mo_id)

Recommission this host to VSAN cluster. 

Recommission this host to VSAN cluster.  Users may use this API to recommission a node that has been evacuated in *VsanHostDecommissionMode*.  See also *HostVsanSystem.EvacuateVsanNode_Task*, *VsanHostDecommissionMode*.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Recommission this host to VSAN cluster. 
        api_response = api_instance.host_vsan_system_recommission_vsan_node_task(mo_id)
        print("The response of HostVsanSystemApi->host_vsan_system_recommission_vsan_node_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_recommission_vsan_node_task: %s\n" % e)
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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: if the host is not evacuated.  ***VsanFault***: if operation fails with VSAN-specific error.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_remove_disk_mapping_task**
> ManagedObjectReference host_vsan_system_remove_disk_mapping_task(mo_id, remove_disk_mapping_request_type)

Delete given set of disk mappings from use by the VSAN service on this host. 

Delete given set of disk mappings from use by the VSAN service on this host.  This API may be used to remove all disks in a given mapping, including its *VsanHostDiskMapping.ssd*. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.  The task is cancellable.  Upon successful completion of the returned *Task*, its *TaskInfo.result* field will be populated with an empty *VsanHostDiskMapResult*\\[\\]. If any errors are encountered, the returned field will instead contain populated error information.  See also *HostVsanSystem.RemoveDisk_Task*, *HostVsanSystem.UpdateVsan_Task*, *VsanHostConfigInfoStorageInfo.autoClaimStorage*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.remove_disk_mapping_request_type import RemoveDiskMappingRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_disk_mapping_request_type = vmware_vi.RemoveDiskMappingRequestType() # RemoveDiskMappingRequestType | 

    try:
        # Delete given set of disk mappings from use by the VSAN service on this host. 
        api_response = api_instance.host_vsan_system_remove_disk_mapping_task(mo_id, remove_disk_mapping_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_remove_disk_mapping_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_remove_disk_mapping_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_disk_mapping_request_type** | [**RemoveDiskMappingRequestType**](RemoveDiskMappingRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_remove_disk_task**
> ManagedObjectReference host_vsan_system_remove_disk_task(mo_id, remove_disk_request_type)

Remove the set of given disks from use by the VSAN service on this host. 

Remove the set of given disks from use by the VSAN service on this host.  Users may use this API to manually remove a *VsanHostDiskMapping.nonSsd* from a *VsanHostDiskMapping*. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.  The task is cancellable.  This method may not be used to remove the last *VsanHostDiskMapping.nonSsd* from any given *VsanHostDiskMapping*. Removal of the last *VsanHostDiskMapping.nonSsd* can be accomplished by using *HostVsanSystem.RemoveDiskMapping_Task*.  Upon successful completion of the returned *Task*, its *TaskInfo.result* field will be populated with a *VsanHostDiskResult*\\[\\]. Sets DiskIsLastRemainingNonSSD fault in returned task if specified disk is the last *VsanHostDiskMapping.nonSsd* member of *VsanHostDiskMapping*.  See also *HostVsanSystem.RemoveDiskMapping_Task*, *HostVsanSystem.UpdateVsan_Task*, *VsanHostConfigInfoStorageInfo.autoClaimStorage*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.remove_disk_request_type import RemoveDiskRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_disk_request_type = vmware_vi.RemoveDiskRequestType() # RemoveDiskRequestType | 

    try:
        # Remove the set of given disks from use by the VSAN service on this host. 
        api_response = api_instance.host_vsan_system_remove_disk_task(mo_id, remove_disk_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_remove_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_remove_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_disk_request_type** | [**RemoveDiskRequestType**](RemoveDiskRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_unmount_disk_mapping_task**
> ManagedObjectReference host_vsan_system_unmount_disk_mapping_task(mo_id, unmount_disk_mapping_request_type)

Unmount the mounted *VsanHostDiskMapping*. 

Unmount the mounted *VsanHostDiskMapping*.  An unmounted volume cannot be used for any VSAN operations. In contrast to *HostVsanSystem.RemoveDiskMapping_Task*, this operation does not destroy or alter VSAN data on the disks. *HostVsanSystem.AddDisks_Task* and *HostVsanSystem.InitializeDisks_Task* can be used to re-mount the diskMapping.  In case of shared-SAS, where diskMappings are visible to more than one VSAN hosts, Users may use this API to manually unmount and re-mount diskMappings.  Upon successful completion of the returned *Task*, its *TaskInfo.result* field will be populated with *VsanHostDiskMapResult*\\[\\]. If any errors are encountered, the returned field will instead contain populated error information.  See also *HostVsanSystem.RemoveDiskMapping_Task*, *HostVsanSystem.AddDisks_Task*, *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.unmount_disk_mapping_request_type import UnmountDiskMappingRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmount_disk_mapping_request_type = vmware_vi.UnmountDiskMappingRequestType() # UnmountDiskMappingRequestType | 

    try:
        # Unmount the mounted *VsanHostDiskMapping*. 
        api_response = api_instance.host_vsan_system_unmount_disk_mapping_task(mo_id, unmount_disk_mapping_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_unmount_disk_mapping_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_unmount_disk_mapping_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmount_disk_mapping_request_type** | [**UnmountDiskMappingRequestType**](UnmountDiskMappingRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: If the *VsanHostDiskMapping* is already unmounted.  ***VsanFault***: if operation fails with VSAN-specific error.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_system_update_vsan_task**
> ManagedObjectReference host_vsan_system_update_vsan_task(mo_id, update_vsan_request_type)

Update the VSAN service on this host according to the given host configuration specification. 

Update the VSAN service on this host according to the given host configuration specification.  Enabling and disabling the VSAN service can be achieved by using the *VsanHostConfigInfo.enabled* flag. Host storage settings can be specified through use of *VsanHostConfigInfo.storageInfo*. If this value is omitted, changes will not be made to the existing storage configuration. Host cluster settings can be specified through use of *VsanHostConfigInfo.clusterInfo*. If this value is omitted, changes will not be made to the existing cluster configuration. Host network settings can be specified through use of *VsanHostConfigInfo.networkInfo*. If this value is omitted, changes will not be made to the existing network configuration.  See also *VsanHostConfigInfo*, *VsanHostConfigInfo.storageInfo*, *VsanHostConfigInfo.clusterInfo*, *VsanHostConfigInfo.networkInfo*, *HostVsanSystem.QueryDisksForVsan*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_vsan_request_type import UpdateVsanRequestType
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
    api_instance = vmware_vi.HostVsanSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_vsan_request_type = vmware_vi.UpdateVsanRequestType() # UpdateVsanRequestType | 

    try:
        # Update the VSAN service on this host according to the given host configuration specification. 
        api_response = api_instance.host_vsan_system_update_vsan_task(mo_id, update_vsan_request_type)
        print("The response of HostVsanSystemApi->host_vsan_system_update_vsan_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanSystemApi->host_vsan_system_update_vsan_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_vsan_request_type** | [**UpdateVsanRequestType**](UpdateVsanRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

