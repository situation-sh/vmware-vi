# vmware_vi.HostPatchManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_patch_manager_check_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_check_host_patch_task) | **POST** /HostPatchManager/{moId}/CheckHostPatch_Task | Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned *Task* object. 
[**host_patch_manager_install_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_install_host_patch_task) | **POST** /HostPatchManager/{moId}/InstallHostPatch_Task | Patch the host. 
[**host_patch_manager_install_host_patch_v2_task**](HostPatchManagerApi.md#host_patch_manager_install_host_patch_v2_task) | **POST** /HostPatchManager/{moId}/InstallHostPatchV2_Task | Patch the host. 
[**host_patch_manager_query_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_query_host_patch_task) | **POST** /HostPatchManager/{moId}/QueryHostPatch_Task | Query the host for installed bulletins. 
[**host_patch_manager_scan_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_scan_host_patch_task) | **POST** /HostPatchManager/{moId}/ScanHostPatch_Task | Scan the host for the patch status. 
[**host_patch_manager_scan_host_patch_v2_task**](HostPatchManagerApi.md#host_patch_manager_scan_host_patch_v2_task) | **POST** /HostPatchManager/{moId}/ScanHostPatchV2_Task | Scan the host for the patch status. 
[**host_patch_manager_stage_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_stage_host_patch_task) | **POST** /HostPatchManager/{moId}/StageHostPatch_Task | Stage the vib files to esx local location and possibly do some run time check. 
[**host_patch_manager_uninstall_host_patch_task**](HostPatchManagerApi.md#host_patch_manager_uninstall_host_patch_task) | **POST** /HostPatchManager/{moId}/UninstallHostPatch_Task | Uninstall patch from the host. 


# **host_patch_manager_check_host_patch_task**
> ManagedObjectReference host_patch_manager_check_host_patch_task(mo_id, check_host_patch_request_type)

Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned *Task* object. 

Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned *Task* object.  No integrity checks are performed on the metadata.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_host_patch_request_type import CheckHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_host_patch_request_type = vmware_vi.CheckHostPatchRequestType() # CheckHostPatchRequestType | 

    try:
        # Check the list of metadata and returns the dependency, obsolete and conflict information The operation is cancelable through the returned *Task* object. 
        api_response = api_instance.host_patch_manager_check_host_patch_task(mo_id, check_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_check_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_check_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_host_patch_request_type** | [**CheckHostPatchRequestType**](CheckHostPatchRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostPatchManagerStatus* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***RequestCanceled***: if the operation is canceled.  ***InvalidState***: if the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_install_host_patch_task**
> ManagedObjectReference host_patch_manager_install_host_patch_task(mo_id, install_host_patch_request_type)

Patch the host. 

Deprecated method is deprecated, use *HostPatchManager.InstallHostPatchV2_Task* instead.  Patch the host.  The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see *PatchInstallFailed* for details.  ***Required privileges:*** Host.Config.Patch 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.install_host_patch_request_type import InstallHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    install_host_patch_request_type = vmware_vi.InstallHostPatchRequestType() # InstallHostPatchRequestType | 

    try:
        # Patch the host. 
        api_response = api_instance.host_patch_manager_install_host_patch_task(mo_id, install_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_install_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_install_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **install_host_patch_request_type** | [**InstallHostPatchRequestType**](InstallHostPatchRequestType.md)|  | 

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
**500** | ***PatchMetadataInvalid***: if the required metadata is invalid - for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.  ***PatchBinariesNotFound***: if required update related binaries were not available.  ***PatchNotApplicable***: if the patch is not applicable. Typically a more specific subclass of PatchNotApplicable is thrown to indicate a specific problem - for example, PatchSuperseded if the patch is superseded, MissingDependency if required patch or libraries are not installed, AlreadyInstalled if the patch is already installed.  ***NoDiskSpace***: if the update can not be installed because there is insufficient disk space for the installation, including temporary space used for rollback.  ***PatchInstallFailed***: if the installation failed, *PlatformConfigFault.text* has details of the failure. Automatic rollback might have succeeded or failed.  ***RebootRequired***: if the update cannot be installed without restarting the host. This might occur on account of a prior update installation which needed to be installed separately from other updates.  ***InvalidState***: if the host is not in maintenance mode but the patch install requires all virtual machines to be powered off.  ***TaskInProgress***: if there is already a patch installation in progress.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_install_host_patch_v2_task**
> ManagedObjectReference host_patch_manager_install_host_patch_v2_task(mo_id, install_host_patch_v2_request_type)

Patch the host. 

Patch the host.  The operation is not cancelable. If the patch installation failed, an atomic rollback of the installation will be attempted. Manual rollback is required if the atomic rollback failed, see *PatchInstallFailed* for details.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Patch 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.install_host_patch_v2_request_type import InstallHostPatchV2RequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    install_host_patch_v2_request_type = vmware_vi.InstallHostPatchV2RequestType() # InstallHostPatchV2RequestType | 

    try:
        # Patch the host. 
        api_response = api_instance.host_patch_manager_install_host_patch_v2_task(mo_id, install_host_patch_v2_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_install_host_patch_v2_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_install_host_patch_v2_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **install_host_patch_v2_request_type** | [**InstallHostPatchV2RequestType**](InstallHostPatchV2RequestType.md)|  | 

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
**500** | ***RequestCanceled***: if the operation is canceled.  ***InvalidState***: if the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_query_host_patch_task**
> ManagedObjectReference host_patch_manager_query_host_patch_task(mo_id, query_host_patch_request_type)

Query the host for installed bulletins. 

Query the host for installed bulletins.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.query_host_patch_request_type import QueryHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_host_patch_request_type = vmware_vi.QueryHostPatchRequestType() # QueryHostPatchRequestType | 

    try:
        # Query the host for installed bulletins. 
        api_response = api_instance.host_patch_manager_query_host_patch_task(mo_id, query_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_query_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_query_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_host_patch_request_type** | [**QueryHostPatchRequestType**](QueryHostPatchRequestType.md)|  | 

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
**500** | ***RequestCanceled***: if the operation is canceled.  ***InvalidState***: if the bulletin ID did not exist.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_scan_host_patch_task**
> ManagedObjectReference host_patch_manager_scan_host_patch_task(mo_id, scan_host_patch_request_type)

Scan the host for the patch status. 

Deprecated as of VI API 4.0, use *HostPatchManager.ScanHostPatchV2_Task*.  Scan the host for the patch status.  The operation is cancelable through the returned *Task* object. Integrity checks are performed on the metadata only during the scan operation.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.scan_host_patch_request_type import ScanHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    scan_host_patch_request_type = vmware_vi.ScanHostPatchRequestType() # ScanHostPatchRequestType | 

    try:
        # Scan the host for the patch status. 
        api_response = api_instance.host_patch_manager_scan_host_patch_task(mo_id, scan_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_scan_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_scan_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **scan_host_patch_request_type** | [**ScanHostPatchRequestType**](ScanHostPatchRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostPatchManagerStatus* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***RequestCanceled***: if the operation is canceled.  ***PatchMetadataInvalid***: if query required metadata is invalid - for example, it is not found in the repository, is corrupted and so on. Typically a more specific subclass of PatchMetadataInvalid is thrown.  ***PlatformConfigFault***: if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See *PlatformConfigFault.text* for specific details.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_scan_host_patch_v2_task**
> ManagedObjectReference host_patch_manager_scan_host_patch_v2_task(mo_id, scan_host_patch_v2_request_type)

Scan the host for the patch status. 

Scan the host for the patch status.  The operation is cancelable through the returned *Task* object. Integrity checks are performed on the metadata only during the scan operation.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.scan_host_patch_v2_request_type import ScanHostPatchV2RequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    scan_host_patch_v2_request_type = vmware_vi.ScanHostPatchV2RequestType() # ScanHostPatchV2RequestType | 

    try:
        # Scan the host for the patch status. 
        api_response = api_instance.host_patch_manager_scan_host_patch_v2_task(mo_id, scan_host_patch_v2_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_scan_host_patch_v2_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_scan_host_patch_v2_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **scan_host_patch_v2_request_type** | [**ScanHostPatchV2RequestType**](ScanHostPatchV2RequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostPatchManagerStatus* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***RequestCanceled***: if the operation is canceled.  ***InvalidState***: if the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if there is any error in the repository access, metadata download, repository level integrity check, or reading the metadata. See *PlatformConfigFault.text* for specific details.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_stage_host_patch_task**
> ManagedObjectReference host_patch_manager_stage_host_patch_task(mo_id, stage_host_patch_request_type)

Stage the vib files to esx local location and possibly do some run time check. 

Stage the vib files to esx local location and possibly do some run time check.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Patch 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.stage_host_patch_request_type import StageHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    stage_host_patch_request_type = vmware_vi.StageHostPatchRequestType() # StageHostPatchRequestType | 

    try:
        # Stage the vib files to esx local location and possibly do some run time check. 
        api_response = api_instance.host_patch_manager_stage_host_patch_task(mo_id, stage_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_stage_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_stage_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **stage_host_patch_request_type** | [**StageHostPatchRequestType**](StageHostPatchRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the *HostPatchManagerStatus* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***RequestCanceled***: if the operation is canceled.  ***InvalidState***: if the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_patch_manager_uninstall_host_patch_task**
> ManagedObjectReference host_patch_manager_uninstall_host_patch_task(mo_id, uninstall_host_patch_request_type)

Uninstall patch from the host. 

Uninstall patch from the host.  The operation is not cancelable.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Patch 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.uninstall_host_patch_request_type import UninstallHostPatchRequestType
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
    api_instance = vmware_vi.HostPatchManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    uninstall_host_patch_request_type = vmware_vi.UninstallHostPatchRequestType() # UninstallHostPatchRequestType | 

    try:
        # Uninstall patch from the host. 
        api_response = api_instance.host_patch_manager_uninstall_host_patch_task(mo_id, uninstall_host_patch_request_type)
        print("The response of HostPatchManagerApi->host_patch_manager_uninstall_host_patch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPatchManagerApi->host_patch_manager_uninstall_host_patch_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **uninstall_host_patch_request_type** | [**UninstallHostPatchRequestType**](UninstallHostPatchRequestType.md)|  | 

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
**500** | ***InvalidState***: if the feature cannot be supported on the platform, potentially because the hardware configuration does not support it.  ***TaskInProgress***: if there is already a patch installation in progress.  ***PlatformConfigFault***: if any error occurs during the operation. More detailed information will be returned within the payload of the exception as xml string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

