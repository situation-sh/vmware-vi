# vmware_vi.DistributedVirtualSwitchApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributed_virtual_switch_add_dv_portgroup_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_add_dv_portgroup_task) | **POST** /DistributedVirtualSwitch/{moId}/AddDVPortgroup_Task | Creates one or more *DistributedVirtualPortgroup*s and adds them to the distributed virtual switch. 
[**distributed_virtual_switch_add_network_resource_pool**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_add_network_resource_pool) | **POST** /DistributedVirtualSwitch/{moId}/AddNetworkResourcePool | Add a network resource pool. 
[**distributed_virtual_switch_create_dv_portgroup_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_create_dv_portgroup_task) | **POST** /DistributedVirtualSwitch/{moId}/CreateDVPortgroup_Task | Creates a single *DistributedVirtualPortgroup* and adds it to the distributed virtual switch. 
[**distributed_virtual_switch_destroy_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_destroy_task) | **POST** /DistributedVirtualSwitch/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task) | **POST** /DistributedVirtualSwitch/{moId}/DvsReconfigureVmVnicNetworkResourcePool_Task | reconfigure the Virtual NIC network resource pool configuration. 
[**distributed_virtual_switch_dvs_rollback_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_dvs_rollback_task) | **POST** /DistributedVirtualSwitch/{moId}/DVSRollback_Task | This method determines if the distributed virtual switch configuration has changed. 
[**distributed_virtual_switch_enable_network_resource_management**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_enable_network_resource_management) | **POST** /DistributedVirtualSwitch/{moId}/EnableNetworkResourceManagement | Enable/Disable network I/O control on the vSphere Distributed Switch. 
[**distributed_virtual_switch_fetch_dv_port_keys**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_fetch_dv_port_keys) | **POST** /DistributedVirtualSwitch/{moId}/FetchDVPortKeys | Return the keys of ports that meet the criteria. 
[**distributed_virtual_switch_fetch_dv_ports**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_fetch_dv_ports) | **POST** /DistributedVirtualSwitch/{moId}/FetchDVPorts | Return the ports that meet the criteria. 
[**distributed_virtual_switch_get_alarm_actions_enabled**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_alarm_actions_enabled) | **GET** /DistributedVirtualSwitch/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**distributed_virtual_switch_get_available_field**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_available_field) | **GET** /DistributedVirtualSwitch/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**distributed_virtual_switch_get_capability**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_capability) | **GET** /DistributedVirtualSwitch/{moId}/capability | Capability of the switch. 
[**distributed_virtual_switch_get_config**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_config) | **GET** /DistributedVirtualSwitch/{moId}/config | Switch configuration data. 
[**distributed_virtual_switch_get_config_issue**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_config_issue) | **GET** /DistributedVirtualSwitch/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**distributed_virtual_switch_get_config_status**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_config_status) | **GET** /DistributedVirtualSwitch/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**distributed_virtual_switch_get_custom_value**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_custom_value) | **GET** /DistributedVirtualSwitch/{moId}/customValue | Custom field values. 
[**distributed_virtual_switch_get_declared_alarm_state**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_declared_alarm_state) | **GET** /DistributedVirtualSwitch/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**distributed_virtual_switch_get_disabled_method**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_disabled_method) | **GET** /DistributedVirtualSwitch/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**distributed_virtual_switch_get_effective_role**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_effective_role) | **GET** /DistributedVirtualSwitch/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**distributed_virtual_switch_get_name**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_name) | **GET** /DistributedVirtualSwitch/{moId}/name | Name of this entity, unique relative to its parent. 
[**distributed_virtual_switch_get_network_resource_pool**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_network_resource_pool) | **GET** /DistributedVirtualSwitch/{moId}/networkResourcePool | Network resource pool information for the switch. 
[**distributed_virtual_switch_get_overall_status**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_overall_status) | **GET** /DistributedVirtualSwitch/{moId}/overallStatus | General health of this managed entity. 
[**distributed_virtual_switch_get_parent**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_parent) | **GET** /DistributedVirtualSwitch/{moId}/parent | Parent of this entity. 
[**distributed_virtual_switch_get_permission**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_permission) | **GET** /DistributedVirtualSwitch/{moId}/permission | List of permissions defined for this entity. 
[**distributed_virtual_switch_get_portgroup**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_portgroup) | **GET** /DistributedVirtualSwitch/{moId}/portgroup | Portgroups that are defined on the switch. 
[**distributed_virtual_switch_get_recent_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_recent_task) | **GET** /DistributedVirtualSwitch/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**distributed_virtual_switch_get_runtime**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_runtime) | **GET** /DistributedVirtualSwitch/{moId}/runtime | Runtime information of the distributed virtual switch. 
[**distributed_virtual_switch_get_summary**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_summary) | **GET** /DistributedVirtualSwitch/{moId}/summary | Summary of the switch. 
[**distributed_virtual_switch_get_tag**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_tag) | **GET** /DistributedVirtualSwitch/{moId}/tag | The set of tags associated with this managed entity. 
[**distributed_virtual_switch_get_triggered_alarm_state**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_triggered_alarm_state) | **GET** /DistributedVirtualSwitch/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**distributed_virtual_switch_get_uuid**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_uuid) | **GET** /DistributedVirtualSwitch/{moId}/uuid | Generated UUID of the switch. 
[**distributed_virtual_switch_get_value**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_get_value) | **GET** /DistributedVirtualSwitch/{moId}/value | List of custom field values. 
[**distributed_virtual_switch_lookup_dv_port_group**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_lookup_dv_port_group) | **POST** /DistributedVirtualSwitch/{moId}/LookupDvPortGroup | Returns the portgroup identified by the key within this VDS. 
[**distributed_virtual_switch_merge_dvs_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_merge_dvs_task) | **POST** /DistributedVirtualSwitch/{moId}/MergeDvs_Task | Merge an existing DistributedVirtualSwitch (source) to this switch (destination). 
[**distributed_virtual_switch_move_dv_port_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_move_dv_port_task) | **POST** /DistributedVirtualSwitch/{moId}/MoveDVPort_Task | Move the ports out of their current portgroup into the specified portgroup. 
[**distributed_virtual_switch_perform_dvs_product_spec_operation_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_perform_dvs_product_spec_operation_task) | **POST** /DistributedVirtualSwitch/{moId}/PerformDvsProductSpecOperation_Task | This method updates the *DistributedVirtualSwitch* product specifications. 
[**distributed_virtual_switch_query_used_vlan_id_in_dvs**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_query_used_vlan_id_in_dvs) | **POST** /DistributedVirtualSwitch/{moId}/QueryUsedVlanIdInDvs | Return the used VLAN ID (PVLAN excluded) in the switch. 
[**distributed_virtual_switch_reconfigure_dv_port_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_reconfigure_dv_port_task) | **POST** /DistributedVirtualSwitch/{moId}/ReconfigureDVPort_Task | Reconfigure individual ports. 
[**distributed_virtual_switch_reconfigure_dvs_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_reconfigure_dvs_task) | **POST** /DistributedVirtualSwitch/{moId}/ReconfigureDvs_Task | Reconfigures a distributed virtual switch. 
[**distributed_virtual_switch_rectify_dvs_host_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_rectify_dvs_host_task) | **POST** /DistributedVirtualSwitch/{moId}/RectifyDvsHost_Task | Update the switch configuration on the host to bring them in sync with the current configuration in vCenter Server. 
[**distributed_virtual_switch_refresh_dv_port_state**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_refresh_dv_port_state) | **POST** /DistributedVirtualSwitch/{moId}/RefreshDVPortState | Refresh port states. 
[**distributed_virtual_switch_reload**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_reload) | **POST** /DistributedVirtualSwitch/{moId}/Reload | Reload the entity state. 
[**distributed_virtual_switch_remove_network_resource_pool**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_remove_network_resource_pool) | **POST** /DistributedVirtualSwitch/{moId}/RemoveNetworkResourcePool | Remove a network resource pool. 
[**distributed_virtual_switch_rename_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_rename_task) | **POST** /DistributedVirtualSwitch/{moId}/Rename_Task | Renames this managed entity. 
[**distributed_virtual_switch_set_custom_value**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_set_custom_value) | **POST** /DistributedVirtualSwitch/{moId}/setCustomValue | Assigns a value to a custom field. 
[**distributed_virtual_switch_update_dvs_capability**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_update_dvs_capability) | **POST** /DistributedVirtualSwitch/{moId}/UpdateDvsCapability | Set the capability of the switch. 
[**distributed_virtual_switch_update_dvs_health_check_config_task**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_update_dvs_health_check_config_task) | **POST** /DistributedVirtualSwitch/{moId}/UpdateDVSHealthCheckConfig_Task | Update health check configuration. 
[**distributed_virtual_switch_update_network_resource_pool**](DistributedVirtualSwitchApi.md#distributed_virtual_switch_update_network_resource_pool) | **POST** /DistributedVirtualSwitch/{moId}/UpdateNetworkResourcePool | Update the network resource pool configuration. 


# **distributed_virtual_switch_add_dv_portgroup_task**
> ManagedObjectReference distributed_virtual_switch_add_dv_portgroup_task(mo_id, add_dv_portgroup_request_type)

Creates one or more *DistributedVirtualPortgroup*s and adds them to the distributed virtual switch. 

Creates one or more *DistributedVirtualPortgroup*s and adds them to the distributed virtual switch.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVPortgroup.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_dv_portgroup_request_type import AddDVPortgroupRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_dv_portgroup_request_type = vmware_vi.AddDVPortgroupRequestType() # AddDVPortgroupRequestType | 

    try:
        # Creates one or more *DistributedVirtualPortgroup*s and adds them to the distributed virtual switch. 
        api_response = api_instance.distributed_virtual_switch_add_dv_portgroup_task(mo_id, add_dv_portgroup_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_add_dv_portgroup_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_add_dv_portgroup_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_dv_portgroup_request_type** | [**AddDVPortgroupRequestType**](AddDVPortgroupRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation. The method does not return a value in the *Task*.*Task.info*.*TaskInfo.result* property. Use the *DistributedVirtualSwitch.portgroup* property to obtain managed object references to the new portgroups.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: If called directly on a host.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_add_network_resource_pool**
> distributed_virtual_switch_add_network_resource_pool(mo_id, add_network_resource_pool_request_type)

Add a network resource pool. 

Deprecated as of vSphere API 6.0 Use *DistributedVirtualSwitch.DvsReconfigureVmVnicNetworkResourcePool_Task* instead to add a Virtual NIC network resource pool.  Add a network resource pool.  ***Since:*** vSphere API 5.0  ***Required privileges:*** DVSwitch.ResourceManagement 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_network_resource_pool_request_type import AddNetworkResourcePoolRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_network_resource_pool_request_type = vmware_vi.AddNetworkResourcePoolRequestType() # AddNetworkResourcePoolRequestType | 

    try:
        # Add a network resource pool. 
        api_instance.distributed_virtual_switch_add_network_resource_pool(mo_id, add_network_resource_pool_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_add_network_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_network_resource_pool_request_type** | [**AddNetworkResourcePoolRequestType**](AddNetworkResourcePoolRequestType.md)|  | 

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
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  ***NotSupported***: if network I/O control is not supported on the vSphere Distributed Switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_create_dv_portgroup_task**
> ManagedObjectReference distributed_virtual_switch_create_dv_portgroup_task(mo_id, create_dv_portgroup_request_type)

Creates a single *DistributedVirtualPortgroup* and adds it to the distributed virtual switch. 

Creates a single *DistributedVirtualPortgroup* and adds it to the distributed virtual switch.  ***Since:*** vSphere API 5.1  ***Required privileges:*** DVPortgroup.Create 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_dv_portgroup_request_type import CreateDVPortgroupRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_dv_portgroup_request_type = vmware_vi.CreateDVPortgroupRequestType() # CreateDVPortgroupRequestType | 

    try:
        # Creates a single *DistributedVirtualPortgroup* and adds it to the distributed virtual switch. 
        api_response = api_instance.distributed_virtual_switch_create_dv_portgroup_task(mo_id, create_dv_portgroup_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_create_dv_portgroup_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_create_dv_portgroup_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_dv_portgroup_request_type** | [**CreateDVPortgroupRequestType**](CreateDVPortgroupRequestType.md)|  | 

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
**200** | Returns a *Task* object. The *Task*.*Task.info*.*TaskInfo.result* property contains a managed object reference to the new portgroup. The *DistributedVirtualSwitch.portgroup* property also contains the reference.  Refers instance of *Task*.  |  -  |
**500** | ***DuplicateName***: if a portgroup with the same name already exists  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***InvalidName***: if name of the portgroup is invalid  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_destroy_task**
> ManagedObjectReference distributed_virtual_switch_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** DVSwitch.Delete 

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.distributed_virtual_switch_destroy_task(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_destroy_task: %s\n" % e)
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

# **distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task**
> ManagedObjectReference distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task(mo_id, dvs_reconfigure_vm_vnic_network_resource_pool_request_type)

reconfigure the Virtual NIC network resource pool configuration. 

reconfigure the Virtual NIC network resource pool configuration.  ***Since:*** vSphere API 6.0  ***Required privileges:*** DVSwitch.ResourceManagement 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_reconfigure_vm_vnic_network_resource_pool_request_type import DvsReconfigureVmVnicNetworkResourcePoolRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dvs_reconfigure_vm_vnic_network_resource_pool_request_type = vmware_vi.DvsReconfigureVmVnicNetworkResourcePoolRequestType() # DvsReconfigureVmVnicNetworkResourcePoolRequestType | 

    try:
        # reconfigure the Virtual NIC network resource pool configuration. 
        api_response = api_instance.distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task(mo_id, dvs_reconfigure_vm_vnic_network_resource_pool_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_dvs_reconfigure_vm_vnic_network_resource_pool_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dvs_reconfigure_vm_vnic_network_resource_pool_request_type** | [**DvsReconfigureVmVnicNetworkResourcePoolRequestType**](DvsReconfigureVmVnicNetworkResourcePoolRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***DvsFault***: if operation fails on any host or if there are other reconfigure failures.  ***NotFound***: if the resource pool does not exist on the dvs.  ***DuplicateName***: if a virtual NIC network resource pool with the same name already exists.  ***ConcurrentAccess***: if a Virtual NIC network resource pool is modified by two or more clients at the same time.  ***ResourceInUse***: If Virtual NIC network resource pool being removed is associated with a network entity  ***NotSupported***: if network I/O control is not supported on the vSphere Distributed Switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  ***ConflictingConfiguration***: if the any property being set is in conflict.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_dvs_rollback_task**
> ManagedObjectReference distributed_virtual_switch_dvs_rollback_task(mo_id, dvs_rollback_request_type)

This method determines if the distributed virtual switch configuration has changed. 

This method determines if the distributed virtual switch configuration has changed.  If it has changed, the method returns a *VMwareDVSConfigSpec*. Use the *DistributedVirtualSwitch.ReconfigureDvs_Task* method to apply the rollback configuration to the switch. You can use the rollback method only on a *VmwareDistributedVirtualSwitch*. - If you specify the <code>entityBackup</code> parameter, the returned   configuration specification represents the exported switch configuration.   If the <code>entityBackup</code> matches the current switch   configuration, the method does not return a configuration specification. - If <code>entityBackup</code> is not specified, the returned configuration   specification represents a previous state of the switch, if available.   When you use a VMware distributed virtual switch, each time you reconfigure   the switch, the Server saves the switch configuration before applying the updates.   If the vCenter Server is restarted, the saved configuration is not preserved   and the method does not return a configuration specification.    To use the rollback method, you must have the DVSwitch.Read privilege.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_rollback_request_type import DVSRollbackRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dvs_rollback_request_type = vmware_vi.DVSRollbackRequestType() # DVSRollbackRequestType | 

    try:
        # This method determines if the distributed virtual switch configuration has changed. 
        api_response = api_instance.distributed_virtual_switch_dvs_rollback_task(mo_id, dvs_rollback_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_dvs_rollback_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_dvs_rollback_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dvs_rollback_request_type** | [**DVSRollbackRequestType**](DVSRollbackRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation. If the distributed virtual switch configuration has changed, the *Task*.*Task.info*.*TaskInfo.result* property contains the *DVSConfigSpec* object.  Refers instance of *Task*.  |  -  |
**500** | ***RollbackFailure***: if there is no configuration specified in entityBackup and the previous configuration does not exist either.  ***DvsFault***: if operation fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_enable_network_resource_management**
> distributed_virtual_switch_enable_network_resource_management(mo_id, enable_network_resource_management_request_type)

Enable/Disable network I/O control on the vSphere Distributed Switch. 

Enable/Disable network I/O control on the vSphere Distributed Switch.  ***Since:*** vSphere API 4.1  ***Required privileges:*** DVSwitch.ResourceManagement 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_network_resource_management_request_type import EnableNetworkResourceManagementRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_network_resource_management_request_type = vmware_vi.EnableNetworkResourceManagementRequestType() # EnableNetworkResourceManagementRequestType | 

    try:
        # Enable/Disable network I/O control on the vSphere Distributed Switch. 
        api_instance.distributed_virtual_switch_enable_network_resource_management(mo_id, enable_network_resource_management_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_enable_network_resource_management: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_network_resource_management_request_type** | [**EnableNetworkResourceManagementRequestType**](EnableNetworkResourceManagementRequestType.md)|  | 

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
**500** | ***DvsFault***: if the enabling/disabling fails.  ***NotSupported***: if network I/O control is not supported on the vSphere Distributed Switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_fetch_dv_port_keys**
> List[str] distributed_virtual_switch_fetch_dv_port_keys(mo_id, fetch_dv_port_keys_request_type)

Return the keys of ports that meet the criteria. 

Return the keys of ports that meet the criteria.  On an ESXi host, the property shows only the connected ports currently on the host.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.fetch_dv_port_keys_request_type import FetchDVPortKeysRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    fetch_dv_port_keys_request_type = vmware_vi.FetchDVPortKeysRequestType() # FetchDVPortKeysRequestType | 

    try:
        # Return the keys of ports that meet the criteria. 
        api_response = api_instance.distributed_virtual_switch_fetch_dv_port_keys(mo_id, fetch_dv_port_keys_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_fetch_dv_port_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_fetch_dv_port_keys: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **fetch_dv_port_keys_request_type** | [**FetchDVPortKeysRequestType**](FetchDVPortKeysRequestType.md)|  | 

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
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_fetch_dv_ports**
> List[DistributedVirtualPort] distributed_virtual_switch_fetch_dv_ports(mo_id, fetch_dv_ports_request_type)

Return the ports that meet the criteria. 

Return the ports that meet the criteria.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.distributed_virtual_port import DistributedVirtualPort
from vmware_vi.models.fetch_dv_ports_request_type import FetchDVPortsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    fetch_dv_ports_request_type = vmware_vi.FetchDVPortsRequestType() # FetchDVPortsRequestType | 

    try:
        # Return the ports that meet the criteria. 
        api_response = api_instance.distributed_virtual_switch_fetch_dv_ports(mo_id, fetch_dv_ports_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_fetch_dv_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_fetch_dv_ports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **fetch_dv_ports_request_type** | [**FetchDVPortsRequestType**](FetchDVPortsRequestType.md)|  | 

### Return type

[**List[DistributedVirtualPort]**](DistributedVirtualPort.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_get_alarm_actions_enabled**
> bool distributed_virtual_switch_get_alarm_actions_enabled(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.distributed_virtual_switch_get_alarm_actions_enabled(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_alarm_actions_enabled: %s\n" % e)
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

# **distributed_virtual_switch_get_available_field**
> List[CustomFieldDef] distributed_virtual_switch_get_available_field(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.distributed_virtual_switch_get_available_field(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_available_field: %s\n" % e)
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

# **distributed_virtual_switch_get_capability**
> DVSCapability distributed_virtual_switch_get_capability(mo_id)

Capability of the switch. 

Capability of the switch.  Capabilities are indicated at the port, portgroup and switch levels, and for version-specific features. When you retrieve this property from an ESXi host, *DistributedVirtualSwitch.capability*.*DVSCapability.dvsOperationSupported* should always be set to false.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_capability import DVSCapability
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Capability of the switch. 
        api_response = api_instance.distributed_virtual_switch_get_capability(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**DVSCapability**](DVSCapability.md)

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

# **distributed_virtual_switch_get_config**
> DVSConfigInfo distributed_virtual_switch_get_config(mo_id)

Switch configuration data. 

Switch configuration data.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_config_info import DVSConfigInfo
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Switch configuration data. 
        api_response = api_instance.distributed_virtual_switch_get_config(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**DVSConfigInfo**](DVSConfigInfo.md)

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

# **distributed_virtual_switch_get_config_issue**
> List[Event] distributed_virtual_switch_get_config_issue(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.distributed_virtual_switch_get_config_issue(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_config_issue: %s\n" % e)
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

# **distributed_virtual_switch_get_config_status**
> ManagedEntityStatusEnum distributed_virtual_switch_get_config_status(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.distributed_virtual_switch_get_config_status(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_config_status: %s\n" % e)
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

# **distributed_virtual_switch_get_custom_value**
> List[CustomFieldValue] distributed_virtual_switch_get_custom_value(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.distributed_virtual_switch_get_custom_value(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_custom_value: %s\n" % e)
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

# **distributed_virtual_switch_get_declared_alarm_state**
> List[AlarmState] distributed_virtual_switch_get_declared_alarm_state(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.distributed_virtual_switch_get_declared_alarm_state(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_declared_alarm_state: %s\n" % e)
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

# **distributed_virtual_switch_get_disabled_method**
> List[str] distributed_virtual_switch_get_disabled_method(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.distributed_virtual_switch_get_disabled_method(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_disabled_method: %s\n" % e)
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

# **distributed_virtual_switch_get_effective_role**
> List[int] distributed_virtual_switch_get_effective_role(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.distributed_virtual_switch_get_effective_role(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_effective_role: %s\n" % e)
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

# **distributed_virtual_switch_get_name**
> str distributed_virtual_switch_get_name(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.distributed_virtual_switch_get_name(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_name: %s\n" % e)
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

# **distributed_virtual_switch_get_network_resource_pool**
> List[DVSNetworkResourcePool] distributed_virtual_switch_get_network_resource_pool(mo_id)

Network resource pool information for the switch. 

Deprecated as of vSphere API 6.0 Use *DVSConfigInfo.vmVnicNetworkResourcePool* to get the Virtual NIC resource pool information. Use *DVSConfigInfo.infrastructureTrafficResourceConfig* to get the host infrastructure resource information.  Network resource pool information for the switch.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_network_resource_pool import DVSNetworkResourcePool
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Network resource pool information for the switch. 
        api_response = api_instance.distributed_virtual_switch_get_network_resource_pool(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_network_resource_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_network_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[DVSNetworkResourcePool]**](DVSNetworkResourcePool.md)

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

# **distributed_virtual_switch_get_overall_status**
> ManagedEntityStatusEnum distributed_virtual_switch_get_overall_status(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.distributed_virtual_switch_get_overall_status(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_overall_status: %s\n" % e)
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

# **distributed_virtual_switch_get_parent**
> ManagedObjectReference distributed_virtual_switch_get_parent(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.distributed_virtual_switch_get_parent(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_parent: %s\n" % e)
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

# **distributed_virtual_switch_get_permission**
> List[Permission] distributed_virtual_switch_get_permission(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.distributed_virtual_switch_get_permission(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_permission: %s\n" % e)
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

# **distributed_virtual_switch_get_portgroup**
> List[ManagedObjectReference] distributed_virtual_switch_get_portgroup(mo_id)

Portgroups that are defined on the switch. 

Portgroups that are defined on the switch.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Portgroups that are defined on the switch. 
        api_response = api_instance.distributed_virtual_switch_get_portgroup(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_portgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_portgroup: %s\n" % e)
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
**200** | Refers instances of *DistributedVirtualPortgroup*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_get_recent_task**
> List[ManagedObjectReference] distributed_virtual_switch_get_recent_task(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.distributed_virtual_switch_get_recent_task(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_recent_task: %s\n" % e)
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

# **distributed_virtual_switch_get_runtime**
> DVSRuntimeInfo distributed_virtual_switch_get_runtime(mo_id)

Runtime information of the distributed virtual switch. 

Runtime information of the distributed virtual switch.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_runtime_info import DVSRuntimeInfo
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Runtime information of the distributed virtual switch. 
        api_response = api_instance.distributed_virtual_switch_get_runtime(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_runtime: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**DVSRuntimeInfo**](DVSRuntimeInfo.md)

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

# **distributed_virtual_switch_get_summary**
> DVSSummary distributed_virtual_switch_get_summary(mo_id)

Summary of the switch. 

Summary of the switch.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dvs_summary import DVSSummary
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Summary of the switch. 
        api_response = api_instance.distributed_virtual_switch_get_summary(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**DVSSummary**](DVSSummary.md)

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

# **distributed_virtual_switch_get_tag**
> List[Tag] distributed_virtual_switch_get_tag(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.distributed_virtual_switch_get_tag(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_tag: %s\n" % e)
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

# **distributed_virtual_switch_get_triggered_alarm_state**
> List[AlarmState] distributed_virtual_switch_get_triggered_alarm_state(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.distributed_virtual_switch_get_triggered_alarm_state(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_triggered_alarm_state: %s\n" % e)
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

# **distributed_virtual_switch_get_uuid**
> str distributed_virtual_switch_get_uuid(mo_id)

Generated UUID of the switch. 

Generated UUID of the switch.  Unique across vCenter Server inventory and instances.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Generated UUID of the switch. 
        api_response = api_instance.distributed_virtual_switch_get_uuid(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_uuid: %s\n" % e)
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

# **distributed_virtual_switch_get_value**
> List[CustomFieldValue] distributed_virtual_switch_get_value(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.distributed_virtual_switch_get_value(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_get_value: %s\n" % e)
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

# **distributed_virtual_switch_lookup_dv_port_group**
> ManagedObjectReference distributed_virtual_switch_lookup_dv_port_group(mo_id, lookup_dv_port_group_request_type)

Returns the portgroup identified by the key within this VDS. 

Returns the portgroup identified by the key within this VDS.  ***Since:*** vSphere API 5.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.lookup_dv_port_group_request_type import LookupDvPortGroupRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    lookup_dv_port_group_request_type = vmware_vi.LookupDvPortGroupRequestType() # LookupDvPortGroupRequestType | 

    try:
        # Returns the portgroup identified by the key within this VDS. 
        api_response = api_instance.distributed_virtual_switch_lookup_dv_port_group(mo_id, lookup_dv_port_group_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_lookup_dv_port_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_lookup_dv_port_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **lookup_dv_port_group_request_type** | [**LookupDvPortGroupRequestType**](LookupDvPortGroupRequestType.md)|  | 

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
**200** | Refers instance of *DistributedVirtualPortgroup*.  |  -  |
**500** | ***NotFound***: If the portgroup for the specified key is not found.  ***NotSupported***: If the operation is not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_merge_dvs_task**
> ManagedObjectReference distributed_virtual_switch_merge_dvs_task(mo_id, merge_dvs_request_type)

Merge an existing DistributedVirtualSwitch (source) to this switch (destination). 

Deprecated as of vSphere API 5.5.  Merge an existing DistributedVirtualSwitch (source) to this switch (destination).  The host members and the connected entity of the source switch will be transferred to the destination switch. This operation disconnects the entities from the source switch, tears down its host proxy switches, creates new proxies for the destination switch, and reconnects the entities to the destination switch.  In summary, this operation does the following: - Adds the   <code>config</code>.*DVSConfigInfo.maxPorts*   of the source switch to the <code>maxPorts</code> of the   destination switch. - The host members of the source switch leave the source switch   and join the destination switch with the same Physical NIC and   VirtualSwitch (if applicable). A set of new uplink ports,   compliant with the   *DVSConfigSpec.uplinkPortPolicy*,   is created as the hosts join the destination switch. - The portgroups on the source switch are copied over to destination   switch, by calculating the effective default port config and   creating a portgroup of the same name in the destination switch. If   the name already exists, the copied portgroup uses names following a   \"Copy of switch-portgroup-name\" scheme to avoid conflict. The same   number of ports are created inside each copied portgroup. - The standalone distributed virtual ports are not copied,   unless there is a virtual   machine or host virtual NIC connecting to it. In that case, the   operation calculates the effective port config and creates a port   in the destination switch with the same name. Name conflict is   resolved using numbers like \"original-port-name(1)\". The uplink ports   are not copied over. - The virtual machine and host virtual NICs are disconnected from the source   switch and reconnected with the destination switch, to the   copied standalone port or portgroup. - If you are using a *VmwareDistributedVirtualSwitch* -   Unless the PVLAN map contains exactly the same entries between   the source and destination VMware distributed virtual switches,   the method raises a fault if   *VmwareDistributedVirtualSwitchPvlanSpec.pvlanId*   is set in any port, portgroup, or switch that will be copied.    ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.Modify 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.merge_dvs_request_type import MergeDvsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    merge_dvs_request_type = vmware_vi.MergeDvsRequestType() # MergeDvsRequestType | 

    try:
        # Merge an existing DistributedVirtualSwitch (source) to this switch (destination). 
        api_response = api_instance.distributed_virtual_switch_merge_dvs_task(mo_id, merge_dvs_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_merge_dvs_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_merge_dvs_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **merge_dvs_request_type** | [**MergeDvsRequestType**](MergeDvsRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: If called directly on a host.  ***ResourceInUse***: If failed to delete the source switch  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_move_dv_port_task**
> ManagedObjectReference distributed_virtual_switch_move_dv_port_task(mo_id, move_dv_port_request_type)

Move the ports out of their current portgroup into the specified portgroup. 

Deprecated as of vSphere API 6.0.  Move the ports out of their current portgroup into the specified portgroup.  If the moving of any of the ports results in a violation of the portgroup policy, or type of the source or destination portgroup, the operation raises a fault. A conflict port cannot be moved.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.Modify 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_dv_port_request_type import MoveDVPortRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_dv_port_request_type = vmware_vi.MoveDVPortRequestType() # MoveDVPortRequestType | 

    try:
        # Move the ports out of their current portgroup into the specified portgroup. 
        api_response = api_instance.distributed_virtual_switch_move_dv_port_task(mo_id, move_dv_port_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_move_dv_port_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_move_dv_port_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_dv_port_request_type** | [**MoveDVPortRequestType**](MoveDVPortRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: If called directly on a host.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_perform_dvs_product_spec_operation_task**
> ManagedObjectReference distributed_virtual_switch_perform_dvs_product_spec_operation_task(mo_id, perform_dvs_product_spec_operation_request_type)

This method updates the *DistributedVirtualSwitch* product specifications. 

This method updates the *DistributedVirtualSwitch* product specifications.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.Modify 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.perform_dvs_product_spec_operation_request_type import PerformDvsProductSpecOperationRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    perform_dvs_product_spec_operation_request_type = vmware_vi.PerformDvsProductSpecOperationRequestType() # PerformDvsProductSpecOperationRequestType | 

    try:
        # This method updates the *DistributedVirtualSwitch* product specifications. 
        api_response = api_instance.distributed_virtual_switch_perform_dvs_product_spec_operation_task(mo_id, perform_dvs_product_spec_operation_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_perform_dvs_product_spec_operation_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_perform_dvs_product_spec_operation_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **perform_dvs_product_spec_operation_request_type** | [**PerformDvsProductSpecOperationRequestType**](PerformDvsProductSpecOperationRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: If called directly on a host.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_query_used_vlan_id_in_dvs**
> List[int] distributed_virtual_switch_query_used_vlan_id_in_dvs(mo_id)

Return the used VLAN ID (PVLAN excluded) in the switch. 

Return the used VLAN ID (PVLAN excluded) in the switch.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Return the used VLAN ID (PVLAN excluded) in the switch. 
        api_response = api_instance.distributed_virtual_switch_query_used_vlan_id_in_dvs(mo_id)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_query_used_vlan_id_in_dvs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_query_used_vlan_id_in_dvs: %s\n" % e)
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

# **distributed_virtual_switch_reconfigure_dv_port_task**
> ManagedObjectReference distributed_virtual_switch_reconfigure_dv_port_task(mo_id, reconfigure_dv_port_request_type)

Reconfigure individual ports. 

Reconfigure individual ports.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.PortConfig 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfigure_dv_port_request_type import ReconfigureDVPortRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_dv_port_request_type = vmware_vi.ReconfigureDVPortRequestType() # ReconfigureDVPortRequestType | 

    try:
        # Reconfigure individual ports. 
        api_response = api_instance.distributed_virtual_switch_reconfigure_dv_port_task(mo_id, reconfigure_dv_port_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_reconfigure_dv_port_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_reconfigure_dv_port_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_dv_port_request_type** | [**ReconfigureDVPortRequestType**](ReconfigureDVPortRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: If called directly on a host or if the switch implementation doesn&#39;t support this API or if the spec includes settings for any vSphere Distributed Switch feature that is not supported on this switch.  ***InvalidArgument***: If the array have different elements for the same port.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_reconfigure_dvs_task**
> ManagedObjectReference distributed_virtual_switch_reconfigure_dvs_task(mo_id, reconfigure_dvs_request_type)

Reconfigures a distributed virtual switch. 

Reconfigures a distributed virtual switch.  You can use this method to set switch properties or to reset the switch to a previous state.  **Reconfiguring a Standard Distributed Virtual Switch**  To reconfigure a *DistributedVirtualSwitch*, use a *DVSConfigSpec* to set the switch properties.  **Reconfiguring a VMware Distributed Virtual Switch**  If you use a *VmwareDistributedVirtualSwitch*, you can perform the following switch reconfiguration: - Use a *VMwareDVSConfigSpec*   to set the switch properties. - Use the *VMwareDVSConfigSpec*   returned by *DistributedVirtualSwitch.DVSRollback_Task*   to reset the switch to a previous state.    Reconfiguring the switch may require any of the following privileges, depending on what is being changed: - DVSwitch.PolicyOp if *DVSConfigSpec.policy*   is set. - DVSwitch.PortSetting if *DVSConfigSpec.defaultPortConfig*   is set. - DVSwitch.HostOp if *DVSConfigSpec.policy*   is set. The   user will also need the Host.Config.Network   privilege on the host. - DVSwitch.Vspan if *VMwareDVSConfigSpec.vspanConfigSpec*   is set. - DVSwitch.Modify for anything else.    ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfigure_dvs_request_type import ReconfigureDvsRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_dvs_request_type = vmware_vi.ReconfigureDvsRequestType() # ReconfigureDvsRequestType | 

    try:
        # Reconfigures a distributed virtual switch. 
        api_response = api_instance.distributed_virtual_switch_reconfigure_dvs_task(mo_id, reconfigure_dvs_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_reconfigure_dvs_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_reconfigure_dvs_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_dvs_request_type** | [**ReconfigureDvsRequestType**](ReconfigureDvsRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if called directly on a host or if the spec includes settings for any vNetwork Distributed Switch feature that is not supported on this switch.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *DVSConfigInfo.extensionKey*.  ***ResourceNotAvailable***: If there is no port available in the portgroup  ***VspanPortConflict***: if dvPort is used as both the transmitted source and destination ports in Distributed Port Mirroring sessions.  ***VspanPromiscuousPortNotSupported***: if a promiscuous port is used as transmitted source or destination in the Distributed Port Mirroring sessions.  ***VspanSameSessionPortConflict***: if a dvPort is used as both the source and destination in the same Distributed Port Mirroring session.  ***VspanDestPortConflict***: if a dvPort is used as desination ports in multiple Distributed Port Mirroring sessions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_rectify_dvs_host_task**
> ManagedObjectReference distributed_virtual_switch_rectify_dvs_host_task(mo_id, rectify_dvs_host_request_type)

Update the switch configuration on the host to bring them in sync with the current configuration in vCenter Server. 

Deprecated as of vSphere API 5.0. Use *DistributedVirtualSwitchManager*.*DistributedVirtualSwitchManager.RectifyDvsOnHost_Task* instead.  Update the switch configuration on the host to bring them in sync with the current configuration in vCenter Server.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.rectify_dvs_host_request_type import RectifyDvsHostRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rectify_dvs_host_request_type = vmware_vi.RectifyDvsHostRequestType() # RectifyDvsHostRequestType | 

    try:
        # Update the switch configuration on the host to bring them in sync with the current configuration in vCenter Server. 
        api_response = api_instance.distributed_virtual_switch_rectify_dvs_host_task(mo_id, rectify_dvs_host_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_rectify_dvs_host_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_rectify_dvs_host_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rectify_dvs_host_request_type** | [**RectifyDvsHostRequestType**](RectifyDvsHostRequestType.md)|  | 

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
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_refresh_dv_port_state**
> distributed_virtual_switch_refresh_dv_port_state(mo_id, refresh_dv_port_state_request_type)

Refresh port states. 

Refresh port states.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.refresh_dv_port_state_request_type import RefreshDVPortStateRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    refresh_dv_port_state_request_type = vmware_vi.RefreshDVPortStateRequestType() # RefreshDVPortStateRequestType | 

    try:
        # Refresh port states. 
        api_instance.distributed_virtual_switch_refresh_dv_port_state(mo_id, refresh_dv_port_state_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_refresh_dv_port_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **refresh_dv_port_state_request_type** | [**RefreshDVPortStateRequestType**](RefreshDVPortStateRequestType.md)|  | 

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
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_reload**
> distributed_virtual_switch_reload(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.distributed_virtual_switch_reload(mo_id)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_reload: %s\n" % e)
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

# **distributed_virtual_switch_remove_network_resource_pool**
> distributed_virtual_switch_remove_network_resource_pool(mo_id, remove_network_resource_pool_request_type)

Remove a network resource pool. 

Deprecated as of vSphere API 6.0 Use *DistributedVirtualSwitch.DvsReconfigureVmVnicNetworkResourcePool_Task* instead to remove a Virtual NIC network resource pool.  Remove a network resource pool.  ***Since:*** vSphere API 5.0  ***Required privileges:*** DVSwitch.ResourceManagement 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_network_resource_pool_request_type import RemoveNetworkResourcePoolRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_network_resource_pool_request_type = vmware_vi.RemoveNetworkResourcePoolRequestType() # RemoveNetworkResourcePoolRequestType | 

    try:
        # Remove a network resource pool. 
        api_instance.distributed_virtual_switch_remove_network_resource_pool(mo_id, remove_network_resource_pool_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_remove_network_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_network_resource_pool_request_type** | [**RemoveNetworkResourcePoolRequestType**](RemoveNetworkResourcePoolRequestType.md)|  | 

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
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  ***NotFound***: if the resource pool does not exist on the dvs.  ***InvalidName***: if the name of the resource pool is invalid.  ***ResourceInUse***: If network resource pool is associated with a network entity  ***NotSupported***: if network I/O control is not supported on the vSphere Distributed Switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_rename_task**
> ManagedObjectReference distributed_virtual_switch_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** DVSwitch.Modify 

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.distributed_virtual_switch_rename_task(mo_id, rename_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_rename_task: %s\n" % e)
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

# **distributed_virtual_switch_set_custom_value**
> distributed_virtual_switch_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.distributed_virtual_switch_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_set_custom_value: %s\n" % e)
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

# **distributed_virtual_switch_update_dvs_capability**
> distributed_virtual_switch_update_dvs_capability(mo_id, update_dvs_capability_request_type)

Set the capability of the switch. 

Set the capability of the switch.  ***Since:*** vSphere API 4.0  ***Required privileges:*** DVSwitch.Modify 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_dvs_capability_request_type import UpdateDvsCapabilityRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_dvs_capability_request_type = vmware_vi.UpdateDvsCapabilityRequestType() # UpdateDvsCapabilityRequestType | 

    try:
        # Set the capability of the switch. 
        api_instance.distributed_virtual_switch_update_dvs_capability(mo_id, update_dvs_capability_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_update_dvs_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_dvs_capability_request_type** | [**UpdateDvsCapabilityRequestType**](UpdateDvsCapabilityRequestType.md)|  | 

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
**500** | ***NotSupported***: If called directly on a host or if the switch implementation doesn&#39;t support this API.  ***DvsFault***: if operation fails on any host or if there are other update failures.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_update_dvs_health_check_config_task**
> ManagedObjectReference distributed_virtual_switch_update_dvs_health_check_config_task(mo_id, update_dvs_health_check_config_request_type)

Update health check configuration. 

Update health check configuration.  ***Since:*** vSphere API 5.1  ***Required privileges:*** DVSwitch.Modify 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_dvs_health_check_config_request_type import UpdateDVSHealthCheckConfigRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_dvs_health_check_config_request_type = vmware_vi.UpdateDVSHealthCheckConfigRequestType() # UpdateDVSHealthCheckConfigRequestType | 

    try:
        # Update health check configuration. 
        api_response = api_instance.distributed_virtual_switch_update_dvs_health_check_config_task(mo_id, update_dvs_health_check_config_request_type)
        print("The response of DistributedVirtualSwitchApi->distributed_virtual_switch_update_dvs_health_check_config_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_update_dvs_health_check_config_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_dvs_health_check_config_request_type** | [**UpdateDVSHealthCheckConfigRequestType**](UpdateDVSHealthCheckConfigRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  ***NotSupported***: if health check is not supported on the switch.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_switch_update_network_resource_pool**
> distributed_virtual_switch_update_network_resource_pool(mo_id, update_network_resource_pool_request_type)

Update the network resource pool configuration. 

Deprecated as of vSphere API 6.0 Use *DistributedVirtualSwitch.DvsReconfigureVmVnicNetworkResourcePool_Task* instead to update the Virtual NIC network resource pool.  Update the network resource pool configuration.  ***Since:*** vSphere API 4.1  ***Required privileges:*** DVSwitch.ResourceManagement 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_network_resource_pool_request_type import UpdateNetworkResourcePoolRequestType
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
    api_instance = vmware_vi.DistributedVirtualSwitchApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_network_resource_pool_request_type = vmware_vi.UpdateNetworkResourcePoolRequestType() # UpdateNetworkResourcePoolRequestType | 

    try:
        # Update the network resource pool configuration. 
        api_instance.distributed_virtual_switch_update_network_resource_pool(mo_id, update_network_resource_pool_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualSwitchApi->distributed_virtual_switch_update_network_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_network_resource_pool_request_type** | [**UpdateNetworkResourcePoolRequestType**](UpdateNetworkResourcePoolRequestType.md)|  | 

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
**500** | ***DvsFault***: if operation fails on any host or if there are other update failures.  ***NotFound***: if the resource pool does not exist on the dvs.  ***InvalidName***: if the name of the resource pool is invalid.  ***ConcurrentAccess***: if a network resource pool is modified by two or more clients at the same time.  ***NotSupported***: if network I/O control is not supported on the vSphere Distributed Switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

