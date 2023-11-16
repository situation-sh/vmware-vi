# vmware_vi.DistributedVirtualPortgroupApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributed_virtual_portgroup_destroy_network**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_destroy_network) | **POST** /DistributedVirtualPortgroup/{moId}/DestroyNetwork | Removes a network. 
[**distributed_virtual_portgroup_destroy_task**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_destroy_task) | **POST** /DistributedVirtualPortgroup/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**distributed_virtual_portgroup_dv_portgroup_rollback_task**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_dv_portgroup_rollback_task) | **POST** /DistributedVirtualPortgroup/{moId}/DVPortgroupRollback_Task | This method determines if the portgroup configuration has changed. 
[**distributed_virtual_portgroup_get_alarm_actions_enabled**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_alarm_actions_enabled) | **GET** /DistributedVirtualPortgroup/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**distributed_virtual_portgroup_get_available_field**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_available_field) | **GET** /DistributedVirtualPortgroup/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**distributed_virtual_portgroup_get_config**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_config) | **GET** /DistributedVirtualPortgroup/{moId}/config | Configuration of the portgroup. 
[**distributed_virtual_portgroup_get_config_issue**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_config_issue) | **GET** /DistributedVirtualPortgroup/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**distributed_virtual_portgroup_get_config_status**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_config_status) | **GET** /DistributedVirtualPortgroup/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**distributed_virtual_portgroup_get_custom_value**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_custom_value) | **GET** /DistributedVirtualPortgroup/{moId}/customValue | Custom field values. 
[**distributed_virtual_portgroup_get_declared_alarm_state**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_declared_alarm_state) | **GET** /DistributedVirtualPortgroup/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**distributed_virtual_portgroup_get_disabled_method**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_disabled_method) | **GET** /DistributedVirtualPortgroup/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**distributed_virtual_portgroup_get_effective_role**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_effective_role) | **GET** /DistributedVirtualPortgroup/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**distributed_virtual_portgroup_get_host**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_host) | **GET** /DistributedVirtualPortgroup/{moId}/host | Hosts attached to this network. 
[**distributed_virtual_portgroup_get_key**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_key) | **GET** /DistributedVirtualPortgroup/{moId}/key | Generated UUID of the portgroup. 
[**distributed_virtual_portgroup_get_name**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_name) | **GET** /DistributedVirtualPortgroup/{moId}/name | Name of this entity, unique relative to its parent. 
[**distributed_virtual_portgroup_get_overall_status**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_overall_status) | **GET** /DistributedVirtualPortgroup/{moId}/overallStatus | General health of this managed entity. 
[**distributed_virtual_portgroup_get_parent**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_parent) | **GET** /DistributedVirtualPortgroup/{moId}/parent | Parent of this entity. 
[**distributed_virtual_portgroup_get_permission**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_permission) | **GET** /DistributedVirtualPortgroup/{moId}/permission | List of permissions defined for this entity. 
[**distributed_virtual_portgroup_get_port_keys**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_port_keys) | **GET** /DistributedVirtualPortgroup/{moId}/portKeys | Port keys for the set of ports in the portgroup. 
[**distributed_virtual_portgroup_get_recent_task**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_recent_task) | **GET** /DistributedVirtualPortgroup/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**distributed_virtual_portgroup_get_summary**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_summary) | **GET** /DistributedVirtualPortgroup/{moId}/summary | Properties of a network. 
[**distributed_virtual_portgroup_get_tag**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_tag) | **GET** /DistributedVirtualPortgroup/{moId}/tag | The set of tags associated with this managed entity. 
[**distributed_virtual_portgroup_get_triggered_alarm_state**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_triggered_alarm_state) | **GET** /DistributedVirtualPortgroup/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**distributed_virtual_portgroup_get_value**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_value) | **GET** /DistributedVirtualPortgroup/{moId}/value | List of custom field values. 
[**distributed_virtual_portgroup_get_vm**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_get_vm) | **GET** /DistributedVirtualPortgroup/{moId}/vm | Virtual machines using this network. 
[**distributed_virtual_portgroup_reconfigure_dv_portgroup_task**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_reconfigure_dv_portgroup_task) | **POST** /DistributedVirtualPortgroup/{moId}/ReconfigureDVPortgroup_Task | Reconfigures one or more distributed virtual portgroups. 
[**distributed_virtual_portgroup_reload**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_reload) | **POST** /DistributedVirtualPortgroup/{moId}/Reload | Reload the entity state. 
[**distributed_virtual_portgroup_rename_task**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_rename_task) | **POST** /DistributedVirtualPortgroup/{moId}/Rename_Task | Renames this managed entity. 
[**distributed_virtual_portgroup_set_custom_value**](DistributedVirtualPortgroupApi.md#distributed_virtual_portgroup_set_custom_value) | **POST** /DistributedVirtualPortgroup/{moId}/setCustomValue | Assigns a value to a custom field. 


# **distributed_virtual_portgroup_destroy_network**
> distributed_virtual_portgroup_destroy_network(mo_id)

Removes a network. 

Deprecated as of VI API 2.5 do not use this method. This method throws *ResourceInUse*. Networks are automatically removed when no longer in use, so this method is unnecessary.  Removes a network.  A network can be removed only if it is not used by any host or virtual machine.  ***Required privileges:*** Network.Delete 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes a network. 
        api_instance.distributed_virtual_portgroup_destroy_network(mo_id)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_destroy_network: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***ResourceInUse***: if one or more hosts or virtual machines are configured to use the network.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_portgroup_destroy_task**
> ManagedObjectReference distributed_virtual_portgroup_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** DVPortgroup.Delete 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.distributed_virtual_portgroup_destroy_task(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_destroy_task: %s\n" % e)
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

# **distributed_virtual_portgroup_dv_portgroup_rollback_task**
> ManagedObjectReference distributed_virtual_portgroup_dv_portgroup_rollback_task(mo_id, dv_portgroup_rollback_request_type)

This method determines if the portgroup configuration has changed. 

This method determines if the portgroup configuration has changed.  If it has changed, the method returns a *DVPortgroupConfigSpec*. Use the *DistributedVirtualPortgroup.ReconfigureDVPortgroup_Task* method to apply the rollback configuration to the portgroup. You can use the rollback method only on a portgroup that is associated with a *VmwareDistributedVirtualSwitch*. - If you specify the <code>entityBackup</code> parameter, the returned   configuration specification represents the exported portgroup configuration.   If the <code>entityBackup</code> matches the current portgroup   configuration, the method does not return a configuration specification. - If <code>entityBackup</code> is not specified, the returned configuration   specification represents a previous state of the portgroup, if available.   When you use a VMware distributed virtual switch, each time you reconfigure   the switch, the Server saves the switch configuration before applying the updates.   If the vCenter Server is restarted, the saved configuration is not preserved   and the method does not return a configuration specification.    To use the rollback method, you must have the DVPortgroup.Read privilege.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dv_portgroup_rollback_request_type import DVPortgroupRollbackRequestType
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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    dv_portgroup_rollback_request_type = vmware_vi.DVPortgroupRollbackRequestType() # DVPortgroupRollbackRequestType | 

    try:
        # This method determines if the portgroup configuration has changed. 
        api_response = api_instance.distributed_virtual_portgroup_dv_portgroup_rollback_task(mo_id, dv_portgroup_rollback_request_type)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_dv_portgroup_rollback_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_dv_portgroup_rollback_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **dv_portgroup_rollback_request_type** | [**DVPortgroupRollbackRequestType**](DVPortgroupRollbackRequestType.md)|  | 

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
**200** | Returns a *Task* object with which to monitor the operation. If the distributed virtual portgroup configuration has changed, the *Task*.*Task.info*.*TaskInfo.result* property contains the *DVPortgroupConfigSpec* object.  Refers instance of *Task*.  |  -  |
**500** | ***RollbackFailure***: if there is no configuration specified in entityBackup and the previous configuration does not exist either  ***DvsFault***: if operation fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_portgroup_get_alarm_actions_enabled**
> bool distributed_virtual_portgroup_get_alarm_actions_enabled(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_alarm_actions_enabled(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_alarm_actions_enabled: %s\n" % e)
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

# **distributed_virtual_portgroup_get_available_field**
> List[CustomFieldDef] distributed_virtual_portgroup_get_available_field(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.distributed_virtual_portgroup_get_available_field(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_available_field: %s\n" % e)
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

# **distributed_virtual_portgroup_get_config**
> DVPortgroupConfigInfo distributed_virtual_portgroup_get_config(mo_id)

Configuration of the portgroup. 

Configuration of the portgroup.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.dv_portgroup_config_info import DVPortgroupConfigInfo
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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of the portgroup. 
        api_response = api_instance.distributed_virtual_portgroup_get_config(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**DVPortgroupConfigInfo**](DVPortgroupConfigInfo.md)

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

# **distributed_virtual_portgroup_get_config_issue**
> List[Event] distributed_virtual_portgroup_get_config_issue(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_config_issue(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config_issue: %s\n" % e)
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

# **distributed_virtual_portgroup_get_config_status**
> ManagedEntityStatusEnum distributed_virtual_portgroup_get_config_status(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_config_status(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_config_status: %s\n" % e)
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

# **distributed_virtual_portgroup_get_custom_value**
> List[CustomFieldValue] distributed_virtual_portgroup_get_custom_value(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.distributed_virtual_portgroup_get_custom_value(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_custom_value: %s\n" % e)
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

# **distributed_virtual_portgroup_get_declared_alarm_state**
> List[AlarmState] distributed_virtual_portgroup_get_declared_alarm_state(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_declared_alarm_state(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_declared_alarm_state: %s\n" % e)
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

# **distributed_virtual_portgroup_get_disabled_method**
> List[str] distributed_virtual_portgroup_get_disabled_method(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_disabled_method(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_disabled_method: %s\n" % e)
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

# **distributed_virtual_portgroup_get_effective_role**
> List[int] distributed_virtual_portgroup_get_effective_role(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_effective_role(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_effective_role: %s\n" % e)
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

# **distributed_virtual_portgroup_get_host**
> List[ManagedObjectReference] distributed_virtual_portgroup_get_host(mo_id)

Hosts attached to this network. 

Hosts attached to this network. 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Hosts attached to this network. 
        api_response = api_instance.distributed_virtual_portgroup_get_host(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_host: %s\n" % e)
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
**200** | Refers instances of *HostSystem*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_portgroup_get_key**
> str distributed_virtual_portgroup_get_key(mo_id)

Generated UUID of the portgroup. 

Generated UUID of the portgroup.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Generated UUID of the portgroup. 
        api_response = api_instance.distributed_virtual_portgroup_get_key(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_key: %s\n" % e)
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

# **distributed_virtual_portgroup_get_name**
> str distributed_virtual_portgroup_get_name(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.distributed_virtual_portgroup_get_name(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_name: %s\n" % e)
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

# **distributed_virtual_portgroup_get_overall_status**
> ManagedEntityStatusEnum distributed_virtual_portgroup_get_overall_status(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_overall_status(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_overall_status: %s\n" % e)
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

# **distributed_virtual_portgroup_get_parent**
> ManagedObjectReference distributed_virtual_portgroup_get_parent(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_parent(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_parent: %s\n" % e)
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

# **distributed_virtual_portgroup_get_permission**
> List[Permission] distributed_virtual_portgroup_get_permission(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_permission(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_permission: %s\n" % e)
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

# **distributed_virtual_portgroup_get_port_keys**
> List[str] distributed_virtual_portgroup_get_port_keys(mo_id)

Port keys for the set of ports in the portgroup. 

Port keys for the set of ports in the portgroup.  ***Since:*** vSphere API 4.0 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Port keys for the set of ports in the portgroup. 
        api_response = api_instance.distributed_virtual_portgroup_get_port_keys(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_port_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_port_keys: %s\n" % e)
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

# **distributed_virtual_portgroup_get_recent_task**
> List[ManagedObjectReference] distributed_virtual_portgroup_get_recent_task(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_recent_task(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_recent_task: %s\n" % e)
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

# **distributed_virtual_portgroup_get_summary**
> NetworkSummary distributed_virtual_portgroup_get_summary(mo_id)

Properties of a network. 

Properties of a network. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.network_summary import NetworkSummary
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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Properties of a network. 
        api_response = api_instance.distributed_virtual_portgroup_get_summary(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**NetworkSummary**](NetworkSummary.md)

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

# **distributed_virtual_portgroup_get_tag**
> List[Tag] distributed_virtual_portgroup_get_tag(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.distributed_virtual_portgroup_get_tag(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_tag: %s\n" % e)
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

# **distributed_virtual_portgroup_get_triggered_alarm_state**
> List[AlarmState] distributed_virtual_portgroup_get_triggered_alarm_state(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.distributed_virtual_portgroup_get_triggered_alarm_state(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_triggered_alarm_state: %s\n" % e)
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

# **distributed_virtual_portgroup_get_value**
> List[CustomFieldValue] distributed_virtual_portgroup_get_value(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.distributed_virtual_portgroup_get_value(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_value: %s\n" % e)
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

# **distributed_virtual_portgroup_get_vm**
> List[ManagedObjectReference] distributed_virtual_portgroup_get_vm(mo_id)

Virtual machines using this network. 

Virtual machines using this network. 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Virtual machines using this network. 
        api_response = api_instance.distributed_virtual_portgroup_get_vm(mo_id)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_get_vm: %s\n" % e)
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

# **distributed_virtual_portgroup_reconfigure_dv_portgroup_task**
> ManagedObjectReference distributed_virtual_portgroup_reconfigure_dv_portgroup_task(mo_id, reconfigure_dv_portgroup_request_type)

Reconfigures one or more distributed virtual portgroups. 

Reconfigures one or more distributed virtual portgroups.  You can use this method to set portgroup properties or to reset the portgroup to a previous state.  **Reconfiguring a Standard Distributed Virtual Portgroup**  To reconfigure a *DistributedVirtualPortgroup*, use a *DVPortgroupConfigSpec* to set the portgroup properties.  **Reconfiguring a Portgroup Associated With a VMware Distributed Virtual Switch**  If you use a *VmwareDistributedVirtualSwitch*, you can perform the following portgroup reconfiguration: - Use a *DVPortgroupConfigSpec*   to set the portgroup properties. - Use the *DVPortgroupConfigSpec*   returned by *DistributedVirtualPortgroup.DVPortgroupRollback_Task*   to reset the portgroup to a previous state.    The following privileges are required to reconfigure a portgroup. - DVPortgroup.PolicyOp if you are changing the policy of the portgroup. - DVPortgroup.ScopeOp if you are changing the scope of the portgroup. - DVPortgroup.Modify for anything else.    ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfigure_dv_portgroup_request_type import ReconfigureDVPortgroupRequestType
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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_dv_portgroup_request_type = vmware_vi.ReconfigureDVPortgroupRequestType() # ReconfigureDVPortgroupRequestType | 

    try:
        # Reconfigures one or more distributed virtual portgroups. 
        api_response = api_instance.distributed_virtual_portgroup_reconfigure_dv_portgroup_task(mo_id, reconfigure_dv_portgroup_request_type)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_reconfigure_dv_portgroup_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_reconfigure_dv_portgroup_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_dv_portgroup_request_type** | [**ReconfigureDVPortgroupRequestType**](ReconfigureDVPortgroupRequestType.md)|  | 

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
**500** | ***DvsFault***: if spec is not valid.  ***NotSupported***: if the spec includes settings for any VDS feature that is not supported on this switch.  ***DvsNotAuthorized***: if login-session&#39;s extension key does not match the switch&#39;s configured *DVSConfigInfo.extensionKey*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_virtual_portgroup_reload**
> distributed_virtual_portgroup_reload(mo_id)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.distributed_virtual_portgroup_reload(mo_id)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_reload: %s\n" % e)
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

# **distributed_virtual_portgroup_rename_task**
> ManagedObjectReference distributed_virtual_portgroup_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** DVPortgroup.Modify 

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.distributed_virtual_portgroup_rename_task(mo_id, rename_request_type)
        print("The response of DistributedVirtualPortgroupApi->distributed_virtual_portgroup_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_rename_task: %s\n" % e)
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

# **distributed_virtual_portgroup_set_custom_value**
> distributed_virtual_portgroup_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.DistributedVirtualPortgroupApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.distributed_virtual_portgroup_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling DistributedVirtualPortgroupApi->distributed_virtual_portgroup_set_custom_value: %s\n" % e)
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

