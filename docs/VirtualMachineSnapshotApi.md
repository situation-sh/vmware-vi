# vmware_vi.VirtualMachineSnapshotApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_snapshot_export_snapshot**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_export_snapshot) | **POST** /VirtualMachineSnapshot/{moId}/ExportSnapshot | Obtains an export lease on this snapshot. 
[**virtual_machine_snapshot_get_available_field**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_get_available_field) | **GET** /VirtualMachineSnapshot/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**virtual_machine_snapshot_get_child_snapshot**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_get_child_snapshot) | **GET** /VirtualMachineSnapshot/{moId}/childSnapshot | All snapshots for which this snapshot is the parent. 
[**virtual_machine_snapshot_get_config**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_get_config) | **GET** /VirtualMachineSnapshot/{moId}/config | Information about the configuration of this virtual machine when this snapshot was taken. 
[**virtual_machine_snapshot_get_value**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_get_value) | **GET** /VirtualMachineSnapshot/{moId}/value | List of custom field values. 
[**virtual_machine_snapshot_get_vm**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_get_vm) | **GET** /VirtualMachineSnapshot/{moId}/vm | The virtual machine for which the snapshot was taken. 
[**virtual_machine_snapshot_remove_snapshot_task**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_remove_snapshot_task) | **POST** /VirtualMachineSnapshot/{moId}/RemoveSnapshot_Task | Removes this snapshot and deletes any associated storage. 
[**virtual_machine_snapshot_rename_snapshot**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_rename_snapshot) | **POST** /VirtualMachineSnapshot/{moId}/RenameSnapshot | Rename this snapshot with either a new name or a new description or both. 
[**virtual_machine_snapshot_revert_to_snapshot_task**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_revert_to_snapshot_task) | **POST** /VirtualMachineSnapshot/{moId}/RevertToSnapshot_Task | Change the execution state of the virtual machine to the state of this snapshot. 
[**virtual_machine_snapshot_set_custom_value**](VirtualMachineSnapshotApi.md#virtual_machine_snapshot_set_custom_value) | **POST** /VirtualMachineSnapshot/{moId}/setCustomValue | Assigns a value to a custom field. 


# **virtual_machine_snapshot_export_snapshot**
> ManagedObjectReference virtual_machine_snapshot_export_snapshot(mo_id)

Obtains an export lease on this snapshot. 

Obtains an export lease on this snapshot.  The export lease contains a list of URLs for the virtual disks for this snapshot, as well as a ticket giving access to the URLs.  See *HttpNfcLease* for information on how to use the lease.  ***Since:*** vSphere API 5.5  ***Required privileges:*** VApp.Export 

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Obtains an export lease on this snapshot. 
        api_response = api_instance.virtual_machine_snapshot_export_snapshot(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_export_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_export_snapshot: %s\n" % e)
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
**200** | The export lease on this *VirtualMachineSnapshot*. The export task continues running until the lease is completed by the caller.  Refers instance of *HttpNfcLease*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***FileFault***: if there is an error accessing the virtual machine files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_get_available_field**
> List[CustomFieldDef] virtual_machine_snapshot_get_available_field(mo_id)

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.virtual_machine_snapshot_get_available_field(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_get_available_field: %s\n" % e)
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

# **virtual_machine_snapshot_get_child_snapshot**
> List[ManagedObjectReference] virtual_machine_snapshot_get_child_snapshot(mo_id)

All snapshots for which this snapshot is the parent. 

All snapshots for which this snapshot is the parent.  ***Since:*** vSphere API 4.1 

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # All snapshots for which this snapshot is the parent. 
        api_response = api_instance.virtual_machine_snapshot_get_child_snapshot(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_get_child_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_get_child_snapshot: %s\n" % e)
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
**200** | Refers instances of *VirtualMachineSnapshot*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_get_config**
> VirtualMachineConfigInfo virtual_machine_snapshot_get_config(mo_id)

Information about the configuration of this virtual machine when this snapshot was taken. 

Information about the configuration of this virtual machine when this snapshot was taken.  The datastore paths for the virtual machine disks point to the head of the disk chain that represents the disk at this given snapshot. The fileInfo.fileLayout field is not set. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_config_info import VirtualMachineConfigInfo
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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about the configuration of this virtual machine when this snapshot was taken. 
        api_response = api_instance.virtual_machine_snapshot_get_config(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineConfigInfo**](VirtualMachineConfigInfo.md)

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

# **virtual_machine_snapshot_get_value**
> List[CustomFieldValue] virtual_machine_snapshot_get_value(mo_id)

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.virtual_machine_snapshot_get_value(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_get_value: %s\n" % e)
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

# **virtual_machine_snapshot_get_vm**
> ManagedObjectReference virtual_machine_snapshot_get_vm(mo_id)

The virtual machine for which the snapshot was taken. 

The virtual machine for which the snapshot was taken.  ***Since:*** vSphere API 6.0 

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The virtual machine for which the snapshot was taken. 
        api_response = api_instance.virtual_machine_snapshot_get_vm(mo_id)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_get_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_get_vm: %s\n" % e)
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
**200** | Refers instance of *VirtualMachine*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_remove_snapshot_task**
> ManagedObjectReference virtual_machine_snapshot_remove_snapshot_task(mo_id, remove_snapshot_request_type)

Removes this snapshot and deletes any associated storage. 

Removes this snapshot and deletes any associated storage.  ***Required privileges:*** VirtualMachine.State.RemoveSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.remove_snapshot_request_type import RemoveSnapshotRequestType
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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_snapshot_request_type = vmware_vi.RemoveSnapshotRequestType() # RemoveSnapshotRequestType | 

    try:
        # Removes this snapshot and deletes any associated storage. 
        api_response = api_instance.virtual_machine_snapshot_remove_snapshot_task(mo_id, remove_snapshot_request_type)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_remove_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_remove_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_snapshot_request_type** | [**RemoveSnapshotRequestType**](RemoveSnapshotRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_rename_snapshot**
> virtual_machine_snapshot_rename_snapshot(mo_id, rename_snapshot_request_type)

Rename this snapshot with either a new name or a new description or both. 

Rename this snapshot with either a new name or a new description or both.  At least one of these must be specified when calling the rename method.  ***Required privileges:*** VirtualMachine.State.RenameSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.rename_snapshot_request_type import RenameSnapshotRequestType
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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_snapshot_request_type = vmware_vi.RenameSnapshotRequestType() # RenameSnapshotRequestType | 

    try:
        # Rename this snapshot with either a new name or a new description or both. 
        api_instance.virtual_machine_snapshot_rename_snapshot(mo_id, rename_snapshot_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_rename_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_snapshot_request_type** | [**RenameSnapshotRequestType**](RenameSnapshotRequestType.md)|  | 

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
**500** | ***NotSupported***: if the host product does not support snapshot rename.  ***InvalidName***: if the specified snapshot name is not valid.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed in the current state of the virtual machine. For example, the virtual machine&#39;s configuration is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_revert_to_snapshot_task**
> ManagedObjectReference virtual_machine_snapshot_revert_to_snapshot_task(mo_id, revert_to_snapshot_request_type)

Change the execution state of the virtual machine to the state of this snapshot. 

Change the execution state of the virtual machine to the state of this snapshot.  ***Required privileges:*** VirtualMachine.State.RevertToSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.revert_to_snapshot_request_type import RevertToSnapshotRequestType
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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    revert_to_snapshot_request_type = vmware_vi.RevertToSnapshotRequestType() # RevertToSnapshotRequestType | 

    try:
        # Change the execution state of the virtual machine to the state of this snapshot. 
        api_response = api_instance.virtual_machine_snapshot_revert_to_snapshot_task(mo_id, revert_to_snapshot_request_type)
        print("The response of VirtualMachineSnapshotApi->virtual_machine_snapshot_revert_to_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_revert_to_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **revert_to_snapshot_request_type** | [**RevertToSnapshotRequestType**](RevertToSnapshotRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support snapshots.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed in the current state of the virtual machine. For example, the virtual machine&#39;s configuration is not available.  ***VmConfigFault***: if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_snapshot_set_custom_value**
> virtual_machine_snapshot_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.VirtualMachineSnapshotApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.virtual_machine_snapshot_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineSnapshotApi->virtual_machine_snapshot_set_custom_value: %s\n" % e)
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

