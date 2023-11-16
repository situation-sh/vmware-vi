# vmware_vi.FolderApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_add_standalone_host_task**](FolderApi.md#folder_add_standalone_host_task) | **POST** /Folder/{moId}/AddStandaloneHost_Task | Creates a new single-host compute resource. 
[**folder_batch_add_hosts_to_cluster_task**](FolderApi.md#folder_batch_add_hosts_to_cluster_task) | **POST** /Folder/{moId}/BatchAddHostsToCluster_Task | Adds a set of new and existing hosts to the cluster. 
[**folder_batch_add_standalone_hosts_task**](FolderApi.md#folder_batch_add_standalone_hosts_task) | **POST** /Folder/{moId}/BatchAddStandaloneHosts_Task | Adds a list of hosts to inventory, as standalone hosts, in a single invocation. 
[**folder_create_cluster**](FolderApi.md#folder_create_cluster) | **POST** /Folder/{moId}/CreateCluster | Creates a new cluster compute resource in this folder. 
[**folder_create_cluster_ex**](FolderApi.md#folder_create_cluster_ex) | **POST** /Folder/{moId}/CreateClusterEx | Creates a new cluster compute resource in this folder. 
[**folder_create_datacenter**](FolderApi.md#folder_create_datacenter) | **POST** /Folder/{moId}/CreateDatacenter | Creates a new datacenter with the given name. 
[**folder_create_dvs_task**](FolderApi.md#folder_create_dvs_task) | **POST** /Folder/{moId}/CreateDVS_Task | Create a *DistributedVirtualSwitch* in the folder according to the specified *DVSCreateSpec*. 
[**folder_create_folder**](FolderApi.md#folder_create_folder) | **POST** /Folder/{moId}/CreateFolder | Creates a new sub-folder with the specified name. 
[**folder_create_storage_pod**](FolderApi.md#folder_create_storage_pod) | **POST** /Folder/{moId}/CreateStoragePod | Creates a new storage pod in this folder. 
[**folder_create_vm_task**](FolderApi.md#folder_create_vm_task) | **POST** /Folder/{moId}/CreateVM_Task | Creates a new virtual machine in the current folder and attaches it to the specified resource pool. 
[**folder_destroy_task**](FolderApi.md#folder_destroy_task) | **POST** /Folder/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**folder_get_alarm_actions_enabled**](FolderApi.md#folder_get_alarm_actions_enabled) | **GET** /Folder/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**folder_get_available_field**](FolderApi.md#folder_get_available_field) | **GET** /Folder/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**folder_get_child_entity**](FolderApi.md#folder_get_child_entity) | **GET** /Folder/{moId}/childEntity | An array of managed object references. 
[**folder_get_child_type**](FolderApi.md#folder_get_child_type) | **GET** /Folder/{moId}/childType | Specifies the object types a folder may contain. 
[**folder_get_config_issue**](FolderApi.md#folder_get_config_issue) | **GET** /Folder/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**folder_get_config_status**](FolderApi.md#folder_get_config_status) | **GET** /Folder/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**folder_get_custom_value**](FolderApi.md#folder_get_custom_value) | **GET** /Folder/{moId}/customValue | Custom field values. 
[**folder_get_declared_alarm_state**](FolderApi.md#folder_get_declared_alarm_state) | **GET** /Folder/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**folder_get_disabled_method**](FolderApi.md#folder_get_disabled_method) | **GET** /Folder/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**folder_get_effective_role**](FolderApi.md#folder_get_effective_role) | **GET** /Folder/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**folder_get_name**](FolderApi.md#folder_get_name) | **GET** /Folder/{moId}/name | Name of this entity, unique relative to its parent. 
[**folder_get_namespace**](FolderApi.md#folder_get_namespace) | **GET** /Folder/{moId}/namespace | The namespace with which the Folder is associated. 
[**folder_get_overall_status**](FolderApi.md#folder_get_overall_status) | **GET** /Folder/{moId}/overallStatus | General health of this managed entity. 
[**folder_get_parent**](FolderApi.md#folder_get_parent) | **GET** /Folder/{moId}/parent | Parent of this entity. 
[**folder_get_permission**](FolderApi.md#folder_get_permission) | **GET** /Folder/{moId}/permission | List of permissions defined for this entity. 
[**folder_get_recent_task**](FolderApi.md#folder_get_recent_task) | **GET** /Folder/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**folder_get_tag**](FolderApi.md#folder_get_tag) | **GET** /Folder/{moId}/tag | The set of tags associated with this managed entity. 
[**folder_get_triggered_alarm_state**](FolderApi.md#folder_get_triggered_alarm_state) | **GET** /Folder/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**folder_get_value**](FolderApi.md#folder_get_value) | **GET** /Folder/{moId}/value | List of custom field values. 
[**folder_move_into_folder_task**](FolderApi.md#folder_move_into_folder_task) | **POST** /Folder/{moId}/MoveIntoFolder_Task | Moves a set of managed entities into this folder. 
[**folder_register_vm_task**](FolderApi.md#folder_register_vm_task) | **POST** /Folder/{moId}/RegisterVM_Task | Adds an existing virtual machine to the folder. 
[**folder_reload**](FolderApi.md#folder_reload) | **POST** /Folder/{moId}/Reload | Reload the entity state. 
[**folder_rename_task**](FolderApi.md#folder_rename_task) | **POST** /Folder/{moId}/Rename_Task | Renames this managed entity. 
[**folder_set_custom_value**](FolderApi.md#folder_set_custom_value) | **POST** /Folder/{moId}/setCustomValue | Assigns a value to a custom field. 
[**folder_unregister_and_destroy_task**](FolderApi.md#folder_unregister_and_destroy_task) | **POST** /Folder/{moId}/UnregisterAndDestroy_Task | Recursively unregisters all virtual machines and vApps, and destroys all child virtual machine folders. 


# **folder_add_standalone_host_task**
> ManagedObjectReference folder_add_standalone_host_task(mo_id, add_standalone_host_request_type)

Creates a new single-host compute resource. 

Creates a new single-host compute resource.  The name provided can be an IP address, such as 192.168.0.120, or a string, such as esx120. If a name is specified, a DNS lookup is used to resolve it to a fully-qualified name, such as esx120.vmware.com. If the DNS lookup fails, the string is stored as specified.  Licenses for the host are allocated when making the first connection to the host. This is because the license needed typically depends on the type of host and the number of CPUs.  In addition to the Host.Inventory.AddStandaloneHost privilege, it requires System.View privilege on the VM folder that the VMs of the host will be placed on.  ***Required privileges:*** Host.Inventory.AddStandaloneHost 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_standalone_host_request_type import AddStandaloneHostRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_standalone_host_request_type = vmware_vi.AddStandaloneHostRequestType() # AddStandaloneHostRequestType | 

    try:
        # Creates a new single-host compute resource. 
        api_response = api_instance.folder_add_standalone_host_task(mo_id, add_standalone_host_request_type)
        print("The response of FolderApi->folder_add_standalone_host_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_add_standalone_host_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_standalone_host_request_type** | [**AddStandaloneHostRequestType**](AddStandaloneHostRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly added *ComputeResource* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidLogin***: if authentication with the host fails.  ***InvalidArgument***: if an argument is specified incorrectly.  ***AlreadyBeingManaged***: if the host is already being managed by a vCenter server. If the host is being managed by a different vCenter server, this can be overridden by the \&quot;force\&quot; flag in the connection specification.  ***NotEnoughLicenses***: if there are not enough licenses to add the host.  ***NoHost***: if the host cannot be contacted.  ***NotSupported***: if the host is being added to a folder whose *Folder.childType* property does not contain \&quot;ComputeResource\&quot;.  ***NotSupportedHost***: if the host is running a software version that is not supported.  ***AgentInstallFailed***: if there is an error installing the vCenter agent on the new host.  ***AlreadyConnected***: if addConnected is true and the host is already connected to vCenter.  ***HostConnectFault***: if an error occurred when attempting to connect to a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.  ***SSLVerifyFault***: if the host certificate could not be authenticated  ***DuplicateName***: if another host in the same folder has the name.  ***NoPermission***: if there are crypto keys to be sent to the host, but the user does not have Cryptographer.RegisterHost privilege on the Folder.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_batch_add_hosts_to_cluster_task**
> ManagedObjectReference folder_batch_add_hosts_to_cluster_task(mo_id, batch_add_hosts_to_cluster_request_type)

Adds a set of new and existing hosts to the cluster. 

Adds a set of new and existing hosts to the cluster.  This API is a composite API and performs the following tasks before hosts become part of the specified cluter - - Adds all new hosts as standalone hosts. - Move each host to the desired state. - Move each host to the cluster.    The dynamic privilege check will ensure that appropriate privileges are acquired to allow this API to perform multiple actions on hosts and cluster. Required privileges - - Host.Inventory.EditCluster on cluster - Host.Config.Maintenance on the hosts if desiredState is set - Privileges for *Folder.BatchAddStandaloneHosts_Task* if newHosts is   set - Host.Inventory.EditCluster on the hosts' source ComputeResource - Host.Inventory.MoveHost on the hosts        ***Since:*** vSphere API 6.7.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.batch_add_hosts_to_cluster_request_type import BatchAddHostsToClusterRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    batch_add_hosts_to_cluster_request_type = vmware_vi.BatchAddHostsToClusterRequestType() # BatchAddHostsToClusterRequestType | 

    try:
        # Adds a set of new and existing hosts to the cluster. 
        api_response = api_instance.folder_batch_add_hosts_to_cluster_task(mo_id, batch_add_hosts_to_cluster_request_type)
        print("The response of FolderApi->folder_batch_add_hosts_to_cluster_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_batch_add_hosts_to_cluster_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **batch_add_hosts_to_cluster_request_type** | [**BatchAddHostsToClusterRequestType**](BatchAddHostsToClusterRequestType.md)|  | 

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

# **folder_batch_add_standalone_hosts_task**
> ManagedObjectReference folder_batch_add_standalone_hosts_task(mo_id, batch_add_standalone_hosts_request_type)

Adds a list of hosts to inventory, as standalone hosts, in a single invocation. 

Adds a list of hosts to inventory, as standalone hosts, in a single invocation.  The operation returns a result containing a list of hosts that are successfully added.  In addition to the Host.Inventory.AddStandaloneHost privilege, the operation requires System.View privilege on the VM folder that the VMs of the host will be placed on.  ***Since:*** vSphere API 6.7.1  ***Required privileges:*** Host.Inventory.AddStandaloneHost 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.batch_add_standalone_hosts_request_type import BatchAddStandaloneHostsRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    batch_add_standalone_hosts_request_type = vmware_vi.BatchAddStandaloneHostsRequestType() # BatchAddStandaloneHostsRequestType | 

    try:
        # Adds a list of hosts to inventory, as standalone hosts, in a single invocation. 
        api_response = api_instance.folder_batch_add_standalone_hosts_task(mo_id, batch_add_standalone_hosts_request_type)
        print("The response of FolderApi->folder_batch_add_standalone_hosts_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_batch_add_standalone_hosts_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **batch_add_standalone_hosts_request_type** | [**BatchAddStandaloneHostsRequestType**](BatchAddStandaloneHostsRequestType.md)|  | 

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

# **folder_create_cluster**
> ManagedObjectReference folder_create_cluster(mo_id, create_cluster_request_type)

Creates a new cluster compute resource in this folder. 

Deprecated as of VI API 2.5, use *Folder.CreateClusterEx*.  Creates a new cluster compute resource in this folder.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Required privileges:*** Host.Inventory.CreateCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_cluster_request_type import CreateClusterRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_cluster_request_type = vmware_vi.CreateClusterRequestType() # CreateClusterRequestType | 

    try:
        # Creates a new cluster compute resource in this folder. 
        api_response = api_instance.folder_create_cluster(mo_id, create_cluster_request_type)
        print("The response of FolderApi->folder_create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_cluster_request_type** | [**CreateClusterRequestType**](CreateClusterRequestType.md)|  | 

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
**200** | A new ClusterComputeResource instance.  Refers instance of *ClusterComputeResource*.  |  -  |
**500** | ***DuplicateName***: if an entity with that name already exists.  ***InvalidArgument***: if the cluster configuration specification parameter is invalid.  ***InvalidName***: if the name is not a valid entity name.  ***NotSupported***: if the cluster is being added to a folder whose *Folder.childType* property value does not contain \&quot;ComputeResource\&quot; or \&quot;ClusterComputeResource\&quot;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_cluster_ex**
> ManagedObjectReference folder_create_cluster_ex(mo_id, create_cluster_ex_request_type)

Creates a new cluster compute resource in this folder. 

Creates a new cluster compute resource in this folder.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Inventory.CreateCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_cluster_ex_request_type import CreateClusterExRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_cluster_ex_request_type = vmware_vi.CreateClusterExRequestType() # CreateClusterExRequestType | 

    try:
        # Creates a new cluster compute resource in this folder. 
        api_response = api_instance.folder_create_cluster_ex(mo_id, create_cluster_ex_request_type)
        print("The response of FolderApi->folder_create_cluster_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_cluster_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_cluster_ex_request_type** | [**CreateClusterExRequestType**](CreateClusterExRequestType.md)|  | 

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
**200** | A new ClusterComputeResource instance.  Refers instance of *ClusterComputeResource*.  |  -  |
**500** | ***DuplicateName***: if an entity with that name already exists.  ***InvalidArgument***: if the cluster configuration specification parameter is invalid.  ***InvalidName***: if the name is not a valid entity name.  ***NotSupported***: if the cluster is being added to a folder whose *Folder.childType* property value does not contain \&quot;ComputeResource\&quot; or \&quot;ClusterComputeResource\&quot;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_datacenter**
> ManagedObjectReference folder_create_datacenter(mo_id, create_datacenter_request_type)

Creates a new datacenter with the given name. 

Creates a new datacenter with the given name.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Required privileges:*** Datacenter.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_datacenter_request_type import CreateDatacenterRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_datacenter_request_type = vmware_vi.CreateDatacenterRequestType() # CreateDatacenterRequestType | 

    try:
        # Creates a new datacenter with the given name. 
        api_response = api_instance.folder_create_datacenter(mo_id, create_datacenter_request_type)
        print("The response of FolderApi->folder_create_datacenter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_datacenter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_datacenter_request_type** | [**CreateDatacenterRequestType**](CreateDatacenterRequestType.md)|  | 

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
**200** | A new Datacenter instance.  Refers instance of *Datacenter*.  |  -  |
**500** | ***DuplicateName***: if an entity with that name already exists.  ***InvalidName***: if the new name is not a valid entity name.  ***NotSupported***: if the datacenter is being created within a folder whose *Folder.childType* property value does not contain \&quot;Datacenter\&quot;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_dvs_task**
> ManagedObjectReference folder_create_dvs_task(mo_id, create_dvs_request_type)

Create a *DistributedVirtualSwitch* in the folder according to the specified *DVSCreateSpec*. 

Create a *DistributedVirtualSwitch* in the folder according to the specified *DVSCreateSpec*.  The specified Folder must be a Network entity folder.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_dvs_request_type import CreateDVSRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_dvs_request_type = vmware_vi.CreateDVSRequestType() # CreateDVSRequestType | 

    try:
        # Create a *DistributedVirtualSwitch* in the folder according to the specified *DVSCreateSpec*. 
        api_response = api_instance.folder_create_dvs_task(mo_id, create_dvs_request_type)
        print("The response of FolderApi->folder_create_dvs_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_dvs_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_dvs_request_type** | [**CreateDVSRequestType**](CreateDVSRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. After successful completion, the *Task*.*Task.info*.*TaskInfo.result* property contains the newly registered *DistributedVirtualSwitch*.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if called directly on a host.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match (*DVSConfigInfo.extensionKey*).  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_folder**
> ManagedObjectReference folder_create_folder(mo_id, create_folder_request_type)

Creates a new sub-folder with the specified name. 

Creates a new sub-folder with the specified name.  The *Folder.childType* property of the new folder is the same as the *Folder.childType* property of the current folder.  ***Required privileges:*** Folder.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_folder_request_type import CreateFolderRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_folder_request_type = vmware_vi.CreateFolderRequestType() # CreateFolderRequestType | 

    try:
        # Creates a new sub-folder with the specified name. 
        api_response = api_instance.folder_create_folder(mo_id, create_folder_request_type)
        print("The response of FolderApi->folder_create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_folder: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_folder_request_type** | [**CreateFolderRequestType**](CreateFolderRequestType.md)|  | 

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
**200** | A reference to the new folder.  Refers instance of *Folder*.  |  -  |
**500** | ***DuplicateName***: if another object in the same folder has the target name.  ***InvalidName***: if the name is not a valid entity name.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_storage_pod**
> ManagedObjectReference folder_create_storage_pod(mo_id, create_storage_pod_request_type)

Creates a new storage pod in this folder. 

Creates a new storage pod in this folder.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Folder.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_storage_pod_request_type import CreateStoragePodRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_storage_pod_request_type = vmware_vi.CreateStoragePodRequestType() # CreateStoragePodRequestType | 

    try:
        # Creates a new storage pod in this folder. 
        api_response = api_instance.folder_create_storage_pod(mo_id, create_storage_pod_request_type)
        print("The response of FolderApi->folder_create_storage_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_storage_pod: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_storage_pod_request_type** | [**CreateStoragePodRequestType**](CreateStoragePodRequestType.md)|  | 

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
**200** | A new StoragePod instance.  Refers instance of *StoragePod*.  |  -  |
**500** | ***DuplicateName***: if an entity with that name already exists.  ***InvalidName***: if the name is not a valid entity name.  ***NotSupported***: if the storage pod is being added to a folder whose *Folder.childType* property value does not contain \&quot;StoragePod\&quot;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_create_vm_task**
> ManagedObjectReference folder_create_vm_task(mo_id, create_vm_request_type)

Creates a new virtual machine in the current folder and attaches it to the specified resource pool. 

Creates a new virtual machine in the current folder and attaches it to the specified resource pool.  This operation creates a virtual machine, instead of cloning a virtual machine from an existing one.  The server does not support creating templates using this method. Instead, you should create templates by marking existing virtual machines as templates, or by cloning an existing virtual machine or template.  This operation only works if the folder's childType includes VirtualMachine. In addition to the VirtualMachine.Inventory.Create privilege, may also require any of the following privileges depending on the properties of the virtual machine bring created: - VirtualMachine.Config.AddExistingDisk if including a virtual disk device   that refers to an existing virtual disk file (not RDM) - VirtualMachine.Config.AddNewDisk if including a virtual disk device that   creates a new virtual disk file (not RDM) - VirtualMachine.Config.RawDevice if including a raw device mapping   (RDM) or SCSI passthrough device - VirtualMachine.Config.HostUSBDevice if including a VirtualUSB device   backed by a host USB device - VirtualMachine.Config.AdvancedConfig if setting values in   ConfigSpec.extraConfig - VirtualMachine.Config.SwapPlacement if setting swapPlacement - VirtualMachine.Config.ChangeTracking if setting changed   block tracking for the virtual machine's disks. - Datastore.AllocateSpace required on all datastores where the   virtual machine and its virtual disks will be created - Network.Assign required on the network which is assigned to the   new virtual machine that is being created - Cryptographer.EncryptNew on the folder if the created virtual   machine is encrypted - Cryptographer.RegisterHost on the host if the created virtual   machine is encrypted, but encryption is not enabled on the host    To create a VirtualDisk on a persistent memory storage, the storage must be specified via *profile* while the datastore property of corresponding VirtualDisk backing must be unset.  To create a VirtualNVDIMM device, the storage *profile* must be set to the default persistent memory storage profile while the datastore property of *the device backing* must be unset.  ***Required privileges:*** VirtualMachine.Inventory.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_vm_request_type import CreateVMRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_vm_request_type = vmware_vi.CreateVMRequestType() # CreateVMRequestType | 

    try:
        # Creates a new virtual machine in the current folder and attaches it to the specified resource pool. 
        api_response = api_instance.folder_create_vm_task(mo_id, create_vm_request_type)
        print("The response of FolderApi->folder_create_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_create_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_vm_request_type** | [**CreateVMRequestType**](CreateVMRequestType.md)|  | 

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
**500** | ***VmConfigFault***: if the configSpec has incorrect values. Typically, a more specific subclass is thrown.  ***OutOfBounds***: if Host.capability.maxSupportedVMs is exceeded.  ***FileAlreadyExists***: if the requested cfgPath for the virtual machine&#39;s configuration file already exists.  ***FileFault***: if there is a problem creating the virtual machine on disk. Typically, a more specific subclass, such as NoDiskSpace, will be thrown.  ***DuplicateName***: if another virtual machine in the same folder already has the specified target name.  ***InvalidName***: if the name is not a valid entity name.  ***NotSupported***: if the virtual machine is being created within a folder whose *Folder.childType* property is not set to \&quot;VirtualMachine\&quot;.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***VmWwnConflict***: if the WWN of the virtual machine has been used by other virtual machines.  ***AlreadyExists***: if the requested cfgPath (or the default cfgPath) for the virtual machine&#39;s configuration file is already loaded in the inventory.  ***InvalidState***: if the operation is not allowed in current state of the entities involved.  ***NoPermission***: if the created virtual machine is encrypted but the user does not have Cryptographer.EncryptNew on the folder.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_destroy_task**
> ManagedObjectReference folder_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** Folder.Delete 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.folder_destroy_task(mo_id)
        print("The response of FolderApi->folder_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_destroy_task: %s\n" % e)
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

# **folder_get_alarm_actions_enabled**
> bool folder_get_alarm_actions_enabled(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.folder_get_alarm_actions_enabled(mo_id)
        print("The response of FolderApi->folder_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_alarm_actions_enabled: %s\n" % e)
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

# **folder_get_available_field**
> List[CustomFieldDef] folder_get_available_field(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.folder_get_available_field(mo_id)
        print("The response of FolderApi->folder_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_available_field: %s\n" % e)
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

# **folder_get_child_entity**
> List[ManagedObjectReference] folder_get_child_entity(mo_id)

An array of managed object references. 

An array of managed object references.  Each entry is a reference to a child entity.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # An array of managed object references. 
        api_response = api_instance.folder_get_child_entity(mo_id)
        print("The response of FolderApi->folder_get_child_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_child_entity: %s\n" % e)
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
**200** | Refers instances of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_get_child_type**
> List[str] folder_get_child_type(mo_id)

Specifies the object types a folder may contain. 

Specifies the object types a folder may contain.  When you create a folder, it inherits its childType from the parent folder in which it is created. childType is an array of strings. Each array entry identifies a set of object types - Folder and one or more managed object types. The following list shows childType values for the different folders: - { \"vim.Folder\", \"vim.Datacenter\" } - Identifies the root folder   and its descendant folders. Data center folders can contain   child data center folders and Datacenter managed objects.   Datacenter objects contain virtual machine, compute resource,   network entity, and datastore folders. - { \"vim.Folder\", \"vim.Virtualmachine\", \"vim.VirtualApp\" } - Identifies   a virtual machine folder. A virtual machine folder may contain child   virtual machine folders. It also can contain VirtualMachine managed objects,   templates, and VirtualApp managed objects. - { \"vim.Folder\", \"vim.ComputeResource\" } - Identifies a   compute resource folder, which contains child compute resource folders   and ComputeResource hierarchies. - { \"vim.Folder\", \"vim.Network\" } - Identifies a network entity folder.   Network entity folders on a vCenter Server can contain Network,   DistributedVirtualSwitch, and DistributedVirtualPortgroup managed   objects. Network entity folders on an ESXi host can contain only   Network objects. - { \"vim.Folder\", \"vim.Datastore\" } - Identifies a datastore folder.   Datastore folders can contain child datastore folders and Datastore   managed objects.    ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Specifies the object types a folder may contain. 
        api_response = api_instance.folder_get_child_type(mo_id)
        print("The response of FolderApi->folder_get_child_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_child_type: %s\n" % e)
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

# **folder_get_config_issue**
> List[Event] folder_get_config_issue(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.folder_get_config_issue(mo_id)
        print("The response of FolderApi->folder_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_config_issue: %s\n" % e)
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

# **folder_get_config_status**
> ManagedEntityStatusEnum folder_get_config_status(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.folder_get_config_status(mo_id)
        print("The response of FolderApi->folder_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_config_status: %s\n" % e)
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

# **folder_get_custom_value**
> List[CustomFieldValue] folder_get_custom_value(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.folder_get_custom_value(mo_id)
        print("The response of FolderApi->folder_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_custom_value: %s\n" % e)
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

# **folder_get_declared_alarm_state**
> List[AlarmState] folder_get_declared_alarm_state(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.folder_get_declared_alarm_state(mo_id)
        print("The response of FolderApi->folder_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_declared_alarm_state: %s\n" % e)
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

# **folder_get_disabled_method**
> List[str] folder_get_disabled_method(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.folder_get_disabled_method(mo_id)
        print("The response of FolderApi->folder_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_disabled_method: %s\n" % e)
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

# **folder_get_effective_role**
> List[int] folder_get_effective_role(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.folder_get_effective_role(mo_id)
        print("The response of FolderApi->folder_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_effective_role: %s\n" % e)
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

# **folder_get_name**
> str folder_get_name(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.folder_get_name(mo_id)
        print("The response of FolderApi->folder_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_name: %s\n" % e)
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

# **folder_get_namespace**
> str folder_get_namespace(mo_id)

The namespace with which the Folder is associated. 

The namespace with which the Folder is associated.  Namespace is a vAPI resource which divides cluster resources and allows administrators to give Kubernetes environments to their development teams. This property is set only at the time of creation and cannot change.  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The namespace with which the Folder is associated. 
        api_response = api_instance.folder_get_namespace(mo_id)
        print("The response of FolderApi->folder_get_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_namespace: %s\n" % e)
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

# **folder_get_overall_status**
> ManagedEntityStatusEnum folder_get_overall_status(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.folder_get_overall_status(mo_id)
        print("The response of FolderApi->folder_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_overall_status: %s\n" % e)
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

# **folder_get_parent**
> ManagedObjectReference folder_get_parent(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.folder_get_parent(mo_id)
        print("The response of FolderApi->folder_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_parent: %s\n" % e)
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

# **folder_get_permission**
> List[Permission] folder_get_permission(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.folder_get_permission(mo_id)
        print("The response of FolderApi->folder_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_permission: %s\n" % e)
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

# **folder_get_recent_task**
> List[ManagedObjectReference] folder_get_recent_task(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.folder_get_recent_task(mo_id)
        print("The response of FolderApi->folder_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_recent_task: %s\n" % e)
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

# **folder_get_tag**
> List[Tag] folder_get_tag(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.folder_get_tag(mo_id)
        print("The response of FolderApi->folder_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_tag: %s\n" % e)
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

# **folder_get_triggered_alarm_state**
> List[AlarmState] folder_get_triggered_alarm_state(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.folder_get_triggered_alarm_state(mo_id)
        print("The response of FolderApi->folder_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_triggered_alarm_state: %s\n" % e)
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

# **folder_get_value**
> List[CustomFieldValue] folder_get_value(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.folder_get_value(mo_id)
        print("The response of FolderApi->folder_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_get_value: %s\n" % e)
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

# **folder_move_into_folder_task**
> ManagedObjectReference folder_move_into_folder_task(mo_id, move_into_folder_request_type)

Moves a set of managed entities into this folder. 

Moves a set of managed entities into this folder.  This operation is typically used by clients when they implement a drag-and-drop interface to move a set of objects into a folder.  This operation is transactional only with respect to each individual entity. The set of entities is moved sequentially as specified in the list, and committed one at a time. If the *Folder.MoveIntoFolder_Task* method fails on an object, the method terminates at that point with an exception, leaving the rest of the managed entities in their original location.  The objects that can be moved into a folder depends on the folder's type (as defined by the folder's *Folder.childType* property). For a datacenter folder, only datacenters and datacenter folders can be moved into the folder. For a virtual machine folder, only virtual machines and virtual machine folders can be moved into the folder. For a host folder, ComputeResource objects, host folder objects, and HostSystem objects can be moved into the folder.  Moving a HostSystem into a host folder creates a stand-alone host from a host that is currently part of a ClusterComputeResource. The host must be part of a ClusterComputeResource in the same datacenter and the host must be in maintenance mode. Otherwise, the operation fails.  A ComputeResource with a single root resource pool is created for each HostSystem. The name of the ComputeResource is the DNS or IP address of the host. This operation moves the (physical) host resources out of a cluster. It does not move or change the ResourcePool configuration that is part of the ClusterComputeResource with which the host was associated.  Note that all virtual machines associated with a host are moved with the host into the folder. If there are virtual machines that should not be moved with the host, then migrate them from the host before initiating this operation.  For a HostSystem move, the privileges required are Host.Inventory.EditCluster on the source ClusterComputeResource, Host.Inventory.MoveHost on the HostSystem, and Host.Inventory.AddStandaloneHost on the target Folder.  Otherwise, the privilege required for this operation varies depending on this folder's type and is checked against the source container, destination container, and the object: - Folder.Move if the object is a Folder - Datacenter.Move if the object is a Datacenter - Host.Inventory.MoveCluster if the object is a ComputeResource - VirtualMachine.Inventory.Move if the object is a virtual machine   or virtual machine template - DVSwitch.Move if the object is a DistributedVirtualSwitch - Datastore.Move if the object is a datastore - Network.Move if the object is a network    If the object is a HostSystem, the privileges required are Host.Inventory.AddStandaloneHost on the folder, Host.Inventory.MoveHost on the HostSystem, and Host.Inventory.EditCluster on the host's original ComputeResource. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_into_folder_request_type import MoveIntoFolderRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_into_folder_request_type = vmware_vi.MoveIntoFolderRequestType() # MoveIntoFolderRequestType | 

    try:
        # Moves a set of managed entities into this folder. 
        api_response = api_instance.folder_move_into_folder_task(mo_id, move_into_folder_request_type)
        print("The response of FolderApi->folder_move_into_folder_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_move_into_folder_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_into_folder_request_type** | [**MoveIntoFolderRequestType**](MoveIntoFolderRequestType.md)|  | 

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
**500** | ***DuplicateName***: if this folder already contains an object with the specified name.  ***InvalidFolder***: if a Folder that is a parent of this Folder is part of the list of objects.  ***InvalidState***: if a HostSystem is not part of the same datacenter, not part of a ClusterComputeResource, or not in maintenance mode.  ***NotSupported***: if the entity is being moved into a folder whose *Folder.childType* property is not set to the appropriate value. For example, a VirtualMachine entity cannot be moved into a folder whose ChildType property value does not contain \&quot;VirtualMachine\&quot;.  ***DisallowedOperationOnFailoverHost***: if the host is being moved out of a cluster and was configured as a failover host in that cluster. See *ClusterFailoverHostAdmissionControlPolicy*.  ***VmAlreadyExistsInDatacenter***: if moving a standalone host between datacenters, and one or more of the host&#39;s virtual machines is already registered to a host in the destination datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_register_vm_task**
> ManagedObjectReference folder_register_vm_task(mo_id, register_vm_request_type)

Adds an existing virtual machine to the folder. 

Adds an existing virtual machine to the folder.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  This operation only works if the folder's type is VirtualMachine. In addition to the VirtualMachine.Inventory.Register and Resource.AssignVMToPool privileges, it requires System.Read privilege on the datastore that the existing virtual machine resides on. If the virtual machine is encrypted Cryptographer.RegisterVM is required on the folder, in which the virtual machine is registered. Otherwise, the VM is registered successfully, but is left in the locked state.  ***Required privileges:*** VirtualMachine.Inventory.Register 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.register_vm_request_type import RegisterVMRequestType
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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_vm_request_type = vmware_vi.RegisterVMRequestType() # RegisterVMRequestType | 

    try:
        # Adds an existing virtual machine to the folder. 
        api_response = api_instance.folder_register_vm_task(mo_id, register_vm_request_type)
        print("The response of FolderApi->folder_register_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_register_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_vm_request_type** | [**RegisterVMRequestType**](RegisterVMRequestType.md)|  | 

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
**500** | ***NotSupported***: if the operation is not supported. For example, templates are not supported directly on hosts. Also, if the operation is invoked on a folder whose *Folder.childType* property is not set to \&quot;VirtualMachine\&quot;.  ***OutOfBounds***: if the maximum number of VMs for this folder has been exceeded. The maximum number is determined by Host.capability.maxSupportedVMs.  ***DuplicateName***: if another virtual machine in the same folder has the target name.  ***AlreadyExists***: if the virtual machine is already registered.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***NotFound***: if the configuration file is not found on the system.  ***InvalidName***: if the entity name is invalid.  ***InvalidArgument***: if any of the arguments such as host or resource pool are not set to valid values.  ***VmConfigFault***: if the format / configuration of the virtual machine is invalid. Typically, a more specific fault is thrown such as InvalidFormat if the configuration file cannot be read, or InvalidDiskFormat if the disks cannot be read.  ***FileFault***: if there is an error accessing the files on disk.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidState***: if the operation is not allowed in current state of the entities involved.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_reload**
> folder_reload(mo_id)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.folder_reload(mo_id)
    except Exception as e:
        print("Exception when calling FolderApi->folder_reload: %s\n" % e)
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

# **folder_rename_task**
> ManagedObjectReference folder_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** Folder.Rename 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.folder_rename_task(mo_id, rename_request_type)
        print("The response of FolderApi->folder_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_rename_task: %s\n" % e)
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

# **folder_set_custom_value**
> folder_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.folder_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling FolderApi->folder_set_custom_value: %s\n" % e)
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

# **folder_unregister_and_destroy_task**
> ManagedObjectReference folder_unregister_and_destroy_task(mo_id)

Recursively unregisters all virtual machines and vApps, and destroys all child virtual machine folders. 

Recursively unregisters all virtual machines and vApps, and destroys all child virtual machine folders.  This is similar to the Destroy\\_Task method, but this method calls UnregisterAndDestroy\\_Task on each virtual machine object instead of calling Destroy\\_Task. This operation applies only to VirtualMachine folders.  UnregisterAndDestroy\\_Task is a recursive operation that destroys the specified virtual machine folder, unregisters all child virtual machine objects, and destroys all child virtual machine folders. When you call UnregisterAndDestroy\\_Task to destroy a virtual machine folder, the system uses the specified folder as a root and traverses its descendant hierarchy, calling UnregisterAndDestroy\\_Task on each virtual machine object and Destroy\\_Task on each virtual machine folder. UnregisterAndDestroy\\_Task is a single operation that treats each recursive call as a single transaction, committing each call to remove an object individually. If a failure occurs, the method terminates at that point with an exception, leaving some or all objects unaffected.  If you are removing virtual machines, you must hold the VirtualMachine.Delete privilege on all of the virtual machines to be unregistered, and on their parent folders. If you are removing virtual applications, you must hold the VApp.Delete privilege on all of the virtual applications to be unregistered, and on their parent folders.  ***Required privileges:*** Folder.Delete 

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
    api_instance = vmware_vi.FolderApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Recursively unregisters all virtual machines and vApps, and destroys all child virtual machine folders. 
        api_response = api_instance.folder_unregister_and_destroy_task(mo_id)
        print("The response of FolderApi->folder_unregister_and_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderApi->folder_unregister_and_destroy_task: %s\n" % e)
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
**500** | ***InvalidState***: if a virtual machine is not powered off or suspended.  ***ConcurrentAccess***: if another client modifies the folder contents before this operation completes.  ***NotSupported***: if the *Folder.childType* property of the folder is not set to \&quot;VirtualMachine\&quot;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

