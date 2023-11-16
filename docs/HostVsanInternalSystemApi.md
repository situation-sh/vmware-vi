# vmware_vi.HostVsanInternalSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_vsan_internal_system_abdicate_dom_ownership**](HostVsanInternalSystemApi.md#host_vsan_internal_system_abdicate_dom_ownership) | **POST** /HostVsanInternalSystem/{moId}/AbdicateDomOwnership | Abdicate ownership of DOM objects. 
[**host_vsan_internal_system_can_provision_objects**](HostVsanInternalSystemApi.md#host_vsan_internal_system_can_provision_objects) | **POST** /HostVsanInternalSystem/{moId}/CanProvisionObjects | Determine if given objects can be provisioned. 
[**host_vsan_internal_system_delete_vsan_objects**](HostVsanInternalSystemApi.md#host_vsan_internal_system_delete_vsan_objects) | **POST** /HostVsanInternalSystem/{moId}/DeleteVsanObjects | Delete VSAN objects. 
[**host_vsan_internal_system_get_vsan_obj_ext_attrs**](HostVsanInternalSystemApi.md#host_vsan_internal_system_get_vsan_obj_ext_attrs) | **POST** /HostVsanInternalSystem/{moId}/GetVsanObjExtAttrs | Get VSAN object extended attributes. 
[**host_vsan_internal_system_query_cmmds**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_cmmds) | **POST** /HostVsanInternalSystem/{moId}/QueryCmmds | Query CMMDS directly. 
[**host_vsan_internal_system_query_objects_on_physical_vsan_disk**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_objects_on_physical_vsan_disk) | **POST** /HostVsanInternalSystem/{moId}/QueryObjectsOnPhysicalVsanDisk | Query DOM objects on a given set of physical disks. 
[**host_vsan_internal_system_query_physical_vsan_disks**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_physical_vsan_disks) | **POST** /HostVsanInternalSystem/{moId}/QueryPhysicalVsanDisks | Query statistics about physical VSAN disks. 
[**host_vsan_internal_system_query_syncing_vsan_objects**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_syncing_vsan_objects) | **POST** /HostVsanInternalSystem/{moId}/QuerySyncingVsanObjects | Query information about VSAN DOM objects that are currently syncing data. 
[**host_vsan_internal_system_query_vsan_object_uuids_by_filter**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_vsan_object_uuids_by_filter) | **POST** /HostVsanInternalSystem/{moId}/QueryVsanObjectUuidsByFilter | Query VSAN object UUIDs by filtering conditions. 
[**host_vsan_internal_system_query_vsan_objects**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_vsan_objects) | **POST** /HostVsanInternalSystem/{moId}/QueryVsanObjects | Query information about VSAN DOM objects. 
[**host_vsan_internal_system_query_vsan_statistics**](HostVsanInternalSystemApi.md#host_vsan_internal_system_query_vsan_statistics) | **POST** /HostVsanInternalSystem/{moId}/QueryVsanStatistics | Query VSAN system statistics. 
[**host_vsan_internal_system_reconfiguration_satisfiable**](HostVsanInternalSystemApi.md#host_vsan_internal_system_reconfiguration_satisfiable) | **POST** /HostVsanInternalSystem/{moId}/ReconfigurationSatisfiable | Determine if the given objects can be reconfigured with the given policies. 
[**host_vsan_internal_system_reconfigure_dom_object**](HostVsanInternalSystemApi.md#host_vsan_internal_system_reconfigure_dom_object) | **POST** /HostVsanInternalSystem/{moId}/ReconfigureDomObject | Reconfigure DOM object. 
[**host_vsan_internal_system_run_vsan_physical_disk_diagnostics**](HostVsanInternalSystemApi.md#host_vsan_internal_system_run_vsan_physical_disk_diagnostics) | **POST** /HostVsanInternalSystem/{moId}/RunVsanPhysicalDiskDiagnostics | Runs diagnostics on VSAN physical disks. 
[**host_vsan_internal_system_upgrade_vsan_objects**](HostVsanInternalSystemApi.md#host_vsan_internal_system_upgrade_vsan_objects) | **POST** /HostVsanInternalSystem/{moId}/UpgradeVsanObjects | Upgrade VSAN objects version. 


# **host_vsan_internal_system_abdicate_dom_ownership**
> List[str] host_vsan_internal_system_abdicate_dom_ownership(mo_id, abdicate_dom_ownership_request_type)

Abdicate ownership of DOM objects. 

Abdicate ownership of DOM objects.  The objects must be currently owned by this host. Which host has ownership of an object at a given point in time can be queried from QueryVsanObjects() or QueryCmmds() APIs. Abidcating ownership tears down DOM owner in-memory state. Hosts in the cluster will then compete to become the new owner of the object, similar to a host failure event. There is a short interuption of IO flow while the owner re-election is going on, but it is transparent to any consumers of the object. This API is meant as a troubleshooting and debugging tool. It is internal at this point and can be used to resolve issues where DOM owner gets \"stuck\".  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.abdicate_dom_ownership_request_type import AbdicateDomOwnershipRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    abdicate_dom_ownership_request_type = vmware_vi.AbdicateDomOwnershipRequestType() # AbdicateDomOwnershipRequestType | 

    try:
        # Abdicate ownership of DOM objects. 
        api_response = api_instance.host_vsan_internal_system_abdicate_dom_ownership(mo_id, abdicate_dom_ownership_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_abdicate_dom_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_abdicate_dom_ownership: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **abdicate_dom_ownership_request_type** | [**AbdicateDomOwnershipRequestType**](AbdicateDomOwnershipRequestType.md)|  | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of UUIDs successfully abdicated.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_can_provision_objects**
> List[VsanPolicySatisfiability] host_vsan_internal_system_can_provision_objects(mo_id, can_provision_objects_request_type)

Determine if given objects can be provisioned. 

Determine if given objects can be provisioned.  Determines if the objects of the given size can be provisioned with the given policies. The API is intended to answer the question: can these objects be provisioned with the given policy using the current cluster topology (#hosts and #disks) and does NOT take into account free space on the disk, size of disks, etc. If the objects cannot be provisioned, the API returns the reason for not being able to satisfy the policy. If the objects can be provisioned, the API returns the cost of provisioning objects with this policy. Please note: This API ignores forceProvisioning.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.can_provision_objects_request_type import CanProvisionObjectsRequestType
from vmware_vi.models.vsan_policy_satisfiability import VsanPolicySatisfiability
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    can_provision_objects_request_type = vmware_vi.CanProvisionObjectsRequestType() # CanProvisionObjectsRequestType | 

    try:
        # Determine if given objects can be provisioned. 
        api_response = api_instance.host_vsan_internal_system_can_provision_objects(mo_id, can_provision_objects_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_can_provision_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_can_provision_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **can_provision_objects_request_type** | [**CanProvisionObjectsRequestType**](CanProvisionObjectsRequestType.md)|  | 

### Return type

[**List[VsanPolicySatisfiability]**](VsanPolicySatisfiability.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PolicySatisfiability objects, one for each specified size.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_delete_vsan_objects**
> List[HostVsanInternalSystemDeleteVsanObjectsResult] host_vsan_internal_system_delete_vsan_objects(mo_id, delete_vsan_objects_request_type)

Delete VSAN objects. 

Delete VSAN objects.  This API is internal and intended for troubleshooting/debugging only. WARNING: This API can be slow because we do IOs to all the objects. This API can be used to delete VSAN objects. DOM won't allow access to objects which have lost quorum. Such objects can be deleted with the optional \"force\" flag. These objects may however re-appear with quorum if the absent components come back (network partition gets resolved, etc.)  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_vsan_objects_request_type import DeleteVsanObjectsRequestType
from vmware_vi.models.host_vsan_internal_system_delete_vsan_objects_result import HostVsanInternalSystemDeleteVsanObjectsResult
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_vsan_objects_request_type = vmware_vi.DeleteVsanObjectsRequestType() # DeleteVsanObjectsRequestType | 

    try:
        # Delete VSAN objects. 
        api_response = api_instance.host_vsan_internal_system_delete_vsan_objects(mo_id, delete_vsan_objects_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_delete_vsan_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_delete_vsan_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_vsan_objects_request_type** | [**DeleteVsanObjectsRequestType**](DeleteVsanObjectsRequestType.md)|  | 

### Return type

[**List[HostVsanInternalSystemDeleteVsanObjectsResult]**](HostVsanInternalSystemDeleteVsanObjectsResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DeleteVsanObjectsResult.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_get_vsan_obj_ext_attrs**
> str host_vsan_internal_system_get_vsan_obj_ext_attrs(mo_id, get_vsan_obj_ext_attrs_request_type)

Get VSAN object extended attributes. 

Get VSAN object extended attributes.  This API is internal and intended for troubleshooting/debugging situations in the field. WARNING: This API can be slow because we do IOs (reads) to all the objects. This API can be used to get extended attributes of any object in the VSAN cluster from any host provided the object is accessible from that host. In case of an error, we return a dict with key \"Error\" for that object.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.get_vsan_obj_ext_attrs_request_type import GetVsanObjExtAttrsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_vsan_obj_ext_attrs_request_type = vmware_vi.GetVsanObjExtAttrsRequestType() # GetVsanObjExtAttrsRequestType | 

    try:
        # Get VSAN object extended attributes. 
        api_response = api_instance.host_vsan_internal_system_get_vsan_obj_ext_attrs(mo_id, get_vsan_obj_ext_attrs_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_get_vsan_obj_ext_attrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_get_vsan_obj_ext_attrs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_vsan_obj_ext_attrs_request_type** | [**GetVsanObjExtAttrsRequestType**](GetVsanObjExtAttrsRequestType.md)|  | 

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
**200** | JSON string with the extended attributes.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_cmmds**
> str host_vsan_internal_system_query_cmmds(mo_id, query_cmmds_request_type)

Query CMMDS directly. 

Query CMMDS directly.  The list of given queries is executed and all results are returned in a flat list. No attempt is made to de-dupe results in the case of overlapping query results.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_cmmds_request_type import QueryCmmdsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_cmmds_request_type = vmware_vi.QueryCmmdsRequestType() # QueryCmmdsRequestType | 

    try:
        # Query CMMDS directly. 
        api_response = api_instance.host_vsan_internal_system_query_cmmds(mo_id, query_cmmds_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_cmmds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_cmmds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_cmmds_request_type** | [**QueryCmmdsRequestType**](QueryCmmdsRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_objects_on_physical_vsan_disk**
> str host_vsan_internal_system_query_objects_on_physical_vsan_disk(mo_id, query_objects_on_physical_vsan_disk_request_type)

Query DOM objects on a given set of physical disks. 

Query DOM objects on a given set of physical disks.  Finds all DOM objects that have at least one component on the given physical disks. In order to make this API efficient, the output of this API contains the found DOM\\_OBJECT, and referenced LSOM\\_OBJECT and DISK entries.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_objects_on_physical_vsan_disk_request_type import QueryObjectsOnPhysicalVsanDiskRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_objects_on_physical_vsan_disk_request_type = vmware_vi.QueryObjectsOnPhysicalVsanDiskRequestType() # QueryObjectsOnPhysicalVsanDiskRequestType | 

    try:
        # Query DOM objects on a given set of physical disks. 
        api_response = api_instance.host_vsan_internal_system_query_objects_on_physical_vsan_disk(mo_id, query_objects_on_physical_vsan_disk_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_objects_on_physical_vsan_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_objects_on_physical_vsan_disk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_objects_on_physical_vsan_disk_request_type** | [**QueryObjectsOnPhysicalVsanDiskRequestType**](QueryObjectsOnPhysicalVsanDiskRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_physical_vsan_disks**
> str host_vsan_internal_system_query_physical_vsan_disks(mo_id, query_physical_vsan_disks_request_type)

Query statistics about physical VSAN disks. 

Query statistics about physical VSAN disks.  Using the props parameter the caller can control which properties are returned. Requesting only the required properties is encouraged to reduce server load, response time and client load.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_physical_vsan_disks_request_type import QueryPhysicalVsanDisksRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_physical_vsan_disks_request_type = vmware_vi.QueryPhysicalVsanDisksRequestType() # QueryPhysicalVsanDisksRequestType | 

    try:
        # Query statistics about physical VSAN disks. 
        api_response = api_instance.host_vsan_internal_system_query_physical_vsan_disks(mo_id, query_physical_vsan_disks_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_physical_vsan_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_physical_vsan_disks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_physical_vsan_disks_request_type** | [**QueryPhysicalVsanDisksRequestType**](QueryPhysicalVsanDisksRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_syncing_vsan_objects**
> str host_vsan_internal_system_query_syncing_vsan_objects(mo_id, query_syncing_vsan_objects_request_type)

Query information about VSAN DOM objects that are currently syncing data. 

Query information about VSAN DOM objects that are currently syncing data.  Instead of returning all objects, only such objects are returned that are currently resyncing any stale components or syncing fresh replicas. The API returns the same output format as queryVsanObjects(). It retrieves information about syncing all objects, or retricts the search for syncing objects to the UUID list provided. In order to make this API efficient, the output of this API contains the found DOM\\_OBJECT, and referenced LSOM\\_OBJECT and DISK entries.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_syncing_vsan_objects_request_type import QuerySyncingVsanObjectsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_syncing_vsan_objects_request_type = vmware_vi.QuerySyncingVsanObjectsRequestType() # QuerySyncingVsanObjectsRequestType | 

    try:
        # Query information about VSAN DOM objects that are currently syncing data. 
        api_response = api_instance.host_vsan_internal_system_query_syncing_vsan_objects(mo_id, query_syncing_vsan_objects_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_syncing_vsan_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_syncing_vsan_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_syncing_vsan_objects_request_type** | [**QuerySyncingVsanObjectsRequestType**](QuerySyncingVsanObjectsRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_vsan_object_uuids_by_filter**
> List[str] host_vsan_internal_system_query_vsan_object_uuids_by_filter(mo_id, query_vsan_object_uuids_by_filter_request_type)

Query VSAN object UUIDs by filtering conditions. 

Query VSAN object UUIDs by filtering conditions.  The API queries CMMDS by given filtering conditions (initially only for object version) and return object UUID in an array with limited elements count. If caller specified the inputs objects UUID, then only these objects will be checked for the filtering conditions, and return ones which satisfy the filtering condition. In this case, the 'limit' parameter will be ignored.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vsan_object_uuids_by_filter_request_type import QueryVsanObjectUuidsByFilterRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vsan_object_uuids_by_filter_request_type = vmware_vi.QueryVsanObjectUuidsByFilterRequestType() # QueryVsanObjectUuidsByFilterRequestType | 

    try:
        # Query VSAN object UUIDs by filtering conditions. 
        api_response = api_instance.host_vsan_internal_system_query_vsan_object_uuids_by_filter(mo_id, query_vsan_object_uuids_by_filter_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_object_uuids_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_object_uuids_by_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vsan_object_uuids_by_filter_request_type** | [**QueryVsanObjectUuidsByFilterRequestType**](QueryVsanObjectUuidsByFilterRequestType.md)|  | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | String array of object uuids which satisfy the filtering conditions.  |  -  |
**500** | ***VsanFault***: for any unexpected failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_vsan_objects**
> str host_vsan_internal_system_query_vsan_objects(mo_id, query_vsan_objects_request_type)

Query information about VSAN DOM objects. 

Query information about VSAN DOM objects.  Retrieves information about the given set of DOM object UUIDs. In order to make this API efficient, the output of this API contains the found DOM\\_OBJECT, and referenced LSOM\\_OBJECT and DISK entries.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vsan_objects_request_type import QueryVsanObjectsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vsan_objects_request_type = vmware_vi.QueryVsanObjectsRequestType() # QueryVsanObjectsRequestType | 

    try:
        # Query information about VSAN DOM objects. 
        api_response = api_instance.host_vsan_internal_system_query_vsan_objects(mo_id, query_vsan_objects_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vsan_objects_request_type** | [**QueryVsanObjectsRequestType**](QueryVsanObjectsRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_query_vsan_statistics**
> str host_vsan_internal_system_query_vsan_statistics(mo_id, query_vsan_statistics_request_type)

Query VSAN system statistics. 

Query VSAN system statistics.  This is a low level API that gathers low level statistic counters from the system. The details of the counters remain undocumented and unsupported at this point, and this API remains internal. The data for this API call mostly comes from VSI, but also other tools like memstats. The caller can control which counters are being retrieved by providing a list of labels. The following labels are current supported: \\- TBD  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vsan_statistics_request_type import QueryVsanStatisticsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vsan_statistics_request_type = vmware_vi.QueryVsanStatisticsRequestType() # QueryVsanStatisticsRequestType | 

    try:
        # Query VSAN system statistics. 
        api_response = api_instance.host_vsan_internal_system_query_vsan_statistics(mo_id, query_vsan_statistics_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_query_vsan_statistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vsan_statistics_request_type** | [**QueryVsanStatisticsRequestType**](QueryVsanStatisticsRequestType.md)|  | 

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
**200** | JSON string with the results  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_reconfiguration_satisfiable**
> List[VsanPolicySatisfiability] host_vsan_internal_system_reconfiguration_satisfiable(mo_id, reconfiguration_satisfiable_request_type)

Determine if the given objects can be reconfigured with the given policies. 

Determine if the given objects can be reconfigured with the given policies.  The what-if determination only takes into account the total number of hosts and total number of disks per host. The API is intended to answer the question: is this reconfiguration possible using the current cluster topology (#hosts and #disks) and does NOT take into account free space on the disk, size of disks, etc. If policy is not satisfiable, the API returns the reason for not being able to satisfy the policy. If the policy is satisfiable, the API returns the cost of provisioning objects with the new policy. This cost can be combined with current available free disk space to compute if a particular operation is expected to succeed or fail. Please note: This API ignores forceProvisioning.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfiguration_satisfiable_request_type import ReconfigurationSatisfiableRequestType
from vmware_vi.models.vsan_policy_satisfiability import VsanPolicySatisfiability
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfiguration_satisfiable_request_type = vmware_vi.ReconfigurationSatisfiableRequestType() # ReconfigurationSatisfiableRequestType | 

    try:
        # Determine if the given objects can be reconfigured with the given policies. 
        api_response = api_instance.host_vsan_internal_system_reconfiguration_satisfiable(mo_id, reconfiguration_satisfiable_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_reconfiguration_satisfiable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_reconfiguration_satisfiable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfiguration_satisfiable_request_type** | [**ReconfigurationSatisfiableRequestType**](ReconfigurationSatisfiableRequestType.md)|  | 

### Return type

[**List[VsanPolicySatisfiability]**](VsanPolicySatisfiability.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PolicySatisfiability objects, one for each specified UUID.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_reconfigure_dom_object**
> host_vsan_internal_system_reconfigure_dom_object(mo_id, reconfigure_dom_object_request_type)

Reconfigure DOM object. 

Reconfigure DOM object.  Typically we expect VM centric APIs to be used for setting storage policies, i.e. to use ReconfigVM() to change the policy/profile of a namespace directory or virtual disk. This is a low level API to reconfigure any object known by UUID. This API is internal and intended for troubleshooting/debugging situations in the field.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfigure_dom_object_request_type import ReconfigureDomObjectRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_dom_object_request_type = vmware_vi.ReconfigureDomObjectRequestType() # ReconfigureDomObjectRequestType | 

    try:
        # Reconfigure DOM object. 
        api_instance.host_vsan_internal_system_reconfigure_dom_object(mo_id, reconfigure_dom_object_request_type)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_reconfigure_dom_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_dom_object_request_type** | [**ReconfigureDomObjectRequestType**](ReconfigureDomObjectRequestType.md)|  | 

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

# **host_vsan_internal_system_run_vsan_physical_disk_diagnostics**
> List[HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult] host_vsan_internal_system_run_vsan_physical_disk_diagnostics(mo_id, run_vsan_physical_disk_diagnostics_request_type)

Runs diagnostics on VSAN physical disks. 

Runs diagnostics on VSAN physical disks.  This method takes an active approach and creates a minimal and temporary object on each physical MD disk consumed by VSAN across the entire VSAN cluster. The temporary objects are deleted right away upon completion of creation. The result returns a list of all checked MDs, indicating wheather or not there was a problem creating an object on that MD at the given point in time.  ***Since:*** vSphere API 5.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_vsan_internal_system_vsan_physical_disk_diagnostics_result import HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult
from vmware_vi.models.run_vsan_physical_disk_diagnostics_request_type import RunVsanPhysicalDiskDiagnosticsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    run_vsan_physical_disk_diagnostics_request_type = vmware_vi.RunVsanPhysicalDiskDiagnosticsRequestType() # RunVsanPhysicalDiskDiagnosticsRequestType | 

    try:
        # Runs diagnostics on VSAN physical disks. 
        api_response = api_instance.host_vsan_internal_system_run_vsan_physical_disk_diagnostics(mo_id, run_vsan_physical_disk_diagnostics_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_run_vsan_physical_disk_diagnostics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_run_vsan_physical_disk_diagnostics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **run_vsan_physical_disk_diagnostics_request_type** | [**RunVsanPhysicalDiskDiagnosticsRequestType**](RunVsanPhysicalDiskDiagnosticsRequestType.md)|  | 

### Return type

[**List[HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult]**](HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of result structures. One per checked disk.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_vsan_internal_system_upgrade_vsan_objects**
> List[HostVsanInternalSystemVsanObjectOperationResult] host_vsan_internal_system_upgrade_vsan_objects(mo_id, upgrade_vsan_objects_request_type)

Upgrade VSAN objects version. 

Upgrade VSAN objects version.  Upgrade a set of objects' version to new one in batch mode. API caller should limit the size of the inputs array, and suggested array size is 500 ~ 1000 initially. (The API will give more realistic suggestion after more experiments, then will apply hard limits in future)  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_vsan_internal_system_vsan_object_operation_result import HostVsanInternalSystemVsanObjectOperationResult
from vmware_vi.models.upgrade_vsan_objects_request_type import UpgradeVsanObjectsRequestType
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
    api_instance = vmware_vi.HostVsanInternalSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upgrade_vsan_objects_request_type = vmware_vi.UpgradeVsanObjectsRequestType() # UpgradeVsanObjectsRequestType | 

    try:
        # Upgrade VSAN objects version. 
        api_response = api_instance.host_vsan_internal_system_upgrade_vsan_objects(mo_id, upgrade_vsan_objects_request_type)
        print("The response of HostVsanInternalSystemApi->host_vsan_internal_system_upgrade_vsan_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVsanInternalSystemApi->host_vsan_internal_system_upgrade_vsan_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upgrade_vsan_objects_request_type** | [**UpgradeVsanObjectsRequestType**](UpgradeVsanObjectsRequestType.md)|  | 

### Return type

[**List[HostVsanInternalSystemVsanObjectOperationResult]**](HostVsanInternalSystemVsanObjectOperationResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of VsanObjectOperationResult, the array only contains result for failed objects, such as invalid or not existing UUID, upgrade failure, etc.  |  -  |
**500** | ***VsanFault***: for any unexpected failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

