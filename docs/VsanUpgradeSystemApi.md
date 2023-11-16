# vmware_vi.VsanUpgradeSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vsan_upgrade_system_perform_vsan_upgrade_preflight_check**](VsanUpgradeSystemApi.md#vsan_upgrade_system_perform_vsan_upgrade_preflight_check) | **POST** /VsanUpgradeSystem/{moId}/PerformVsanUpgradePreflightCheck | Perform an upgrade pre-flight check on a cluster. 
[**vsan_upgrade_system_perform_vsan_upgrade_task**](VsanUpgradeSystemApi.md#vsan_upgrade_system_perform_vsan_upgrade_task) | **POST** /VsanUpgradeSystem/{moId}/PerformVsanUpgrade_Task | Start VSAN on-disk format upgrade process on a particular cluster. 
[**vsan_upgrade_system_query_vsan_upgrade_status**](VsanUpgradeSystemApi.md#vsan_upgrade_system_query_vsan_upgrade_status) | **POST** /VsanUpgradeSystem/{moId}/QueryVsanUpgradeStatus | Retrieve the latest status of a running, or the previously completed, upgrade process. 


# **vsan_upgrade_system_perform_vsan_upgrade_preflight_check**
> VsanUpgradeSystemPreflightCheckResult vsan_upgrade_system_perform_vsan_upgrade_preflight_check(mo_id, perform_vsan_upgrade_preflight_check_request_type)

Perform an upgrade pre-flight check on a cluster. 

Perform an upgrade pre-flight check on a cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.perform_vsan_upgrade_preflight_check_request_type import PerformVsanUpgradePreflightCheckRequestType
from vmware_vi.models.vsan_upgrade_system_preflight_check_result import VsanUpgradeSystemPreflightCheckResult
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
    api_instance = vmware_vi.VsanUpgradeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    perform_vsan_upgrade_preflight_check_request_type = vmware_vi.PerformVsanUpgradePreflightCheckRequestType() # PerformVsanUpgradePreflightCheckRequestType | 

    try:
        # Perform an upgrade pre-flight check on a cluster. 
        api_response = api_instance.vsan_upgrade_system_perform_vsan_upgrade_preflight_check(mo_id, perform_vsan_upgrade_preflight_check_request_type)
        print("The response of VsanUpgradeSystemApi->vsan_upgrade_system_perform_vsan_upgrade_preflight_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsanUpgradeSystemApi->vsan_upgrade_system_perform_vsan_upgrade_preflight_check: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **perform_vsan_upgrade_preflight_check_request_type** | [**PerformVsanUpgradePreflightCheckRequestType**](PerformVsanUpgradePreflightCheckRequestType.md)|  | 

### Return type

[**VsanUpgradeSystemPreflightCheckResult**](VsanUpgradeSystemPreflightCheckResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pre-flight check result.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vsan_upgrade_system_perform_vsan_upgrade_task**
> ManagedObjectReference vsan_upgrade_system_perform_vsan_upgrade_task(mo_id, perform_vsan_upgrade_request_type)

Start VSAN on-disk format upgrade process on a particular cluster. 

Start VSAN on-disk format upgrade process on a particular cluster.  In order to perform this on-disk format upgrade, the upgrade process will perform a rolling evacuation/remove/re-add operation to accomplish the upgrade. In other words, one disk group at a time, it will evacuate the data from the disk group, then remove the old format from the now empty disk group, then reformat the disk group with the new format. Once all disk groups have been upgraded, and if the performObjectUpgrade parameter is set, the VSAN object version is also upgraded. Before the object version is upgraded, it is possible to downgrade the cluster by passing the downgradeFormat parameter. Once objects are of the new object version however, downgrade (and thus rollback) are no longer possible. The new object version is required to allow objects to benefit from new VSAN features. This is a long running (hours to days) task. In addition to normal task progress reporting, use the queryUpgradeStatus() API which allows to retrieve in-depth status updates from the upgrade process. In there will be a detailed log of every operation the upgrade process has taken or issues it encountered. Some are simple log messages, others refer to operations like evacuating a disk group. For such log entries, the task object of the evacuation task is provided to allow \"sub-task\" tracking. Before starting, the upgrade process will perform a pre-flight check, and abort if any of the pre-conditions are not met. See  See also *VsanUpgradeSystem.PerformVsanUpgradePreflightCheck*for details on the pre-conditions being checked for. The upgrade process performs additional \"pre-flight checks\" before proceeding to upgrade the next host. The upgrade process will be halted if any of those pre-flight checks fail. If the upgrade process has been halted due to a problem, or even due to a crash or other failure, it can be re-started at any point in time. The upgrade will resume where it left off and only do the parts that are still outstanding. If the upgrade process stopped after removing VSAN from a disk group, but before re-adding those disks to VSAN, the upgrade process can recover from that. The pre-flight check results indicate such a condition. The upgrade process will however only re-add those disks if the restoreBackup parameter is passed in as true. Privilege \"Host.Config.Storage\" on all hosts under specified cluster is required..  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.perform_vsan_upgrade_request_type import PerformVsanUpgradeRequestType
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
    api_instance = vmware_vi.VsanUpgradeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    perform_vsan_upgrade_request_type = vmware_vi.PerformVsanUpgradeRequestType() # PerformVsanUpgradeRequestType | 

    try:
        # Start VSAN on-disk format upgrade process on a particular cluster. 
        api_response = api_instance.vsan_upgrade_system_perform_vsan_upgrade_task(mo_id, perform_vsan_upgrade_request_type)
        print("The response of VsanUpgradeSystemApi->vsan_upgrade_system_perform_vsan_upgrade_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsanUpgradeSystemApi->vsan_upgrade_system_perform_vsan_upgrade_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **perform_vsan_upgrade_request_type** | [**PerformVsanUpgradeRequestType**](PerformVsanUpgradeRequestType.md)|  | 

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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vsan_upgrade_system_query_vsan_upgrade_status**
> VsanUpgradeSystemUpgradeStatus vsan_upgrade_system_query_vsan_upgrade_status(mo_id, query_vsan_upgrade_status_request_type)

Retrieve the latest status of a running, or the previously completed, upgrade process. 

Retrieve the latest status of a running, or the previously completed, upgrade process.  Information about previous upgrade runs are not always, e.g. when VC gets restarted.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_vsan_upgrade_status_request_type import QueryVsanUpgradeStatusRequestType
from vmware_vi.models.vsan_upgrade_system_upgrade_status import VsanUpgradeSystemUpgradeStatus
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
    api_instance = vmware_vi.VsanUpgradeSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_vsan_upgrade_status_request_type = vmware_vi.QueryVsanUpgradeStatusRequestType() # QueryVsanUpgradeStatusRequestType | 

    try:
        # Retrieve the latest status of a running, or the previously completed, upgrade process. 
        api_response = api_instance.vsan_upgrade_system_query_vsan_upgrade_status(mo_id, query_vsan_upgrade_status_request_type)
        print("The response of VsanUpgradeSystemApi->vsan_upgrade_system_query_vsan_upgrade_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VsanUpgradeSystemApi->vsan_upgrade_system_query_vsan_upgrade_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_vsan_upgrade_status_request_type** | [**QueryVsanUpgradeStatusRequestType**](QueryVsanUpgradeStatusRequestType.md)|  | 

### Return type

[**VsanUpgradeSystemUpgradeStatus**](VsanUpgradeSystemUpgradeStatus.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

