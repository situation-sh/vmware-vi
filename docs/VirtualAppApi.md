# vmware_vi.VirtualAppApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_app_clone_v_app_task**](VirtualAppApi.md#virtual_app_clone_v_app_task) | **POST** /VirtualApp/{moId}/CloneVApp_Task | Creates a clone of this vApp. 
[**virtual_app_create_child_vm_task**](VirtualAppApi.md#virtual_app_create_child_vm_task) | **POST** /VirtualApp/{moId}/CreateChildVM_Task | Creates a new virtual machine in a vApp container. 
[**virtual_app_create_resource_pool**](VirtualAppApi.md#virtual_app_create_resource_pool) | **POST** /VirtualApp/{moId}/CreateResourcePool | Creates a new resource pool. 
[**virtual_app_create_v_app**](VirtualAppApi.md#virtual_app_create_v_app) | **POST** /VirtualApp/{moId}/CreateVApp | Creates a new vApp container. 
[**virtual_app_destroy_children**](VirtualAppApi.md#virtual_app_destroy_children) | **POST** /VirtualApp/{moId}/DestroyChildren | Removes all child resource pools recursively. 
[**virtual_app_destroy_task**](VirtualAppApi.md#virtual_app_destroy_task) | **POST** /VirtualApp/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**virtual_app_export_v_app**](VirtualAppApi.md#virtual_app_export_v_app) | **POST** /VirtualApp/{moId}/ExportVApp | Obtains an export lease on this vApp. 
[**virtual_app_get_alarm_actions_enabled**](VirtualAppApi.md#virtual_app_get_alarm_actions_enabled) | **GET** /VirtualApp/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**virtual_app_get_available_field**](VirtualAppApi.md#virtual_app_get_available_field) | **GET** /VirtualApp/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**virtual_app_get_child_configuration**](VirtualAppApi.md#virtual_app_get_child_configuration) | **GET** /VirtualApp/{moId}/childConfiguration | The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group. 
[**virtual_app_get_child_link**](VirtualAppApi.md#virtual_app_get_child_link) | **GET** /VirtualApp/{moId}/childLink | List of linked children. 
[**virtual_app_get_config**](VirtualAppApi.md#virtual_app_get_config) | **GET** /VirtualApp/{moId}/config | Configuration of this resource pool. 
[**virtual_app_get_config_issue**](VirtualAppApi.md#virtual_app_get_config_issue) | **GET** /VirtualApp/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**virtual_app_get_config_status**](VirtualAppApi.md#virtual_app_get_config_status) | **GET** /VirtualApp/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**virtual_app_get_custom_value**](VirtualAppApi.md#virtual_app_get_custom_value) | **GET** /VirtualApp/{moId}/customValue | Custom field values. 
[**virtual_app_get_datastore**](VirtualAppApi.md#virtual_app_get_datastore) | **GET** /VirtualApp/{moId}/datastore | A collection of references to the subset of datastore objects used by this vApp. 
[**virtual_app_get_declared_alarm_state**](VirtualAppApi.md#virtual_app_get_declared_alarm_state) | **GET** /VirtualApp/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**virtual_app_get_disabled_method**](VirtualAppApi.md#virtual_app_get_disabled_method) | **GET** /VirtualApp/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**virtual_app_get_effective_role**](VirtualAppApi.md#virtual_app_get_effective_role) | **GET** /VirtualApp/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**virtual_app_get_name**](VirtualAppApi.md#virtual_app_get_name) | **GET** /VirtualApp/{moId}/name | Name of this entity, unique relative to its parent. 
[**virtual_app_get_namespace**](VirtualAppApi.md#virtual_app_get_namespace) | **GET** /VirtualApp/{moId}/namespace | The namespace with which the ResourcePool is associated. 
[**virtual_app_get_network**](VirtualAppApi.md#virtual_app_get_network) | **GET** /VirtualApp/{moId}/network | A collection of references to the subset of network objects that is used by this virtual machine. 
[**virtual_app_get_overall_status**](VirtualAppApi.md#virtual_app_get_overall_status) | **GET** /VirtualApp/{moId}/overallStatus | General health of this managed entity. 
[**virtual_app_get_owner**](VirtualAppApi.md#virtual_app_get_owner) | **GET** /VirtualApp/{moId}/owner | The ComputeResource to which this set of one or more nested resource pools belong. 
[**virtual_app_get_parent**](VirtualAppApi.md#virtual_app_get_parent) | **GET** /VirtualApp/{moId}/parent | Parent of this entity. 
[**virtual_app_get_parent_folder**](VirtualAppApi.md#virtual_app_get_parent_folder) | **GET** /VirtualApp/{moId}/parentFolder | A reference to the parent folder in the VM and Template folder hierarchy. 
[**virtual_app_get_parent_v_app**](VirtualAppApi.md#virtual_app_get_parent_v_app) | **GET** /VirtualApp/{moId}/parentVApp | Reference to the parent vApp. 
[**virtual_app_get_permission**](VirtualAppApi.md#virtual_app_get_permission) | **GET** /VirtualApp/{moId}/permission | List of permissions defined for this entity. 
[**virtual_app_get_recent_task**](VirtualAppApi.md#virtual_app_get_recent_task) | **GET** /VirtualApp/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**virtual_app_get_resource_pool**](VirtualAppApi.md#virtual_app_get_resource_pool) | **GET** /VirtualApp/{moId}/resourcePool | The set of child resource pools. 
[**virtual_app_get_runtime**](VirtualAppApi.md#virtual_app_get_runtime) | **GET** /VirtualApp/{moId}/runtime | Runtime information about a resource pool. 
[**virtual_app_get_summary**](VirtualAppApi.md#virtual_app_get_summary) | **GET** /VirtualApp/{moId}/summary | Basic information about a resource pool. 
[**virtual_app_get_tag**](VirtualAppApi.md#virtual_app_get_tag) | **GET** /VirtualApp/{moId}/tag | The set of tags associated with this managed entity. 
[**virtual_app_get_triggered_alarm_state**](VirtualAppApi.md#virtual_app_get_triggered_alarm_state) | **GET** /VirtualApp/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**virtual_app_get_v_app_config**](VirtualAppApi.md#virtual_app_get_v_app_config) | **GET** /VirtualApp/{moId}/vAppConfig | Configuration of this package. 
[**virtual_app_get_value**](VirtualAppApi.md#virtual_app_get_value) | **GET** /VirtualApp/{moId}/value | List of custom field values. 
[**virtual_app_get_vm**](VirtualAppApi.md#virtual_app_get_vm) | **GET** /VirtualApp/{moId}/vm | The set of virtual machines associated with this resource pool. 
[**virtual_app_import_v_app**](VirtualAppApi.md#virtual_app_import_v_app) | **POST** /VirtualApp/{moId}/ImportVApp | Creates a new entity in this resource pool. 
[**virtual_app_move_into_resource_pool**](VirtualAppApi.md#virtual_app_move_into_resource_pool) | **POST** /VirtualApp/{moId}/MoveIntoResourcePool | Moves a set of resource pools, vApps or virtual machines into this pool. 
[**virtual_app_power_off_v_app_task**](VirtualAppApi.md#virtual_app_power_off_v_app_task) | **POST** /VirtualApp/{moId}/PowerOffVApp_Task | Stops this vApp. 
[**virtual_app_power_on_v_app_task**](VirtualAppApi.md#virtual_app_power_on_v_app_task) | **POST** /VirtualApp/{moId}/PowerOnVApp_Task | Starts this vApp. 
[**virtual_app_query_resource_config_option**](VirtualAppApi.md#virtual_app_query_resource_config_option) | **POST** /VirtualApp/{moId}/QueryResourceConfigOption | Get a value range and default values for *ResourceConfigSpec*. 
[**virtual_app_refresh_runtime**](VirtualAppApi.md#virtual_app_refresh_runtime) | **POST** /VirtualApp/{moId}/RefreshRuntime | Refreshes the resource usage data that is available in *ResourcePoolRuntimeInfo*. 
[**virtual_app_register_child_vm_task**](VirtualAppApi.md#virtual_app_register_child_vm_task) | **POST** /VirtualApp/{moId}/RegisterChildVM_Task | Adds an existing virtual machine to this resource pool or vApp. 
[**virtual_app_reload**](VirtualAppApi.md#virtual_app_reload) | **POST** /VirtualApp/{moId}/Reload | Reload the entity state. 
[**virtual_app_rename_task**](VirtualAppApi.md#virtual_app_rename_task) | **POST** /VirtualApp/{moId}/Rename_Task | Renames this managed entity. 
[**virtual_app_set_custom_value**](VirtualAppApi.md#virtual_app_set_custom_value) | **POST** /VirtualApp/{moId}/setCustomValue | Assigns a value to a custom field. 
[**virtual_app_suspend_v_app_task**](VirtualAppApi.md#virtual_app_suspend_v_app_task) | **POST** /VirtualApp/{moId}/SuspendVApp_Task | Suspends this vApp. 
[**virtual_app_unregister_v_app_task**](VirtualAppApi.md#virtual_app_unregister_v_app_task) | **POST** /VirtualApp/{moId}/unregisterVApp_Task | Removes this vApp from the inventory without removing any of the virtual machine&#39;s files on disk. 
[**virtual_app_update_child_resource_configuration**](VirtualAppApi.md#virtual_app_update_child_resource_configuration) | **POST** /VirtualApp/{moId}/UpdateChildResourceConfiguration | Changes resource configuration of a set of children of this resource pool. 
[**virtual_app_update_config**](VirtualAppApi.md#virtual_app_update_config) | **POST** /VirtualApp/{moId}/UpdateConfig | Updates the configuration of the resource pool. 
[**virtual_app_update_linked_children**](VirtualAppApi.md#virtual_app_update_linked_children) | **POST** /VirtualApp/{moId}/UpdateLinkedChildren | Reconfigure the set of linked children. 
[**virtual_app_update_v_app_config**](VirtualAppApi.md#virtual_app_update_v_app_config) | **POST** /VirtualApp/{moId}/UpdateVAppConfig | Updates the vApp configuration. 


# **virtual_app_clone_v_app_task**
> ManagedObjectReference virtual_app_clone_v_app_task(mo_id, clone_v_app_request_type)

Creates a clone of this vApp. 

Creates a clone of this vApp.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  When invoking this method, the following privilege checks occur: - The privilege VApp.Clone is required on this vApp. - If the target is a resource pool, the privilege   Resource.AssignVAppToPool is required on it. - If the target is a vApp, the privileges VApp.Clone and   VApp.AssignVApp are required on it.    Additional privileges are required by the clone spec provided. See *VAppCloneSpec* for details.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Clone 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clone_v_app_request_type import CloneVAppRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clone_v_app_request_type = vmware_vi.CloneVAppRequestType() # CloneVAppRequestType | 

    try:
        # Creates a clone of this vApp. 
        api_response = api_instance.virtual_app_clone_v_app_task(mo_id, clone_v_app_request_type)
        print("The response of VirtualAppApi->virtual_app_clone_v_app_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_clone_v_app_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clone_v_app_request_type** | [**CloneVAppRequestType**](CloneVAppRequestType.md)|  | 

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
**500** | ***InvalidPowerState***: if the vApp is powered on.  ***TaskInProgress***: if the vApp is busy.  ***NotSupported***: if the operation is not supported by the current agent.  ***InvalidState***: if the operation cannot be performed because of the vApp&#39;s current state. For example, if the virtual machine configuration information is not available, or if the vApp is running.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***FileFault***: if there was an error accessing one of the virtual machine files.  ***VmConfigFault***: if one of the virtual machines are not compatible with a destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.  ***MigrationFault***: if it is not possible to migrate one of the virtual machines to the destination. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_create_child_vm_task**
> ManagedObjectReference virtual_app_create_child_vm_task(mo_id, create_child_vm_request_type)

Creates a new virtual machine in a vApp container. 

Creates a new virtual machine in a vApp container.  This method supports creating a virtual machine directly in a vApp. A virtual machine in a vApp is not associated with a VM folder and therefore cannot be created using the method on a *Folder*.  This method can only be called directly on a *vApp* or on a resource pool that is a child of a vApp.  The privilege VirtualMachine.Inventory.Create is required on this entity. Further, if this is a resource pool, the privilege Resource.AssignVMToPool is required. If this is a vApp, the privilege VApp.AssignVM is required.  Depending on the properties of the virtual machine bring created, additional privileges may be required. See *Folder.CreateVM_Task* for a description of these privileges.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Inventory.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_child_vm_request_type import CreateChildVMRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_child_vm_request_type = vmware_vi.CreateChildVMRequestType() # CreateChildVMRequestType | 

    try:
        # Creates a new virtual machine in a vApp container. 
        api_response = api_instance.virtual_app_create_child_vm_task(mo_id, create_child_vm_request_type)
        print("The response of VirtualAppApi->virtual_app_create_child_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_create_child_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_child_vm_request_type** | [**CreateChildVMRequestType**](CreateChildVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly created *VirtualMachine* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***VmConfigFault***: if the configSpec has incorrect values. Typically, a more specific subclass is thrown.  ***OutOfBounds***: if Host.capability.maxSupportedVMs is exceeded.  ***FileAlreadyExists***: if the requested cfgPath for the virtual machine&#39;s configuration file already exists.  ***FileFault***: if there is a problem creating the virtual machine on disk. Typically, a more specific subclass, such as NoDiskSpace, will be thrown.  ***InvalidName***: if the name is not a valid entity name.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***VmWwnConflict***: if the WWN of the virtual machine has been used by other virtual machines.  ***NotSupported***: if this resource pool is not a vApp or is a child of a vApp.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_create_resource_pool**
> ManagedObjectReference virtual_app_create_resource_pool(mo_id, create_resource_pool_request_type)

Creates a new resource pool. 

Creates a new resource pool.  ***Required privileges:*** Resource.CreatePool 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_resource_pool_request_type import CreateResourcePoolRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_resource_pool_request_type = vmware_vi.CreateResourcePoolRequestType() # CreateResourcePoolRequestType | 

    try:
        # Creates a new resource pool. 
        api_response = api_instance.virtual_app_create_resource_pool(mo_id, create_resource_pool_request_type)
        print("The response of VirtualAppApi->virtual_app_create_resource_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_create_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_resource_pool_request_type** | [**CreateResourcePoolRequestType**](CreateResourcePoolRequestType.md)|  | 

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
**200** | A reference to the new resource pool.  Refers instance of *ResourcePool*.  |  -  |
**500** | ***NotSupported***: if the ComputeResource does not support nested resource pools.  ***InvalidName***: if the name is not a valid entity name.  ***DuplicateName***: if this pool already contains an object with the given name.  ***InvalidArgument***: if the pool specification is invalid.  ***InsufficientResourcesFault***: if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientCpuResourcesFault will be thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_create_v_app**
> ManagedObjectReference virtual_app_create_v_app(mo_id, create_v_app_request_type)

Creates a new vApp container. 

Creates a new vApp container.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_v_app_request_type import CreateVAppRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_v_app_request_type = vmware_vi.CreateVAppRequestType() # CreateVAppRequestType | 

    try:
        # Creates a new vApp container. 
        api_response = api_instance.virtual_app_create_v_app(mo_id, create_v_app_request_type)
        print("The response of VirtualAppApi->virtual_app_create_v_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_create_v_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_v_app_request_type** | [**CreateVAppRequestType**](CreateVAppRequestType.md)|  | 

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
**200** | The created vApp object.  Refers instance of *VirtualApp*.  |  -  |
**500** | ***NotSupported***: if the ComputeResource does not support nested resource pools.  ***InvalidName***: if the name is not a valid entity name.  ***DuplicateName***: if this pool already contains an object with the given name.  ***InvalidArgument***: if the pool specification is invalid.  ***InsufficientResourcesFault***: if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientCpuResourcesFault will be thrown.  ***InvalidState***: if the resource pool does not support the operation in its current state. This will typically be a subclass such as *NoActiveHostInCluster*.  ***VmConfigFault***: or a more specific subclass, if errors are found in the supplied in VApp configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_destroy_children**
> virtual_app_destroy_children(mo_id)

Removes all child resource pools recursively. 

Removes all child resource pools recursively.  All virtual machines and vApps associated with the child resource pools get associated with this resource pool.  Note that resource pools contained in child vApps are not affected.  The privilege checks performed are the following. - Resource.DeletePool privilege must be held on this object and each of it's   immediate children to be destroyed. - If VMs are being moved, the privilege Resource.AssignVMToPool must be held   on this resource pool as well as on any virtual machines being moved. - If vApps are being moved, the privilege Resource.AssignVAppToPool   must be held on this resource pool as well as on any vApps being   moved. 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes all child resource pools recursively. 
        api_instance.virtual_app_destroy_children(mo_id)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_destroy_children: %s\n" % e)
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

# **virtual_app_destroy_task**
> ManagedObjectReference virtual_app_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** VApp.Delete 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.virtual_app_destroy_task(mo_id)
        print("The response of VirtualAppApi->virtual_app_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_destroy_task: %s\n" % e)
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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_export_v_app**
> ManagedObjectReference virtual_app_export_v_app(mo_id)

Obtains an export lease on this vApp. 

Obtains an export lease on this vApp.  The export lease contains a list of URLs for the disks of the virtual machines in this vApp, as well as a ticket that gives access to these URLs.  See *HttpNfcLease* for information on how to use the lease.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Export 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Obtains an export lease on this vApp. 
        api_response = api_instance.virtual_app_export_v_app(mo_id)
        print("The response of VirtualAppApi->virtual_app_export_v_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_export_v_app: %s\n" % e)
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
**200** | the export lease on this vApp. The export task continues running until the lease is completed or aborted.  Refers instance of *HttpNfcLease*.  |  -  |
**500** | ***InvalidPowerState***: if the vApp is powered on.  ***TaskInProgress***: if the vApp is busy.  ***InvalidState***: if the operation cannot be performed because of the vApp&#39;s current state. For example, if the virtual machine configuration information is not available, or if the vApp is running or already powering on.  ***FileFault***: if there was an error accessing one of the virtual machine files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_alarm_actions_enabled**
> bool virtual_app_get_alarm_actions_enabled(mo_id)

Whether alarm actions are enabled for this entity. 

Whether alarm actions are enabled for this entity.  True if enabled; false otherwise.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.virtual_app_get_alarm_actions_enabled(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_alarm_actions_enabled: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**bool**

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

# **virtual_app_get_available_field**
> List[CustomFieldDef] virtual_app_get_available_field(mo_id)

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.virtual_app_get_available_field(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_available_field: %s\n" % e)
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

# **virtual_app_get_child_configuration**
> List[ResourceConfigSpec] virtual_app_get_child_configuration(mo_id)

The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group. 

The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group.  Property collector update notifications might not be generated for this property. To listen for the child configuration change, please create PropertyCollector filter on the child entities directly. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_config_spec import ResourceConfigSpec
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group. 
        api_response = api_instance.virtual_app_get_child_configuration(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_child_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_child_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ResourceConfigSpec]**](ResourceConfigSpec.md)

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

# **virtual_app_get_child_link**
> List[VirtualAppLinkInfo] virtual_app_get_child_link(mo_id)

List of linked children. 

Deprecated as of vSphere API 5.1.  List of linked children.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_app_link_info import VirtualAppLinkInfo
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of linked children. 
        api_response = api_instance.virtual_app_get_child_link(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_child_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_child_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VirtualAppLinkInfo]**](VirtualAppLinkInfo.md)

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

# **virtual_app_get_config**
> ResourceConfigSpec virtual_app_get_config(mo_id)

Configuration of this resource pool. 

Configuration of this resource pool. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_config_spec import ResourceConfigSpec
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of this resource pool. 
        api_response = api_instance.virtual_app_get_config(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ResourceConfigSpec**](ResourceConfigSpec.md)

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

# **virtual_app_get_config_issue**
> List[Event] virtual_app_get_config_issue(mo_id)

Current configuration issues that have been detected for this entity. 

Current configuration issues that have been detected for this entity.  Typically, these issues have already been logged as events. The entity stores these events as long as they are still current. The *configStatus* property provides an overall status based on these events. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.virtual_app_get_config_issue(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_config_issue: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Event]**](Event.md)

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

# **virtual_app_get_config_status**
> ManagedEntityStatusEnum virtual_app_get_config_status(mo_id)

The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 

The configStatus indicates whether or not the system has detected a configuration issue involving this entity.  For example, it might have detected a duplicate IP address or MAC address, or a host in a cluster might be out of compliance. The meanings of the configStatus values are: - red: A problem has been detected involving the entity. - yellow: A problem is about to occur or a transient condition   has occurred (For example, reconfigure fail-over policy). - green: No configuration issues have been detected. - gray: The configuration status of the entity is not being monitored.    A green status indicates only that a problem has not been detected; it is not a guarantee that the entity is problem-free.  The *configIssue* property contains a list of the problems that have been detected. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.virtual_app_get_config_status(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_config_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md)

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

# **virtual_app_get_custom_value**
> List[CustomFieldValue] virtual_app_get_custom_value(mo_id)

Custom field values. 

Custom field values.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.virtual_app_get_custom_value(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_custom_value: %s\n" % e)
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

# **virtual_app_get_datastore**
> List[ManagedObjectReference] virtual_app_get_datastore(mo_id)

A collection of references to the subset of datastore objects used by this vApp. 

A collection of references to the subset of datastore objects used by this vApp.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A collection of references to the subset of datastore objects used by this vApp. 
        api_response = api_instance.virtual_app_get_datastore(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_datastore: %s\n" % e)
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

# **virtual_app_get_declared_alarm_state**
> List[AlarmState] virtual_app_get_declared_alarm_state(mo_id)

A set of alarm states for alarms that apply to this managed entity. 

A set of alarm states for alarms that apply to this managed entity.  The set includes alarms defined on this entity and alarms inherited from the parent entity, or from any ancestors in the inventory hierarchy.  Alarms are inherited if they can be triggered by this entity or its descendants. This set does not include alarms that are defined on descendants of this entity.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_state import AlarmState
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.virtual_app_get_declared_alarm_state(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_declared_alarm_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AlarmState]**](AlarmState.md)

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

# **virtual_app_get_disabled_method**
> List[str] virtual_app_get_disabled_method(mo_id)

List of operations that are disabled, given the current runtime state of the entity. 

List of operations that are disabled, given the current runtime state of the entity.  For example, a power-on operation always fails if a virtual machine is already powered on. This list can be used by clients to enable or disable operations in a graphical user interface.  Note: This list is determined by the current runtime state of an entity, not by its permissions.  This list may include the following operations for a HostSystem: - *HostSystem.EnterMaintenanceMode_Task* - *HostSystem.ExitMaintenanceMode_Task* - *HostSystem.RebootHost_Task* - *HostSystem.ShutdownHost_Task* - *HostSystem.ReconnectHost_Task* - *HostSystem.DisconnectHost_Task*    This list may include the following operations for a VirtualMachine: - *VirtualMachine.AnswerVM* - *ManagedEntity.Rename_Task* - *VirtualMachine.CloneVM_Task* - *VirtualMachine.PowerOffVM_Task* - *VirtualMachine.PowerOnVM_Task* - *VirtualMachine.SuspendVM_Task* - *VirtualMachine.ResetVM_Task* - *VirtualMachine.ReconfigVM_Task* - *VirtualMachine.RelocateVM_Task* - *VirtualMachine.MigrateVM_Task* - *VirtualMachine.CustomizeVM_Task* - *VirtualMachine.ShutdownGuest* - *VirtualMachine.StandbyGuest* - *VirtualMachine.RebootGuest* - *VirtualMachine.CreateSnapshot_Task* - *VirtualMachine.RemoveAllSnapshots_Task* - *VirtualMachine.RevertToCurrentSnapshot_Task* - *VirtualMachine.MarkAsTemplate* - *VirtualMachine.MarkAsVirtualMachine* - *VirtualMachine.ResetGuestInformation* - *VirtualMachine.MountToolsInstaller* - *VirtualMachine.UnmountToolsInstaller* - *ManagedEntity.Destroy_Task* - *VirtualMachine.UpgradeVM_Task* - *VirtualMachine.ExportVm*    This list may include the following operations for a ResourcePool: - *ResourcePool.ImportVApp* - *ResourcePool.CreateChildVM_Task* - *ResourcePool.UpdateConfig* - *Folder.CreateVM_Task* - *ManagedEntity.Destroy_Task* - *ManagedEntity.Rename_Task*    This list may include the following operations for a VirtualApp: - *ManagedEntity.Destroy_Task* - *VirtualApp.CloneVApp_Task* - *VirtualApp.unregisterVApp_Task* - *VirtualApp.ExportVApp* - *VirtualApp.PowerOnVApp_Task* - *VirtualApp.PowerOffVApp_Task* - *VirtualApp.UpdateVAppConfig*    In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.virtual_app_get_disabled_method(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_disabled_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

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

# **virtual_app_get_effective_role**
> List[int] virtual_app_get_effective_role(mo_id)

Access rights the current session has to this entity. 

Access rights the current session has to this entity.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.virtual_app_get_effective_role(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_effective_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[int]**

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

# **virtual_app_get_name**
> str virtual_app_get_name(mo_id)

Name of this entity, unique relative to its parent. 

Name of this entity, unique relative to its parent.  Any / (slash), \\\\ (backslash), character used in this name element will be escaped. Similarly, any % (percent) character used in this name element will be escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.virtual_app_get_name(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **virtual_app_get_namespace**
> str virtual_app_get_namespace(mo_id)

The namespace with which the ResourcePool is associated. 

The namespace with which the ResourcePool is associated.  Namespace is a vAPI resource which divides cluster resources and allows administrators to give Kubernetes environments to their development teams. This property is set only at the time of creation and cannot change.  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The namespace with which the ResourcePool is associated. 
        api_response = api_instance.virtual_app_get_namespace(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_namespace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **virtual_app_get_network**
> List[ManagedObjectReference] virtual_app_get_network(mo_id)

A collection of references to the subset of network objects that is used by this virtual machine. 

A collection of references to the subset of network objects that is used by this virtual machine.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A collection of references to the subset of network objects that is used by this virtual machine. 
        api_response = api_instance.virtual_app_get_network(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_network: %s\n" % e)
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
**200** | Refers instances of *Network*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_overall_status**
> ManagedEntityStatusEnum virtual_app_get_overall_status(mo_id)

General health of this managed entity. 

General health of this managed entity.  The overall status of the managed entity is computed as the worst status among its alarms and the configuration issues detected on the entity. The status is reported as one of the following values: - red: The entity has alarms or configuration issues with a red status. - yellow: The entity does not have alarms or configuration issues with a   red status, and has at least one with a yellow status. - green: The entity does not have alarms or configuration issues with a   red or yellow status, and has at least one with a green status. - gray: All of the entity's alarms have a gray status and the   configuration status of the entity is not being monitored.    In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.virtual_app_get_overall_status(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_overall_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md)

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

# **virtual_app_get_owner**
> ManagedObjectReference virtual_app_get_owner(mo_id)

The ComputeResource to which this set of one or more nested resource pools belong. 

The ComputeResource to which this set of one or more nested resource pools belong.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The ComputeResource to which this set of one or more nested resource pools belong. 
        api_response = api_instance.virtual_app_get_owner(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_owner: %s\n" % e)
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
**200** | Refers instance of *ComputeResource*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_parent**
> ManagedObjectReference virtual_app_get_parent(mo_id)

Parent of this entity. 

Parent of this entity.  This value is null for the root object and for *VirtualMachine* objects that are part of a *VirtualApp*.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.virtual_app_get_parent(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_parent: %s\n" % e)
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
**200** | Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_parent_folder**
> ManagedObjectReference virtual_app_get_parent_folder(mo_id)

A reference to the parent folder in the VM and Template folder hierarchy. 

A reference to the parent folder in the VM and Template folder hierarchy.  This is only set for a root vApp. A root vApp is a vApp that is not a child of another vApp.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A reference to the parent folder in the VM and Template folder hierarchy. 
        api_response = api_instance.virtual_app_get_parent_folder(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_parent_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_parent_folder: %s\n" % e)
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
**200** | Refers instance of *Folder*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_parent_v_app**
> ManagedObjectReference virtual_app_get_parent_v_app(mo_id)

Reference to the parent vApp. 

Reference to the parent vApp.  ***Since:*** vSphere API 4.1 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reference to the parent vApp. 
        api_response = api_instance.virtual_app_get_parent_v_app(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_parent_v_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_parent_v_app: %s\n" % e)
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
**200** | Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_permission**
> List[Permission] virtual_app_get_permission(mo_id)

List of permissions defined for this entity. 

List of permissions defined for this entity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.permission import Permission
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.virtual_app_get_permission(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Permission]**](Permission.md)

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

# **virtual_app_get_recent_task**
> List[ManagedObjectReference] virtual_app_get_recent_task(mo_id)

The set of recent tasks operating on this managed entity. 

The set of recent tasks operating on this managed entity.  This is a subset of *TaskManager.recentTask* belong to this entity. A task in this list could be in one of the four states: pending, running, success or error.  This property can be used to deduce intermediate power states for a virtual machine entity. For example, if the current powerState is \"poweredOn\" and there is a running task performing the \"suspend\" operation, then the virtual machine's intermediate state might be described as \"suspending.\"  Most tasks (such as power operations) obtain exclusive access to the virtual machine, so it is unusual for this list to contain more than one running task. One exception, however, is the task of cloning a virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.virtual_app_get_recent_task(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_recent_task: %s\n" % e)
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
**200** | Refers instances of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_resource_pool**
> List[ManagedObjectReference] virtual_app_get_resource_pool(mo_id)

The set of child resource pools. 

The set of child resource pools.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of child resource pools. 
        api_response = api_instance.virtual_app_get_resource_pool(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_resource_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_resource_pool: %s\n" % e)
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
**200** | Refers instances of *ResourcePool*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_get_runtime**
> ResourcePoolRuntimeInfo virtual_app_get_runtime(mo_id)

Runtime information about a resource pool. 

Runtime information about a resource pool.  The *ResourcePoolResourceUsage* information within *ResourcePoolRuntimeInfo* can be transiently stale. Use *ResourcePool.RefreshRuntime* method to update the information. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_pool_runtime_info import ResourcePoolRuntimeInfo
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Runtime information about a resource pool. 
        api_response = api_instance.virtual_app_get_runtime(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_runtime: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ResourcePoolRuntimeInfo**](ResourcePoolRuntimeInfo.md)

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

# **virtual_app_get_summary**
> ResourcePoolSummary virtual_app_get_summary(mo_id)

Basic information about a resource pool. 

Basic information about a resource pool.  In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_pool_summary import ResourcePoolSummary
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Basic information about a resource pool. 
        api_response = api_instance.virtual_app_get_summary(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ResourcePoolSummary**](ResourcePoolSummary.md)

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

# **virtual_app_get_tag**
> List[Tag] virtual_app_get_tag(mo_id)

The set of tags associated with this managed entity. 

The set of tags associated with this managed entity.  Experimental. Subject to change.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.tag import Tag
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.virtual_app_get_tag(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Tag]**](Tag.md)

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

# **virtual_app_get_triggered_alarm_state**
> List[AlarmState] virtual_app_get_triggered_alarm_state(mo_id)

A set of alarm states for alarms triggered by this entity or by its descendants. 

A set of alarm states for alarms triggered by this entity or by its descendants.  Triggered alarms are propagated up the inventory hierarchy so that a user can readily tell when a descendant has triggered an alarm. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_state import AlarmState
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.virtual_app_get_triggered_alarm_state(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_triggered_alarm_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AlarmState]**](AlarmState.md)

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

# **virtual_app_get_v_app_config**
> VAppConfigInfo virtual_app_get_v_app_config(mo_id)

Configuration of this package. 

Configuration of this package.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.v_app_config_info import VAppConfigInfo
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of this package. 
        api_response = api_instance.virtual_app_get_v_app_config(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_v_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_v_app_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VAppConfigInfo**](VAppConfigInfo.md)

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

# **virtual_app_get_value**
> List[CustomFieldValue] virtual_app_get_value(mo_id)

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.virtual_app_get_value(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_value: %s\n" % e)
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

# **virtual_app_get_vm**
> List[ManagedObjectReference] virtual_app_get_vm(mo_id)

The set of virtual machines associated with this resource pool. 

The set of virtual machines associated with this resource pool.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of virtual machines associated with this resource pool. 
        api_response = api_instance.virtual_app_get_vm(mo_id)
        print("The response of VirtualAppApi->virtual_app_get_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_get_vm: %s\n" % e)
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
**200** | Refers instances of *VirtualMachine*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_import_v_app**
> ManagedObjectReference virtual_app_import_v_app(mo_id, import_v_app_request_type)

Creates a new entity in this resource pool. 

Creates a new entity in this resource pool.  The import process consists of two steps: 1. Create the VMs and/or vApps that make up the entity. 2. Upload virtual disk contents.     In step 1, the client must wait for the server to create all inventory objects. It does that by monitoring the *HttpNfcLease.state* property on the *HttpNfcLease* object returned from this call. When the server is done creating objects, the lease will change to the ready state, and step 2 begins. If an error occurs while the server is creating inventory objects, the lease will change to the error state, and the import process is aborted.  In step 2, the client uploads disk contents using the URLs provided in the *HttpNfcLease.info* property of the lease. The client must call *HttpNfcLease.HttpNfcLeaseProgress* on the lease periodically to keep the lease alive and report progress to the server. Failure to do so will cause the lease to time out, and the import process will be aborted.  When the client is done uploading disks, it completes the lease by calling *HttpNfcLease.HttpNfcLeaseComplete*. The client can also abort the import process by calling *HttpNfcLease.HttpNfcLeaseAbort*.  If the import process fails, is aborted, or times out, all created inventory objects are removed, including all virtual disks.  This operation only works if the folder's childType includes VirtualMachine.  Depending on the properties of the virtual machine bring imported, additional privileges may be required. See *Folder.CreateVM_Task* for a description of these privileges.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Import 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.import_v_app_request_type import ImportVAppRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    import_v_app_request_type = vmware_vi.ImportVAppRequestType() # ImportVAppRequestType | 

    try:
        # Creates a new entity in this resource pool. 
        api_response = api_instance.virtual_app_import_v_app(mo_id, import_v_app_request_type)
        print("The response of VirtualAppApi->virtual_app_import_v_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_import_v_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **import_v_app_request_type** | [**ImportVAppRequestType**](ImportVAppRequestType.md)|  | 

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
**200** | a *HttpNfcLease* object which is used to drive the import session.  Refers instance of *HttpNfcLease*.  |  -  |
**500** | ***VmConfigFault***: if a VM configSpec has incorrect values. Typically, a more specific subclass is thrown.  ***OutOfBounds***: if Host.capability.maxSupportedVMs is exceeded.  ***FileAlreadyExists***: if the requested cfgPath for the virtual machine&#39;s configuration file already exists.  ***FileFault***: if there is a problem creating the virtual machine on disk. Typically, a more specific subclass, such as NoDiskSpace, will be thrown.  ***DuplicateName***: if another virtual machine in the same folder already has the specified target name.  ***InvalidName***: if the name is not a valid entity name.  ***NotSupported***: if the virtual machine is being created within a folder whose *Folder.childType* property is not set to \&quot;VirtualMachine\&quot;, a vApp is being imported into a resource pool that does not support nested resource pools, or a virtual machine is being imported into a resource pool and no folder is given.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***VmWwnConflict***: if the WWN of the virtual machine has been used by other virtual machines.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_move_into_resource_pool**
> virtual_app_move_into_resource_pool(mo_id, move_into_resource_pool_request_type)

Moves a set of resource pools, vApps or virtual machines into this pool. 

Moves a set of resource pools, vApps or virtual machines into this pool.  The pools, vApps and virtual machines must be part of the cluster or standalone host that contains this pool.  For each entity being moved, the move is subject to the following privilege checks: - If the object being moved is a ResourcePool, then Resource.MovePool must be   held on the pool being moved and it's former parent pool or vApp. If the   target is a vApp, the privilege VApp.AssignResourcePool must be held on   it. If the target is a ResourcePool, Resource.MovePool must be held on it. - If the object being moved is a VirtualApp, VApp.Move must be held on   the vApp being moved and it's former parent pool or vApp. If the target   entity is a resource pool, Resource.AssignVAppToPool must be held on the   target. If the target is a vApp, the privilege VApp.AssignVApp must   be held on the target vApp. - If the object being moved is a VirtualMachine, then if the target is a   ResourcePool, Resource.AssignVMToPool is required on the VirtualMachine and the   target pool. If the target is a vApp, VApp.AssignVM is required on both   the VirtualMachine and the target pool.    This operation is typically used by clients when they implement a drag-and-drop interface to move a set of objects into a folder.  This operation is only transactional with respect to each individual entity. The set of entities is moved sequentially, as specified in the list, and committed one at a time. If a failure is detected, then the method terminates with an exception.  The root resource pool cannot be moved. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.move_into_resource_pool_request_type import MoveIntoResourcePoolRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_into_resource_pool_request_type = vmware_vi.MoveIntoResourcePoolRequestType() # MoveIntoResourcePoolRequestType | 

    try:
        # Moves a set of resource pools, vApps or virtual machines into this pool. 
        api_instance.virtual_app_move_into_resource_pool(mo_id, move_into_resource_pool_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_move_into_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_into_resource_pool_request_type** | [**MoveIntoResourcePoolRequestType**](MoveIntoResourcePoolRequestType.md)|  | 

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
**500** | ***DuplicateName***: if this pool already contains an object with the given name.  ***InvalidArgument***: if an ancestor of this pool is in the list.  ***InsufficientResourcesFault***: if the move would violate the resource usage policy. Typically, a more specific subclass, such as InsufficientMemoryResourcesFault.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_power_off_v_app_task**
> ManagedObjectReference virtual_app_power_off_v_app_task(mo_id, power_off_v_app_request_type)

Stops this vApp. 

Stops this vApp.  The virtual machines (or child vApps) will be stopped in the order specified in the vApp configuration, if force is false. If force is set to true, all virtual machines are powered-off (in no specific order and possibly in parallel) regardless of the vApp auto-start configuration.  While a vApp is stopping, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.PowerOff 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.power_off_v_app_request_type import PowerOffVAppRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    power_off_v_app_request_type = vmware_vi.PowerOffVAppRequestType() # PowerOffVAppRequestType | 

    try:
        # Stops this vApp. 
        api_response = api_instance.virtual_app_power_off_v_app_task(mo_id, power_off_v_app_request_type)
        print("The response of VirtualAppApi->virtual_app_power_off_v_app_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_power_off_v_app_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **power_off_v_app_request_type** | [**PowerOffVAppRequestType**](PowerOffVAppRequestType.md)|  | 

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
**500** | ***InvalidPowerState***: if the vApp is not running  ***TaskInProgress***: if the vApp is busy.  ***InvalidState***: if the operation cannot be performed because of the vApp&#39;s current state. For example, if the vApp is in the process of being started.  ***MissingPowerOffConfiguration***: if no vApp powerOff configuration has been specified.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_power_on_v_app_task**
> ManagedObjectReference virtual_app_power_on_v_app_task(mo_id)

Starts this vApp. 

Starts this vApp.  The virtual machines (or sub vApps) will be started in the order specified in the vApp configuration. If the vApp is suspended (@see vim.VirtualApp.Summary#suspended), all suspended virtual machines will be powered-on based on the defined start-up order.  While a vApp is starting, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.  In case of a failure to power-on a virtual machine, the exception from the virtual machine power on is returned, and the power-on sequence will be terminated. In case of a failure, virtual machines that are already started will remain powered-on.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.PowerOn 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Starts this vApp. 
        api_response = api_instance.virtual_app_power_on_v_app_task(mo_id)
        print("The response of VirtualAppApi->virtual_app_power_on_v_app_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_power_on_v_app_task: %s\n" % e)
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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the vApp is already running  ***TaskInProgress***: if the vApp is busy  ***NotEnoughLicenses***: if there are not enough licenses to power on one or more virtual machines.  ***NotSupported***: if the vApp is marked as a template.  ***InvalidState***: if it fails to power on a virtual machine due to no host availability, or unable to access the configuration file of a VM.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***VmConfigFault***: if a configuration issue on the vApp or a virtual machine in the vApp prevents the power-on to complete. Typically, a more specific fault, such as InvalidPropertyType is thrown.  ***VAppConfigFault***: if a configuration issue on a vApp prevents the power-on. Typically, a more specific fault, MissingPowerOnConfiguration, is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  ***MissingNetworkIpConfig***: if no network configuration exists for the primary network for the vApp.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_query_resource_config_option**
> ResourceConfigOption virtual_app_query_resource_config_option(mo_id)

Get a value range and default values for *ResourceConfigSpec*. 

Deprecated as of vSphere API 6.5.  Get a value range and default values for *ResourceConfigSpec*.  This API was never implemented, and there is no replacement for it.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Resource.EditPool 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_config_option import ResourceConfigOption
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get a value range and default values for *ResourceConfigSpec*. 
        api_response = api_instance.virtual_app_query_resource_config_option(mo_id)
        print("The response of VirtualAppApi->virtual_app_query_resource_config_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_query_resource_config_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ResourceConfigOption**](ResourceConfigOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | *ResourceConfigOption* object.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_refresh_runtime**
> virtual_app_refresh_runtime(mo_id)

Refreshes the resource usage data that is available in *ResourcePoolRuntimeInfo*. 

Refreshes the resource usage data that is available in *ResourcePoolRuntimeInfo*.  The latest runtime resource usage of this resource pool may not be available immediately after operations that alter resource usage, such as powering on a virtual machine. Invoke this method when resource usage may have recently changed, and the most up-to-date value in the *ResourcePoolRuntimeInfo* is needed.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Refreshes the resource usage data that is available in *ResourcePoolRuntimeInfo*. 
        api_instance.virtual_app_refresh_runtime(mo_id)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_refresh_runtime: %s\n" % e)
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

# **virtual_app_register_child_vm_task**
> ManagedObjectReference virtual_app_register_child_vm_task(mo_id, register_child_vm_request_type)

Adds an existing virtual machine to this resource pool or vApp. 

Adds an existing virtual machine to this resource pool or vApp.  This operation only works for vApps or resource pools that are children of vApps. To register a VM in a folder, see *Folder.RegisterVM_Task*.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter. In addition to the VirtualMachine.Inventory.Register privilege, it requires System.Read privilege on the datastore that the existing virtual machine resides on.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Inventory.Register 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.register_child_vm_request_type import RegisterChildVMRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_child_vm_request_type = vmware_vi.RegisterChildVMRequestType() # RegisterChildVMRequestType | 

    try:
        # Adds an existing virtual machine to this resource pool or vApp. 
        api_response = api_instance.virtual_app_register_child_vm_task(mo_id, register_child_vm_request_type)
        print("The response of VirtualAppApi->virtual_app_register_child_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_register_child_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_child_vm_request_type** | [**RegisterChildVMRequestType**](RegisterChildVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly registered *VirtualMachine* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if the operation is not supported. For example, if the operation is invoked on a resource pool that is unrelated to a vApp.  ***OutOfBounds***: if the maximum number of VMs has been exceeded.  ***AlreadyExists***: if the virtual machine is already registered.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***NotFound***: if the configuration file is not found on the system.  ***InvalidName***: if the entity name is invalid.  ***InvalidArgument***: if any of the arguments are invalid and a more specific fault type does not apply.  ***VmConfigFault***: if the format / configuration of the virtual machine is invalid. Typically, a more specific fault is thrown such as InvalidFormat if the configuration file cannot be read, or InvalidDiskFormat if the disks cannot be read.  ***FileFault***: if there is an error accessing the files on disk.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_reload**
> virtual_app_reload(mo_id)

Reload the entity state. 

Reload the entity state.  Clients only need to call this method if they changed some external state that affects the service without using the Web service interface to perform the change. For example, hand-editing a virtual machine configuration file affects the configuration of the associated virtual machine but the service managing the virtual machine might not monitor the file for changes. In this case, after such an edit, a client would call \"reload\" on the associated virtual machine to ensure the service and its clients have current data for the virtual machine.  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.virtual_app_reload(mo_id)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_reload: %s\n" % e)
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

# **virtual_app_rename_task**
> ManagedObjectReference virtual_app_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** VApp.Rename 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.rename_request_type import RenameRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.virtual_app_rename_task(mo_id, rename_request_type)
        print("The response of VirtualAppApi->virtual_app_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_rename_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_request_type** | [**RenameRequestType**](RenameRequestType.md)|  | 

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
**500** | ***DuplicateName***: If another object in the same folder has the target name.  ***InvalidName***: If the new name is not a valid entity name.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_set_custom_value**
> virtual_app_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.virtual_app_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_set_custom_value: %s\n" % e)
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

# **virtual_app_suspend_v_app_task**
> ManagedObjectReference virtual_app_suspend_v_app_task(mo_id)

Suspends this vApp. 

Suspends this vApp.  Suspends all powered-on virtual machines in a vApp, including virtual machines in child vApps. The virtual machines are suspended in the same order as used for a power-off operation (reverse power-on sequence).  While a vApp is being suspended, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.  ***Since:*** vSphere API 4.1  ***Required privileges:*** VApp.Suspend 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Suspends this vApp. 
        api_response = api_instance.virtual_app_suspend_v_app_task(mo_id)
        print("The response of VirtualAppApi->virtual_app_suspend_v_app_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_suspend_v_app_task: %s\n" % e)
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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the vApp is not running  ***TaskInProgress***: if the vApp is busy.  ***InvalidState***: if the operation cannot be performed because of the vApp&#39;s current state. For example, if the vApp is in the process of being started.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_unregister_v_app_task**
> ManagedObjectReference virtual_app_unregister_v_app_task(mo_id)

Removes this vApp from the inventory without removing any of the virtual machine's files on disk. 

Removes this vApp from the inventory without removing any of the virtual machine's files on disk.  All high-level information stored with the management server (ESX Server or VirtualCenter) is removed, including information such as vApp configuration, statistics, permissions, and alarms.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Unregister 

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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes this vApp from the inventory without removing any of the virtual machine's files on disk. 
        api_response = api_instance.virtual_app_unregister_v_app_task(mo_id)
        print("The response of VirtualAppApi->virtual_app_unregister_v_app_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_unregister_v_app_task: %s\n" % e)
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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the vApp is running.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_update_child_resource_configuration**
> virtual_app_update_child_resource_configuration(mo_id, update_child_resource_configuration_request_type)

Changes resource configuration of a set of children of this resource pool. 

Changes resource configuration of a set of children of this resource pool.  The method allows bulk modifications of the set of the direct children (virtual machines and resource pools).  Bulk modifications are not transactional. Each modification is made individually. If a failure is encountered while applying the changes, then the processing stops, meaning at least one and as many as all of the changes are not applied.  A set can include a subset of the resources. Children that are not mentioned in the list are not changed.  For each ResourceConfigSpec, the following privilege checks apply: - If the ResourceConfigSpec refers to a child resource pool or a child   vApp, the privileges required are the same as would be required for   calling *ResourcePool.UpdateConfig* on that entity. - If the ResourceConfigSpec refers to a virtual machine,   VirtualMachine.Config.Resource must be held on the virtual machine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_child_resource_configuration_request_type import UpdateChildResourceConfigurationRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_child_resource_configuration_request_type = vmware_vi.UpdateChildResourceConfigurationRequestType() # UpdateChildResourceConfigurationRequestType | 

    try:
        # Changes resource configuration of a set of children of this resource pool. 
        api_instance.virtual_app_update_child_resource_configuration(mo_id, update_child_resource_configuration_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_update_child_resource_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_child_resource_configuration_request_type** | [**UpdateChildResourceConfigurationRequestType**](UpdateChildResourceConfigurationRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if a managed entity that is not a child of this group is included.  ***InsufficientResourcesFault***: if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientMemoryResourcesFault will be thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_update_config**
> virtual_app_update_config(mo_id, update_config_request_type)

Updates the configuration of the resource pool. 

Updates the configuration of the resource pool.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  The privilege checks for this operation are as follows: - If this is a resource pool, the privilege Resource.EditPool is required on   this and on the parent pool or vApp. - If this is a vApp, the privilege VApp.ResourceConfig is required on   this and on the parent pool or vApp. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_config_request_type import UpdateConfigRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_config_request_type = vmware_vi.UpdateConfigRequestType() # UpdateConfigRequestType | 

    try:
        # Updates the configuration of the resource pool. 
        api_instance.virtual_app_update_config(mo_id, update_config_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_update_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_config_request_type** | [**UpdateConfigRequestType**](UpdateConfigRequestType.md)|  | 

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
**500** | ***InvalidName***: if the name is not a valid entity name.  ***DuplicateName***: if the name is changed to an already existing name.  ***InvalidArgument***: if the parameters are out of range, or if the reservationLimit field is set.  ***InsufficientResourcesFault***: if the pool specification cannot be supported by the parent resource pool or vApp.  ***ConcurrentAccess***: if the changeVersion does not match the server&#39;s changeVersion for the configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_update_linked_children**
> virtual_app_update_linked_children(mo_id, update_linked_children_request_type)

Reconfigure the set of linked children. 

Deprecated as of vSphere API 5.1.  Reconfigure the set of linked children.  A VirtualMachine and vApp can be added as a linked child as long as it is not a direct child of another vApp. In case it is a linked child, the existing link is removed and replaced with the new link specified in this call.  An InvalidArgument fault is thrown if a link target is a direct child of another vApp, or if the addition of the link will result in a vApp with a cycle. For example, a vApp cannot be linked to itself.  The removeSet must refer to managed entities that are currently linked children. Otherwise, an InvalidArgument exception is thrown.  For each entity being linked, the operation is subject to the following privilege checks: - If the object being linked is a vApp, VApp.Move must be held on   the vApp being linked and its former parent vApp (if any). The privilege   VApp.AssignVApp must be held on this vApp. - If the object being linked is a VirtualMachine, VApp.AssignVM is required on   both the target vApp, the VirtualMachine, and its former parent vApp (if any).    Privilege checks for each entity in the removeSet are similar to the entities in the addChangeSet, except that there is no target vApp.  This operation is only transactional with respect to each individual link change. The changes are processed sequentially and committed one at a time. The addChangeSet is processed first, followed by the removeSet. If a failure is detected, then the method terminates with an exception.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_linked_children_request_type import UpdateLinkedChildrenRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_linked_children_request_type = vmware_vi.UpdateLinkedChildrenRequestType() # UpdateLinkedChildrenRequestType | 

    try:
        # Reconfigure the set of linked children. 
        api_instance.virtual_app_update_linked_children(mo_id, update_linked_children_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_update_linked_children: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_linked_children_request_type** | [**UpdateLinkedChildrenRequestType**](UpdateLinkedChildrenRequestType.md)|  | 

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
**500** | ***InvalidArgument***: See above description.  ***ConcurrentAccess***: If a concurrent modification happens while adding the link.  ***NotSupported***: If the target of the link is not in the same datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_app_update_v_app_config**
> virtual_app_update_v_app_config(mo_id, update_v_app_config_request_type)

Updates the vApp configuration. 

Updates the vApp configuration.  Updates in different areas require different privileges. See *VAppConfigSpec* for a full description.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_v_app_config_request_type import UpdateVAppConfigRequestType
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
    api_instance = vmware_vi.VirtualAppApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_v_app_config_request_type = vmware_vi.UpdateVAppConfigRequestType() # UpdateVAppConfigRequestType | 

    try:
        # Updates the vApp configuration. 
        api_instance.virtual_app_update_v_app_config(mo_id, update_v_app_config_request_type)
    except Exception as e:
        print("Exception when calling VirtualAppApi->virtual_app_update_v_app_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_v_app_config_request_type** | [**UpdateVAppConfigRequestType**](UpdateVAppConfigRequestType.md)|  | 

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
**500** | ***InvalidPowerState***: if the reconfiguration is not possible given the current powerState of the vApp.  ***TaskInProgress***: if the vApp is busy.  ***ConcurrentAccess***: if another operation conflicted with this operation.  ***InvalidArgument***: for wrong input.  ***InvalidIndexArgument***: if a wrong key is used in one of the arrays. For example, for duplicated entries in entityConfig.  ***VmConfigFault***: for bad configuration, such as invalid property types.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

