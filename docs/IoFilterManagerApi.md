# vmware_vi.IoFilterManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**io_filter_manager_install_io_filter_task**](IoFilterManagerApi.md#io_filter_manager_install_io_filter_task) | **POST** /IoFilterManager/{moId}/InstallIoFilter_Task | Install an IO Filter on a compute resource. 
[**io_filter_manager_query_disks_using_filter**](IoFilterManagerApi.md#io_filter_manager_query_disks_using_filter) | **POST** /IoFilterManager/{moId}/QueryDisksUsingFilter | Return the list of virtual disks that use an IO Filter installed on a compute resource. 
[**io_filter_manager_query_io_filter_info**](IoFilterManagerApi.md#io_filter_manager_query_io_filter_info) | **POST** /IoFilterManager/{moId}/QueryIoFilterInfo | Return the information for the IO Filters that are installed on the cluster. 
[**io_filter_manager_query_io_filter_issues**](IoFilterManagerApi.md#io_filter_manager_query_io_filter_issues) | **POST** /IoFilterManager/{moId}/QueryIoFilterIssues | Return the issues that occurred during the last installation/uninstallation/upgrade operation of an IO Filter on a compute resource. 
[**io_filter_manager_resolve_installation_errors_on_cluster_task**](IoFilterManagerApi.md#io_filter_manager_resolve_installation_errors_on_cluster_task) | **POST** /IoFilterManager/{moId}/ResolveInstallationErrorsOnCluster_Task | Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a cluster. 
[**io_filter_manager_resolve_installation_errors_on_host_task**](IoFilterManagerApi.md#io_filter_manager_resolve_installation_errors_on_host_task) | **POST** /IoFilterManager/{moId}/ResolveInstallationErrorsOnHost_Task | Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a host. 
[**io_filter_manager_uninstall_io_filter_task**](IoFilterManagerApi.md#io_filter_manager_uninstall_io_filter_task) | **POST** /IoFilterManager/{moId}/UninstallIoFilter_Task | Uninstall an IO Filter from a compute resource. 
[**io_filter_manager_upgrade_io_filter_task**](IoFilterManagerApi.md#io_filter_manager_upgrade_io_filter_task) | **POST** /IoFilterManager/{moId}/UpgradeIoFilter_Task | Upgrade an IO Filter on a compute resource. 


# **io_filter_manager_install_io_filter_task**
> ManagedObjectReference io_filter_manager_install_io_filter_task(mo_id, install_io_filter_request_type)

Install an IO Filter on a compute resource. 

Install an IO Filter on a compute resource.  IO Filters can only be installed on a cluster.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.install_io_filter_request_type import InstallIoFilterRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    install_io_filter_request_type = vmware_vi.InstallIoFilterRequestType() # InstallIoFilterRequestType | 

    try:
        # Install an IO Filter on a compute resource. 
        api_response = api_instance.io_filter_manager_install_io_filter_task(mo_id, install_io_filter_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_install_io_filter_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_install_io_filter_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **install_io_filter_request_type** | [**InstallIoFilterRequestType**](InstallIoFilterRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task is set to success if the filter is installed on all the hosts in the compute resource successfully. If the task fails, first check *TaskInfo.error* to see the error. If the error indicates that installation has failed on the hosts, use *IoFilterManager.QueryIoFilterIssues* to get the detailed errors occurred during installation on each host.  The dynamic privilege check ensures that the user must have Host.Config.Patch privilege for all the hosts in the compute resource.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if \&quot;compRes\&quot; is a standalone host.  ***AlreadyExists***: if another VIB with the same name and vendor has been installed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_query_disks_using_filter**
> List[VirtualDiskId] io_filter_manager_query_disks_using_filter(mo_id, query_disks_using_filter_request_type)

Return the list of virtual disks that use an IO Filter installed on a compute resource. 

Return the list of virtual disks that use an IO Filter installed on a compute resource.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_disks_using_filter_request_type import QueryDisksUsingFilterRequestType
from vmware_vi.models.virtual_disk_id import VirtualDiskId
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_disks_using_filter_request_type = vmware_vi.QueryDisksUsingFilterRequestType() # QueryDisksUsingFilterRequestType | 

    try:
        # Return the list of virtual disks that use an IO Filter installed on a compute resource. 
        api_response = api_instance.io_filter_manager_query_disks_using_filter(mo_id, query_disks_using_filter_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_query_disks_using_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_query_disks_using_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_disks_using_filter_request_type** | [**QueryDisksUsingFilterRequestType**](QueryDisksUsingFilterRequestType.md)|  | 

### Return type

[**List[VirtualDiskId]**](VirtualDiskId.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of *VirtualDiskId* objects that use the given IO Filter installed on the compute resource.  |  -  |
**500** | ***NotFound***: if the filter specified by \&quot;filterId\&quot; is not installed on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_query_io_filter_info**
> List[ClusterIoFilterInfo] io_filter_manager_query_io_filter_info(mo_id, query_io_filter_info_request_type)

Return the information for the IO Filters that are installed on the cluster. 

Return the information for the IO Filters that are installed on the cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_io_filter_info import ClusterIoFilterInfo
from vmware_vi.models.query_io_filter_info_request_type import QueryIoFilterInfoRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_io_filter_info_request_type = vmware_vi.QueryIoFilterInfoRequestType() # QueryIoFilterInfoRequestType | 

    try:
        # Return the information for the IO Filters that are installed on the cluster. 
        api_response = api_instance.io_filter_manager_query_io_filter_info(mo_id, query_io_filter_info_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_query_io_filter_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_query_io_filter_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_io_filter_info_request_type** | [**QueryIoFilterInfoRequestType**](QueryIoFilterInfoRequestType.md)|  | 

### Return type

[**List[ClusterIoFilterInfo]**](ClusterIoFilterInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of *ClusterIoFilterInfo* objects that contain the information for the IO Filters that are installed on the compute resource.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_query_io_filter_issues**
> IoFilterQueryIssueResult io_filter_manager_query_io_filter_issues(mo_id, query_io_filter_issues_request_type)

Return the issues that occurred during the last installation/uninstallation/upgrade operation of an IO Filter on a compute resource. 

Return the issues that occurred during the last installation/uninstallation/upgrade operation of an IO Filter on a compute resource.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.io_filter_query_issue_result import IoFilterQueryIssueResult
from vmware_vi.models.query_io_filter_issues_request_type import QueryIoFilterIssuesRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_io_filter_issues_request_type = vmware_vi.QueryIoFilterIssuesRequestType() # QueryIoFilterIssuesRequestType | 

    try:
        # Return the issues that occurred during the last installation/uninstallation/upgrade operation of an IO Filter on a compute resource. 
        api_response = api_instance.io_filter_manager_query_io_filter_issues(mo_id, query_io_filter_issues_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_query_io_filter_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_query_io_filter_issues: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_io_filter_issues_request_type** | [**QueryIoFilterIssuesRequestType**](QueryIoFilterIssuesRequestType.md)|  | 

### Return type

[**IoFilterQueryIssueResult**](IoFilterQueryIssueResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A *IoFilterQueryIssueResult* object.  |  -  |
**500** | ***NotFound***: if the filter specified by \&quot;filterId\&quot; is not installed on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_resolve_installation_errors_on_cluster_task**
> ManagedObjectReference io_filter_manager_resolve_installation_errors_on_cluster_task(mo_id, resolve_installation_errors_on_cluster_request_type)

Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a cluster. 

Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a cluster.  Depending on the nature of the installation failure, vCenter will take the appropriate actions to resolve it. For example, retry or resume installation.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.resolve_installation_errors_on_cluster_request_type import ResolveInstallationErrorsOnClusterRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    resolve_installation_errors_on_cluster_request_type = vmware_vi.ResolveInstallationErrorsOnClusterRequestType() # ResolveInstallationErrorsOnClusterRequestType | 

    try:
        # Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a cluster. 
        api_response = api_instance.io_filter_manager_resolve_installation_errors_on_cluster_task(mo_id, resolve_installation_errors_on_cluster_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_resolve_installation_errors_on_cluster_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_resolve_installation_errors_on_cluster_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **resolve_installation_errors_on_cluster_request_type** | [**ResolveInstallationErrorsOnClusterRequestType**](ResolveInstallationErrorsOnClusterRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task is set to success if all the errors related to the filter are resolved on the cluster. If the task fails, first check *TaskInfo.error* to see the error. If the error indicates that issues persist on the cluster, use *IoFilterManager.QueryIoFilterIssues* to get the detailed errors on the hosts in the cluster.  The dynamic privilege check will ensure that the appropriate privileges must be acquired for all the hosts in the cluster based on the remediation actions. For example, Host.Config.Maintenance privilege and Host.Config.Patch privileges must be required for upgrading a VIB.  Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the filter specified by \&quot;filterId\&quot; is not installed on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_resolve_installation_errors_on_host_task**
> ManagedObjectReference io_filter_manager_resolve_installation_errors_on_host_task(mo_id, resolve_installation_errors_on_host_request_type)

Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a host. 

Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a host.  Depending on the nature of the installation failure, vCenter will take the appropriate actions to resolve it. For example, retry or resume installation.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.resolve_installation_errors_on_host_request_type import ResolveInstallationErrorsOnHostRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    resolve_installation_errors_on_host_request_type = vmware_vi.ResolveInstallationErrorsOnHostRequestType() # ResolveInstallationErrorsOnHostRequestType | 

    try:
        # Resolve the errors occurred during an installation/uninstallation/upgrade operation of an IO Filter on a host. 
        api_response = api_instance.io_filter_manager_resolve_installation_errors_on_host_task(mo_id, resolve_installation_errors_on_host_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_resolve_installation_errors_on_host_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_resolve_installation_errors_on_host_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **resolve_installation_errors_on_host_request_type** | [**ResolveInstallationErrorsOnHostRequestType**](ResolveInstallationErrorsOnHostRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task is set to success if all the errors related to the filter are resolved on the host. If the task fails, first check *TaskInfo.error* to see the error. If the error indicates that issues persist on the host, use *IoFilterManager.QueryIoFilterIssues* to get the detailed errors on the host.  The dynamic privilege check will ensure that the appropriate privileges are acquired based on the remediation actions. For example, Host.Config.Maintenance and Host.Config.Patch privilege must required for upgrading a VIB.  Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the filter specified by \&quot;filterId\&quot; is not installed on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_uninstall_io_filter_task**
> ManagedObjectReference io_filter_manager_uninstall_io_filter_task(mo_id, uninstall_io_filter_request_type)

Uninstall an IO Filter from a compute resource. 

Uninstall an IO Filter from a compute resource.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.uninstall_io_filter_request_type import UninstallIoFilterRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    uninstall_io_filter_request_type = vmware_vi.UninstallIoFilterRequestType() # UninstallIoFilterRequestType | 

    try:
        # Uninstall an IO Filter from a compute resource. 
        api_response = api_instance.io_filter_manager_uninstall_io_filter_task(mo_id, uninstall_io_filter_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_uninstall_io_filter_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_uninstall_io_filter_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **uninstall_io_filter_request_type** | [**UninstallIoFilterRequestType**](UninstallIoFilterRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task is set to success if the filter is uninstalled from all the hosts in the compute resource successfully. If the task fails, first check *TaskInfo.error* to see the error. If the error indicates that uninstallation has failed on the hosts, use *IoFilterManager.QueryIoFilterIssues* to get the detailed errors occurred during uninstallation on each host.  The dynamic privilege check ensures that the user must have Host.Config.Maintenance and Host.Config.Patch privilege for all the hosts in the compute resource.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if \&quot;compRes\&quot; is a standalone host.  ***NotFound***: if the filter is not installed on the cluster.  ***FilterInUse***: if the filter to be uninstalled is being used by a virtual disk.  ***InvalidState***: if \&quot;compRes\&quot; is a cluster and DRS is disabled on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_filter_manager_upgrade_io_filter_task**
> ManagedObjectReference io_filter_manager_upgrade_io_filter_task(mo_id, upgrade_io_filter_request_type)

Upgrade an IO Filter on a compute resource. 

Upgrade an IO Filter on a compute resource.  ***Since:*** vSphere API 6.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.upgrade_io_filter_request_type import UpgradeIoFilterRequestType
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
    api_instance = vmware_vi.IoFilterManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upgrade_io_filter_request_type = vmware_vi.UpgradeIoFilterRequestType() # UpgradeIoFilterRequestType | 

    try:
        # Upgrade an IO Filter on a compute resource. 
        api_response = api_instance.io_filter_manager_upgrade_io_filter_task(mo_id, upgrade_io_filter_request_type)
        print("The response of IoFilterManagerApi->io_filter_manager_upgrade_io_filter_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IoFilterManagerApi->io_filter_manager_upgrade_io_filter_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upgrade_io_filter_request_type** | [**UpgradeIoFilterRequestType**](UpgradeIoFilterRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The task is set to success if all the hosts in the compute resource are upgraded successfully. If the task fails, first check *TaskInfo.error* to see the error. If the error indicates that upgrade has failed on the hosts, use *IoFilterManager.QueryIoFilterIssues* to get the detailed errors occurred during upgrade on each host.  The dynamic privilege check ensures that the user must have Host.Config.Maintenance and Host.Config.Patch privileges for all the hosts in the compute resource.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if \&quot;compRes\&quot; is a standalone host; or if the VIB package pointed by \&quot;vibUrl\&quot; is not an upgrade of the IO Filter specified by \&quot;filterId\&quot;.  ***NotFound***: if the filter specified by \&quot;filterId\&quot; is not installed on the cluster.  ***InvalidState***: if \&quot;compRes\&quot; is a cluster and DRS is disabled on the cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

