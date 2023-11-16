# vmware_vi.ClusterComputeResourceApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_compute_resource_abandon_hci_workflow**](ClusterComputeResourceApi.md#cluster_compute_resource_abandon_hci_workflow) | **POST** /ClusterComputeResource/{moId}/AbandonHciWorkflow | Opt out of the HCI workflow. 
[**cluster_compute_resource_add_host_task**](ClusterComputeResourceApi.md#cluster_compute_resource_add_host_task) | **POST** /ClusterComputeResource/{moId}/AddHost_Task | Adds a host to the cluster. 
[**cluster_compute_resource_apply_recommendation**](ClusterComputeResourceApi.md#cluster_compute_resource_apply_recommendation) | **POST** /ClusterComputeResource/{moId}/ApplyRecommendation | Applies a recommendation from the drsRecommendation or the recommendation list. 
[**cluster_compute_resource_cancel_recommendation**](ClusterComputeResourceApi.md#cluster_compute_resource_cancel_recommendation) | **POST** /ClusterComputeResource/{moId}/CancelRecommendation | Cancels a recommendation. 
[**cluster_compute_resource_cluster_enter_maintenance_mode**](ClusterComputeResourceApi.md#cluster_compute_resource_cluster_enter_maintenance_mode) | **POST** /ClusterComputeResource/{moId}/ClusterEnterMaintenanceMode | The API takes a list of hosts in the cluster as input, and returns a list of hosts in \&quot;ClusterMaintenanceResult\&quot; that the server can successfully evacuate given the existing constraints in the cluster, such as HA, FT, Vmotion compatibility, reservations, affinity rules, etc. 
[**cluster_compute_resource_configure_hci_task**](ClusterComputeResourceApi.md#cluster_compute_resource_configure_hci_task) | **POST** /ClusterComputeResource/{moId}/ConfigureHCI_Task | Configures the cluster. 
[**cluster_compute_resource_destroy_task**](ClusterComputeResourceApi.md#cluster_compute_resource_destroy_task) | **POST** /ClusterComputeResource/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**cluster_compute_resource_evc_manager**](ClusterComputeResourceApi.md#cluster_compute_resource_evc_manager) | **POST** /ClusterComputeResource/{moId}/EvcManager | A managed object that controls Enhanced vMotion Compatibility mode for this cluster. 
[**cluster_compute_resource_extend_hci_task**](ClusterComputeResourceApi.md#cluster_compute_resource_extend_hci_task) | **POST** /ClusterComputeResource/{moId}/ExtendHCI_Task | Extend an existing HCI cluster. 
[**cluster_compute_resource_find_rules_for_vm**](ClusterComputeResourceApi.md#cluster_compute_resource_find_rules_for_vm) | **POST** /ClusterComputeResource/{moId}/FindRulesForVm | Finds all enabled and disabled VM-VM Affinity and Anti-Affinity rules, involving the given Virtual Machine. 
[**cluster_compute_resource_get_action_history**](ClusterComputeResourceApi.md#cluster_compute_resource_get_action_history) | **GET** /ClusterComputeResource/{moId}/actionHistory | The set of actions that have been performed recently. 
[**cluster_compute_resource_get_alarm_actions_enabled**](ClusterComputeResourceApi.md#cluster_compute_resource_get_alarm_actions_enabled) | **GET** /ClusterComputeResource/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**cluster_compute_resource_get_available_field**](ClusterComputeResourceApi.md#cluster_compute_resource_get_available_field) | **GET** /ClusterComputeResource/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**cluster_compute_resource_get_config_issue**](ClusterComputeResourceApi.md#cluster_compute_resource_get_config_issue) | **GET** /ClusterComputeResource/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**cluster_compute_resource_get_config_manager_enabled**](ClusterComputeResourceApi.md#cluster_compute_resource_get_config_manager_enabled) | **GET** /ClusterComputeResource/{moId}/configManagerEnabled | Flag indicating whether or not desired configuration management platform is enabled on the compute resource. 
[**cluster_compute_resource_get_config_status**](ClusterComputeResourceApi.md#cluster_compute_resource_get_config_status) | **GET** /ClusterComputeResource/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**cluster_compute_resource_get_configuration**](ClusterComputeResourceApi.md#cluster_compute_resource_get_configuration) | **GET** /ClusterComputeResource/{moId}/configuration | Configuration of the cluster. 
[**cluster_compute_resource_get_configuration_ex**](ClusterComputeResourceApi.md#cluster_compute_resource_get_configuration_ex) | **GET** /ClusterComputeResource/{moId}/configurationEx | Configuration of the compute resource; applies to both standalone hosts and clusters. 
[**cluster_compute_resource_get_custom_value**](ClusterComputeResourceApi.md#cluster_compute_resource_get_custom_value) | **GET** /ClusterComputeResource/{moId}/customValue | Custom field values. 
[**cluster_compute_resource_get_datastore**](ClusterComputeResourceApi.md#cluster_compute_resource_get_datastore) | **GET** /ClusterComputeResource/{moId}/datastore | The datastore property is the subset of datastore objects in the datacenter available in this ComputeResource. 
[**cluster_compute_resource_get_declared_alarm_state**](ClusterComputeResourceApi.md#cluster_compute_resource_get_declared_alarm_state) | **GET** /ClusterComputeResource/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**cluster_compute_resource_get_disabled_method**](ClusterComputeResourceApi.md#cluster_compute_resource_get_disabled_method) | **GET** /ClusterComputeResource/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**cluster_compute_resource_get_drs_fault**](ClusterComputeResourceApi.md#cluster_compute_resource_get_drs_fault) | **GET** /ClusterComputeResource/{moId}/drsFault | A collection of the DRS faults generated in the last DRS invocation. 
[**cluster_compute_resource_get_drs_recommendation**](ClusterComputeResourceApi.md#cluster_compute_resource_get_drs_recommendation) | **GET** /ClusterComputeResource/{moId}/drsRecommendation | If DRS is enabled, this returns the set of recommended migrations from the DRS module. 
[**cluster_compute_resource_get_effective_role**](ClusterComputeResourceApi.md#cluster_compute_resource_get_effective_role) | **GET** /ClusterComputeResource/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**cluster_compute_resource_get_environment_browser**](ClusterComputeResourceApi.md#cluster_compute_resource_get_environment_browser) | **GET** /ClusterComputeResource/{moId}/environmentBrowser | The environment browser object that identifies the environments that are supported on this compute resource. 
[**cluster_compute_resource_get_hci_config**](ClusterComputeResourceApi.md#cluster_compute_resource_get_hci_config) | **GET** /ClusterComputeResource/{moId}/hciConfig | This is applicable to clusters which are configured using the HCI workflow and contains data related to the workflow and specification. 
[**cluster_compute_resource_get_host**](ClusterComputeResourceApi.md#cluster_compute_resource_get_host) | **GET** /ClusterComputeResource/{moId}/host | List of hosts that are part of this compute resource. 
[**cluster_compute_resource_get_lifecycle_managed**](ClusterComputeResourceApi.md#cluster_compute_resource_get_lifecycle_managed) | **GET** /ClusterComputeResource/{moId}/lifecycleManaged | Flag indicating whether or not the lifecycle of the compute resource is managed. 
[**cluster_compute_resource_get_migration_history**](ClusterComputeResourceApi.md#cluster_compute_resource_get_migration_history) | **GET** /ClusterComputeResource/{moId}/migrationHistory | The set of migration decisions that have recently been performed. 
[**cluster_compute_resource_get_name**](ClusterComputeResourceApi.md#cluster_compute_resource_get_name) | **GET** /ClusterComputeResource/{moId}/name | Name of this entity, unique relative to its parent. 
[**cluster_compute_resource_get_network**](ClusterComputeResourceApi.md#cluster_compute_resource_get_network) | **GET** /ClusterComputeResource/{moId}/network | The subset of network objects available in the datacenter that is available in this ComputeResource. 
[**cluster_compute_resource_get_overall_status**](ClusterComputeResourceApi.md#cluster_compute_resource_get_overall_status) | **GET** /ClusterComputeResource/{moId}/overallStatus | General health of this managed entity. 
[**cluster_compute_resource_get_parent**](ClusterComputeResourceApi.md#cluster_compute_resource_get_parent) | **GET** /ClusterComputeResource/{moId}/parent | Parent of this entity. 
[**cluster_compute_resource_get_permission**](ClusterComputeResourceApi.md#cluster_compute_resource_get_permission) | **GET** /ClusterComputeResource/{moId}/permission | List of permissions defined for this entity. 
[**cluster_compute_resource_get_recent_task**](ClusterComputeResourceApi.md#cluster_compute_resource_get_recent_task) | **GET** /ClusterComputeResource/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**cluster_compute_resource_get_recommendation**](ClusterComputeResourceApi.md#cluster_compute_resource_get_recommendation) | **GET** /ClusterComputeResource/{moId}/recommendation | List of recommended actions for the cluster. 
[**cluster_compute_resource_get_resource_pool**](ClusterComputeResourceApi.md#cluster_compute_resource_get_resource_pool) | **GET** /ClusterComputeResource/{moId}/resourcePool | Reference to root resource pool. 
[**cluster_compute_resource_get_resource_usage**](ClusterComputeResourceApi.md#cluster_compute_resource_get_resource_usage) | **POST** /ClusterComputeResource/{moId}/GetResourceUsage | This API can be invoked to get the current CPU, memory and storage usage in the cluster. 
[**cluster_compute_resource_get_summary**](ClusterComputeResourceApi.md#cluster_compute_resource_get_summary) | **GET** /ClusterComputeResource/{moId}/summary | Basic runtime information about a compute resource. 
[**cluster_compute_resource_get_summary_ex**](ClusterComputeResourceApi.md#cluster_compute_resource_get_summary_ex) | **GET** /ClusterComputeResource/{moId}/summaryEx | The cluster summary. 
[**cluster_compute_resource_get_system_vms_restricted_datastores**](ClusterComputeResourceApi.md#cluster_compute_resource_get_system_vms_restricted_datastores) | **POST** /ClusterComputeResource/{moId}/GetSystemVMsRestrictedDatastores | Retrieve all the datastores that are either listed in *ClusterSystemVMsConfigInfo.notAllowedDatastores* or are tagged with a category from *ClusterSystemVMsConfigInfo.dsTagCategoriesToExclude*. 
[**cluster_compute_resource_get_tag**](ClusterComputeResourceApi.md#cluster_compute_resource_get_tag) | **GET** /ClusterComputeResource/{moId}/tag | The set of tags associated with this managed entity. 
[**cluster_compute_resource_get_triggered_alarm_state**](ClusterComputeResourceApi.md#cluster_compute_resource_get_triggered_alarm_state) | **GET** /ClusterComputeResource/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**cluster_compute_resource_get_value**](ClusterComputeResourceApi.md#cluster_compute_resource_get_value) | **GET** /ClusterComputeResource/{moId}/value | List of custom field values. 
[**cluster_compute_resource_move_host_into_task**](ClusterComputeResourceApi.md#cluster_compute_resource_move_host_into_task) | **POST** /ClusterComputeResource/{moId}/MoveHostInto_Task | Moves an existing host into a cluster. 
[**cluster_compute_resource_move_into_task**](ClusterComputeResourceApi.md#cluster_compute_resource_move_into_task) | **POST** /ClusterComputeResource/{moId}/MoveInto_Task | Moves an existing host into a cluster. 
[**cluster_compute_resource_place_vm**](ClusterComputeResourceApi.md#cluster_compute_resource_place_vm) | **POST** /ClusterComputeResource/{moId}/PlaceVm | This method returns a *PlacementResult* object. 
[**cluster_compute_resource_recommend_hosts_for_vm**](ClusterComputeResourceApi.md#cluster_compute_resource_recommend_hosts_for_vm) | **POST** /ClusterComputeResource/{moId}/RecommendHostsForVm | Gets a recommendation for where to power on, resume, revert from powered-off state to powered on state, or to migrate a specific virtual machine. 
[**cluster_compute_resource_reconfigure_cluster_task**](ClusterComputeResourceApi.md#cluster_compute_resource_reconfigure_cluster_task) | **POST** /ClusterComputeResource/{moId}/ReconfigureCluster_Task | Reconfigures a cluster. 
[**cluster_compute_resource_reconfigure_compute_resource_task**](ClusterComputeResourceApi.md#cluster_compute_resource_reconfigure_compute_resource_task) | **POST** /ClusterComputeResource/{moId}/ReconfigureComputeResource_Task | Change the compute resource configuration. 
[**cluster_compute_resource_refresh_recommendation**](ClusterComputeResourceApi.md#cluster_compute_resource_refresh_recommendation) | **POST** /ClusterComputeResource/{moId}/RefreshRecommendation | Make DRS invoke again and return a new list of recommendations. 
[**cluster_compute_resource_reload**](ClusterComputeResourceApi.md#cluster_compute_resource_reload) | **POST** /ClusterComputeResource/{moId}/Reload | Reload the entity state. 
[**cluster_compute_resource_rename_task**](ClusterComputeResourceApi.md#cluster_compute_resource_rename_task) | **POST** /ClusterComputeResource/{moId}/Rename_Task | Renames this managed entity. 
[**cluster_compute_resource_retrieve_das_advanced_runtime_info**](ClusterComputeResourceApi.md#cluster_compute_resource_retrieve_das_advanced_runtime_info) | **POST** /ClusterComputeResource/{moId}/RetrieveDasAdvancedRuntimeInfo | Retrieve DAS advanced runtime info for this cluster. 
[**cluster_compute_resource_set_crypto_mode**](ClusterComputeResourceApi.md#cluster_compute_resource_set_crypto_mode) | **POST** /ClusterComputeResource/{moId}/SetCryptoMode | Set the desired encryption mode and host key for the cluster. 
[**cluster_compute_resource_set_custom_value**](ClusterComputeResourceApi.md#cluster_compute_resource_set_custom_value) | **POST** /ClusterComputeResource/{moId}/setCustomValue | Assigns a value to a custom field. 
[**cluster_compute_resource_stamp_all_rules_with_uuid_task**](ClusterComputeResourceApi.md#cluster_compute_resource_stamp_all_rules_with_uuid_task) | **POST** /ClusterComputeResource/{moId}/StampAllRulesWithUuid_Task | Stamp all rules in the cluster with ruleUuid. 
[**cluster_compute_resource_validate_hci_configuration**](ClusterComputeResourceApi.md#cluster_compute_resource_validate_hci_configuration) | **POST** /ClusterComputeResource/{moId}/ValidateHCIConfiguration | Validate HCI configuration in pre-configure and post-configure use-cases. 


# **cluster_compute_resource_abandon_hci_workflow**
> cluster_compute_resource_abandon_hci_workflow(mo_id)

Opt out of the HCI workflow. 

Opt out of the HCI workflow.  This operation is only allowed on a cluster that was created with the HCI workflow. When the cluster is created, but still unconfigured, the *workflowState* is \"in\\_progress\". The AbandonHciWorkflow method may be called at any time before cluster configuration begins; it is not possible to abandon the workflow during the configuration procedure.  ***Since:*** vSphere API 6.7.1  ***Required privileges:*** Host.Inventory.EditCluster 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Opt out of the HCI workflow. 
        api_instance.cluster_compute_resource_abandon_hci_workflow(mo_id)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_abandon_hci_workflow: %s\n" % e)
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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_add_host_task**
> ManagedObjectReference cluster_compute_resource_add_host_task(mo_id, add_host_request_type)

Adds a host to the cluster. 

Adds a host to the cluster.  The hostname must be either an IP address, such as 192.168.0.1, or a DNS resolvable name. DNS names may be fully qualified names, such as host1.domain1.com, or a short name such as host1, providing host1 resolves to host1.domain1.com. The system uses DNS to resolve short names to fully qualified names. If the cluster supports nested resource pools and the user specifies the optional ResourcePool argument, then the host's root resource pool becomes the specified resource pool. The stand-alone host resource hierarchy is imported into the new nested resource pool.  If the cluster does not support nested resource pools, then the stand-alone host resource hierarchy is discarded and all virtual machines on the host are put under the cluster's root resource pool.  In addition to the Host.Inventory.AddHostToCluster and Resource.AssignVMToPool privileges, it requires System.View privilege on the VM folder that the VMs of the host will be placed on.  ***Required privileges:*** Host.Inventory.AddHostToCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_host_request_type import AddHostRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_host_request_type = vmware_vi.AddHostRequestType() # AddHostRequestType | 

    try:
        # Adds a host to the cluster. 
        api_response = api_instance.cluster_compute_resource_add_host_task(mo_id, add_host_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_add_host_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_add_host_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_host_request_type** | [**AddHostRequestType**](AddHostRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly added *HostSystem* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidLogin***: if \&quot;asConnected\&quot; is specified but authentication with the new host fails.  ***HostConnectFault***: if an error occurred when connecting to a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.  ***AlreadyBeingManaged***: if the host is already being managed by a VirtualCenter server.  ***NotEnoughLicenses***: if no licenses are available to add this host.  ***NoHost***: if the host cannot be contacted.  ***NotSupportedHost***: if the host is running a software version that does not support clustering features. It may still be possible to add the host as a stand-alone host.  ***TooManyHosts***: if no additional hosts can be added to the cluster.  ***AgentInstallFailed***: if there is an error installing the VirtualCenter agent on the host.  ***AlreadyConnected***: if asConnected is true and the host is already connected to VirtualCenter.  ***SSLVerifyFault***: if the host certificate could not be authenticated  ***DuplicateName***: if another host in the same cluster has the name.  ***NoPermission***: if there are crypto keys to be sent to the host, but the user does not have Cryptographer.RegisterHost privilege on the Cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_apply_recommendation**
> cluster_compute_resource_apply_recommendation(mo_id, apply_recommendation_request_type)

Applies a recommendation from the drsRecommendation or the recommendation list. 

Applies a recommendation from the drsRecommendation or the recommendation list.  Each recommendation can be applied only once.  resource.applyRecommendation privilege is required if the recommendation is DRS migration or power management recommendations. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.apply_recommendation_request_type import ApplyRecommendationRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    apply_recommendation_request_type = vmware_vi.ApplyRecommendationRequestType() # ApplyRecommendationRequestType | 

    try:
        # Applies a recommendation from the drsRecommendation or the recommendation list. 
        api_instance.cluster_compute_resource_apply_recommendation(mo_id, apply_recommendation_request_type)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_apply_recommendation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **apply_recommendation_request_type** | [**ApplyRecommendationRequestType**](ApplyRecommendationRequestType.md)|  | 

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

# **cluster_compute_resource_cancel_recommendation**
> cluster_compute_resource_cancel_recommendation(mo_id, cancel_recommendation_request_type)

Cancels a recommendation. 

Cancels a recommendation.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cancel_recommendation_request_type import CancelRecommendationRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cancel_recommendation_request_type = vmware_vi.CancelRecommendationRequestType() # CancelRecommendationRequestType | 

    try:
        # Cancels a recommendation. 
        api_instance.cluster_compute_resource_cancel_recommendation(mo_id, cancel_recommendation_request_type)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_cancel_recommendation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cancel_recommendation_request_type** | [**CancelRecommendationRequestType**](CancelRecommendationRequestType.md)|  | 

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

# **cluster_compute_resource_cluster_enter_maintenance_mode**
> ClusterEnterMaintenanceResult cluster_compute_resource_cluster_enter_maintenance_mode(mo_id, cluster_enter_maintenance_mode_request_type)

The API takes a list of hosts in the cluster as input, and returns a list of hosts in \"ClusterMaintenanceResult\" that the server can successfully evacuate given the existing constraints in the cluster, such as HA, FT, Vmotion compatibility, reservations, affinity rules, etc. 

The API takes a list of hosts in the cluster as input, and returns a list of hosts in \"ClusterMaintenanceResult\" that the server can successfully evacuate given the existing constraints in the cluster, such as HA, FT, Vmotion compatibility, reservations, affinity rules, etc.  The client is allowed to pass all hosts in the cluster to the API, even though all of them cannot enter maintenance mode at the same time. The list returned from the API contains the largest number of hosts that the server can evacuate simultaneously. The client can then request to enter each host in the returned list into maintenance mode. The client can specify an integer \"DemandCapacityRatioTarget\" option in the \"option\" parameter. The allowed values of the option range from 40 to 200, and the default value is 100. This option controls how much resource overcommitment the server should make in consolidating the VMs onto fewer hosts. A value of 100 means the server will keep the same amount of powered-on capacity as the current VM demands. A value less than 100 means undercommitted resources. A value greater than 100 means overcommitted resources. The hosts are recommended based on the inventory at the time of the API invocation. It is not guaranteed that the actual enter-maintenance tasks on the hosts will succeed, if the inventory changes after the API returns, or if vmotions fail due to unexpected conditions. For possible exceptions thrown by the necessary relocate operations, see *VirtualMachine.MigrateVM_Task*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_enter_maintenance_mode_request_type import ClusterEnterMaintenanceModeRequestType
from vmware_vi.models.cluster_enter_maintenance_result import ClusterEnterMaintenanceResult
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    cluster_enter_maintenance_mode_request_type = vmware_vi.ClusterEnterMaintenanceModeRequestType() # ClusterEnterMaintenanceModeRequestType | 

    try:
        # The API takes a list of hosts in the cluster as input, and returns a list of hosts in \"ClusterMaintenanceResult\" that the server can successfully evacuate given the existing constraints in the cluster, such as HA, FT, Vmotion compatibility, reservations, affinity rules, etc. 
        api_response = api_instance.cluster_compute_resource_cluster_enter_maintenance_mode(mo_id, cluster_enter_maintenance_mode_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_cluster_enter_maintenance_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_cluster_enter_maintenance_mode: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **cluster_enter_maintenance_mode_request_type** | [**ClusterEnterMaintenanceModeRequestType**](ClusterEnterMaintenanceModeRequestType.md)|  | 

### Return type

[**ClusterEnterMaintenanceResult**](ClusterEnterMaintenanceResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A *ClusterEnterMaintenanceResult* object, which consists of an array of recommendations for hosts that can be evacuated and an array of faults for hosts that cannot be evacuated.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_configure_hci_task**
> ManagedObjectReference cluster_compute_resource_configure_hci_task(mo_id, configure_hci_request_type)

Configures the cluster. 

Configures the cluster.  This API requires Host.Inventory.EditCluster privilege on the cluster and the hosts; additional privileges might be required depending on the inputs. This operation is only allowed on a cluster that was created with the HCI workflow. Before calling this method, it is recommended that *ClusterComputeResource.ValidateHCIConfiguration* is invoked with the DvsProfile objects listed in *ClusterComputeResourceHCIConfigSpec.dvsProf* along with the hosts listed in *ClusterComputeResourceHostConfigurationInput* to validate that the desired network settings can be applied correctly.  ***Since:*** vSphere API 6.7.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_hci_request_type import ConfigureHCIRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_hci_request_type = vmware_vi.ConfigureHCIRequestType() # ConfigureHCIRequestType | 

    try:
        # Configures the cluster. 
        api_response = api_instance.cluster_compute_resource_configure_hci_task(mo_id, configure_hci_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_configure_hci_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_configure_hci_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_hci_request_type** | [**ConfigureHCIRequestType**](ConfigureHCIRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *TaskInfo.result* property in the *Task* contains a *ClusterComputeResourceClusterConfigResult* object, which upon completion will contain a list of hosts which were successfully configured and a list of hosts which could not be configured.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_destroy_task**
> ManagedObjectReference cluster_compute_resource_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** Host.Inventory.DeleteCluster 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.cluster_compute_resource_destroy_task(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_destroy_task: %s\n" % e)
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

# **cluster_compute_resource_evc_manager**
> ManagedObjectReference cluster_compute_resource_evc_manager(mo_id)

A managed object that controls Enhanced vMotion Compatibility mode for this cluster. 

A managed object that controls Enhanced vMotion Compatibility mode for this cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A managed object that controls Enhanced vMotion Compatibility mode for this cluster. 
        api_response = api_instance.cluster_compute_resource_evc_manager(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_evc_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_evc_manager: %s\n" % e)
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
**200** | Refers instance of *ClusterEVCManager*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_extend_hci_task**
> ManagedObjectReference cluster_compute_resource_extend_hci_task(mo_id, extend_hci_request_type)

Extend an existing HCI cluster. 

Extend an existing HCI cluster.  This API requires Host.Inventory.EditCluster privilege on the cluster and the hosts, additional privileges might be required depending on the inputs.  ***Since:*** vSphere API 6.7.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extend_hci_request_type import ExtendHCIRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    extend_hci_request_type = vmware_vi.ExtendHCIRequestType() # ExtendHCIRequestType | 

    try:
        # Extend an existing HCI cluster. 
        api_response = api_instance.cluster_compute_resource_extend_hci_task(mo_id, extend_hci_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_extend_hci_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_extend_hci_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **extend_hci_request_type** | [**ExtendHCIRequestType**](ExtendHCIRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *TaskInfo.result* property in the *Task* contains a *ClusterComputeResourceClusterConfigResult* object, which upon successful completion would contain the list of hosts which couldn&#39;t be configured and a list of hosts which were successfully configured. This API can be called only after the cluster is configured using *ClusterComputeResource.ConfigureHCI_Task* and requires *ClusterComputeResourceHCIConfigInfo.workflowState* to be \&quot;done\&quot;.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_find_rules_for_vm**
> List[ClusterRuleInfo] cluster_compute_resource_find_rules_for_vm(mo_id, find_rules_for_vm_request_type)

Finds all enabled and disabled VM-VM Affinity and Anti-Affinity rules, involving the given Virtual Machine. 

Finds all enabled and disabled VM-VM Affinity and Anti-Affinity rules, involving the given Virtual Machine.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_rule_info import ClusterRuleInfo
from vmware_vi.models.find_rules_for_vm_request_type import FindRulesForVmRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    find_rules_for_vm_request_type = vmware_vi.FindRulesForVmRequestType() # FindRulesForVmRequestType | 

    try:
        # Finds all enabled and disabled VM-VM Affinity and Anti-Affinity rules, involving the given Virtual Machine. 
        api_response = api_instance.cluster_compute_resource_find_rules_for_vm(mo_id, find_rules_for_vm_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_find_rules_for_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_find_rules_for_vm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **find_rules_for_vm_request_type** | [**FindRulesForVmRequestType**](FindRulesForVmRequestType.md)|  | 

### Return type

[**List[ClusterRuleInfo]**](ClusterRuleInfo.md)

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

# **cluster_compute_resource_get_action_history**
> List[ClusterActionHistory] cluster_compute_resource_get_action_history(mo_id)

The set of actions that have been performed recently. 

The set of actions that have been performed recently.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_action_history import ClusterActionHistory
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of actions that have been performed recently. 
        api_response = api_instance.cluster_compute_resource_get_action_history(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_action_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_action_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ClusterActionHistory]**](ClusterActionHistory.md)

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

# **cluster_compute_resource_get_alarm_actions_enabled**
> bool cluster_compute_resource_get_alarm_actions_enabled(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.cluster_compute_resource_get_alarm_actions_enabled(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_alarm_actions_enabled: %s\n" % e)
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

# **cluster_compute_resource_get_available_field**
> List[CustomFieldDef] cluster_compute_resource_get_available_field(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.cluster_compute_resource_get_available_field(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_available_field: %s\n" % e)
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

# **cluster_compute_resource_get_config_issue**
> List[Event] cluster_compute_resource_get_config_issue(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.cluster_compute_resource_get_config_issue(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_config_issue: %s\n" % e)
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

# **cluster_compute_resource_get_config_manager_enabled**
> bool cluster_compute_resource_get_config_manager_enabled(mo_id)

Flag indicating whether or not desired configuration management platform is enabled on the compute resource. 

Flag indicating whether or not desired configuration management platform is enabled on the compute resource.  This property can be set only at the time of creation or through the *ComputeResource.EnableConfigurationManagement* method.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Flag indicating whether or not desired configuration management platform is enabled on the compute resource. 
        api_response = api_instance.cluster_compute_resource_get_config_manager_enabled(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_config_manager_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_config_manager_enabled: %s\n" % e)
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

# **cluster_compute_resource_get_config_status**
> ManagedEntityStatusEnum cluster_compute_resource_get_config_status(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.cluster_compute_resource_get_config_status(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_config_status: %s\n" % e)
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

# **cluster_compute_resource_get_configuration**
> ClusterConfigInfo cluster_compute_resource_get_configuration(mo_id)

Configuration of the cluster. 

Deprecated as of VI API 2.5, use *ComputeResource.configurationEx*, which is a *ClusterConfigInfoEx* data object..  Configuration of the cluster. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_config_info import ClusterConfigInfo
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of the cluster. 
        api_response = api_instance.cluster_compute_resource_get_configuration(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterConfigInfo**](ClusterConfigInfo.md)

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

# **cluster_compute_resource_get_configuration_ex**
> ComputeResourceConfigInfo cluster_compute_resource_get_configuration_ex(mo_id)

Configuration of the compute resource; applies to both standalone hosts and clusters. 

Configuration of the compute resource; applies to both standalone hosts and clusters.  For a cluster this property will return a *ClusterConfigInfoEx* object.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.compute_resource_config_info import ComputeResourceConfigInfo
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of the compute resource; applies to both standalone hosts and clusters. 
        api_response = api_instance.cluster_compute_resource_get_configuration_ex(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_configuration_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_configuration_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ComputeResourceConfigInfo**](ComputeResourceConfigInfo.md)

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

# **cluster_compute_resource_get_custom_value**
> List[CustomFieldValue] cluster_compute_resource_get_custom_value(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.cluster_compute_resource_get_custom_value(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_custom_value: %s\n" % e)
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

# **cluster_compute_resource_get_datastore**
> List[ManagedObjectReference] cluster_compute_resource_get_datastore(mo_id)

The datastore property is the subset of datastore objects in the datacenter available in this ComputeResource. 

The datastore property is the subset of datastore objects in the datacenter available in this ComputeResource.  This property is computed as the aggregate set of datastores available from all the hosts that are part of this compute resource.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The datastore property is the subset of datastore objects in the datacenter available in this ComputeResource. 
        api_response = api_instance.cluster_compute_resource_get_datastore(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_datastore: %s\n" % e)
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

# **cluster_compute_resource_get_declared_alarm_state**
> List[AlarmState] cluster_compute_resource_get_declared_alarm_state(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.cluster_compute_resource_get_declared_alarm_state(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_declared_alarm_state: %s\n" % e)
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

# **cluster_compute_resource_get_disabled_method**
> List[str] cluster_compute_resource_get_disabled_method(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.cluster_compute_resource_get_disabled_method(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_disabled_method: %s\n" % e)
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

# **cluster_compute_resource_get_drs_fault**
> List[ClusterDrsFaults] cluster_compute_resource_get_drs_fault(mo_id)

A collection of the DRS faults generated in the last DRS invocation. 

A collection of the DRS faults generated in the last DRS invocation.  Each element of the collection is the set of faults generated in one recommendation. DRS faults are generated when DRS tries to make recommendations for rule enforcement, power management, etc., and indexed in a tree structure with reason for recommendations and VM to migrate (optional) as the index keys. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_drs_faults import ClusterDrsFaults
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A collection of the DRS faults generated in the last DRS invocation. 
        api_response = api_instance.cluster_compute_resource_get_drs_fault(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_drs_fault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_drs_fault: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ClusterDrsFaults]**](ClusterDrsFaults.md)

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

# **cluster_compute_resource_get_drs_recommendation**
> List[ClusterDrsRecommendation] cluster_compute_resource_get_drs_recommendation(mo_id)

If DRS is enabled, this returns the set of recommended migrations from the DRS module. 

Deprecated as of VI API 2.5, use *ClusterComputeResource.recommendation*. vSphere 6.5 is the last version where this property is populated. Later versions of vSphere no longer populate this property.  If DRS is enabled, this returns the set of recommended migrations from the DRS module. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_drs_recommendation import ClusterDrsRecommendation
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # If DRS is enabled, this returns the set of recommended migrations from the DRS module. 
        api_response = api_instance.cluster_compute_resource_get_drs_recommendation(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_drs_recommendation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_drs_recommendation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ClusterDrsRecommendation]**](ClusterDrsRecommendation.md)

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

# **cluster_compute_resource_get_effective_role**
> List[int] cluster_compute_resource_get_effective_role(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.cluster_compute_resource_get_effective_role(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_effective_role: %s\n" % e)
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

# **cluster_compute_resource_get_environment_browser**
> ManagedObjectReference cluster_compute_resource_get_environment_browser(mo_id)

The environment browser object that identifies the environments that are supported on this compute resource. 

The environment browser object that identifies the environments that are supported on this compute resource.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The environment browser object that identifies the environments that are supported on this compute resource. 
        api_response = api_instance.cluster_compute_resource_get_environment_browser(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_environment_browser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_environment_browser: %s\n" % e)
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
**200** | Refers instance of *EnvironmentBrowser*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_get_hci_config**
> ClusterComputeResourceHCIConfigInfo cluster_compute_resource_get_hci_config(mo_id)

This is applicable to clusters which are configured using the HCI workflow and contains data related to the workflow and specification. 

This is applicable to clusters which are configured using the HCI workflow and contains data related to the workflow and specification.  ***Since:*** vSphere API 6.7.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_compute_resource_hci_config_info import ClusterComputeResourceHCIConfigInfo
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This is applicable to clusters which are configured using the HCI workflow and contains data related to the workflow and specification. 
        api_response = api_instance.cluster_compute_resource_get_hci_config(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_hci_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_hci_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterComputeResourceHCIConfigInfo**](ClusterComputeResourceHCIConfigInfo.md)

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

# **cluster_compute_resource_get_host**
> List[ManagedObjectReference] cluster_compute_resource_get_host(mo_id)

List of hosts that are part of this compute resource. 

List of hosts that are part of this compute resource.  If the compute resource is a standalone type, then this list contains just one element.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of hosts that are part of this compute resource. 
        api_response = api_instance.cluster_compute_resource_get_host(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_host: %s\n" % e)
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

# **cluster_compute_resource_get_lifecycle_managed**
> bool cluster_compute_resource_get_lifecycle_managed(mo_id)

Flag indicating whether or not the lifecycle of the compute resource is managed. 

Flag indicating whether or not the lifecycle of the compute resource is managed.  Once it is enabled, it cannot be disabled. This property can be set only at the time of creation or through the *ComputeResource.EnableLifecycleManagement* method.  ***Since:*** vSphere API 6.9.1  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Flag indicating whether or not the lifecycle of the compute resource is managed. 
        api_response = api_instance.cluster_compute_resource_get_lifecycle_managed(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_lifecycle_managed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_lifecycle_managed: %s\n" % e)
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

# **cluster_compute_resource_get_migration_history**
> List[ClusterDrsMigration] cluster_compute_resource_get_migration_history(mo_id)

The set of migration decisions that have recently been performed. 

The set of migration decisions that have recently been performed.  This list is populated only when DRS is in automatic mode. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_drs_migration import ClusterDrsMigration
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of migration decisions that have recently been performed. 
        api_response = api_instance.cluster_compute_resource_get_migration_history(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_migration_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_migration_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ClusterDrsMigration]**](ClusterDrsMigration.md)

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

# **cluster_compute_resource_get_name**
> str cluster_compute_resource_get_name(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.cluster_compute_resource_get_name(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_name: %s\n" % e)
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

# **cluster_compute_resource_get_network**
> List[ManagedObjectReference] cluster_compute_resource_get_network(mo_id)

The subset of network objects available in the datacenter that is available in this ComputeResource. 

The subset of network objects available in the datacenter that is available in this ComputeResource.  This property is computed as the aggregate set of networks available from all the hosts that are part of this compute resource.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The subset of network objects available in the datacenter that is available in this ComputeResource. 
        api_response = api_instance.cluster_compute_resource_get_network(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_network: %s\n" % e)
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

# **cluster_compute_resource_get_overall_status**
> ManagedEntityStatusEnum cluster_compute_resource_get_overall_status(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.cluster_compute_resource_get_overall_status(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_overall_status: %s\n" % e)
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

# **cluster_compute_resource_get_parent**
> ManagedObjectReference cluster_compute_resource_get_parent(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.cluster_compute_resource_get_parent(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_parent: %s\n" % e)
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

# **cluster_compute_resource_get_permission**
> List[Permission] cluster_compute_resource_get_permission(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.cluster_compute_resource_get_permission(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_permission: %s\n" % e)
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

# **cluster_compute_resource_get_recent_task**
> List[ManagedObjectReference] cluster_compute_resource_get_recent_task(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.cluster_compute_resource_get_recent_task(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_recent_task: %s\n" % e)
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

# **cluster_compute_resource_get_recommendation**
> List[ClusterRecommendation] cluster_compute_resource_get_recommendation(mo_id)

List of recommended actions for the cluster. 

List of recommended actions for the cluster.  It is possible that the current set of recommendations may be empty, either due to not having any running dynamic recommendation generation module, or since there may be no recommended actions at this time.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_recommendation import ClusterRecommendation
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of recommended actions for the cluster. 
        api_response = api_instance.cluster_compute_resource_get_recommendation(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_recommendation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_recommendation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ClusterRecommendation]**](ClusterRecommendation.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of recommendations, with each of them having one or more actions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_get_resource_pool**
> ManagedObjectReference cluster_compute_resource_get_resource_pool(mo_id)

Reference to root resource pool. 

Reference to root resource pool.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reference to root resource pool. 
        api_response = api_instance.cluster_compute_resource_get_resource_pool(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_resource_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_resource_pool: %s\n" % e)
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
**200** | Refers instance of *ResourcePool*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_get_resource_usage**
> ClusterResourceUsageSummary cluster_compute_resource_get_resource_usage(mo_id)

This API can be invoked to get the current CPU, memory and storage usage in the cluster. 

This API can be invoked to get the current CPU, memory and storage usage in the cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_resource_usage_summary import ClusterResourceUsageSummary
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This API can be invoked to get the current CPU, memory and storage usage in the cluster. 
        api_response = api_instance.cluster_compute_resource_get_resource_usage(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_resource_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_resource_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterResourceUsageSummary**](ClusterResourceUsageSummary.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of ResourceUsageSummary with following information: 1. cpuCapacityMHz: Sum of CPU capacity of all the available hosts in the    cluster in MHz. 2. cpuUsedMHz: Sum of CPU consumed in all the available hosts in the cluster    in MHz. 3. memCapacityMB: Sum of memory capacity of all the available hosts in the    cluster in MB. 4. memUsedMB: Sum of memory consumed in all the available hosts in this    cluster in MB. 5. storageCapacityMB: Total storage capacity of all the accessible datastores    in this cluster. 6. storageUsedMB: Total storage consumed in all the accessible datastores in    this cluster.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_get_summary**
> ComputeResourceSummary cluster_compute_resource_get_summary(mo_id)

Basic runtime information about a compute resource. 

Basic runtime information about a compute resource.  This information is used on summary screens and in list views. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.compute_resource_summary import ComputeResourceSummary
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Basic runtime information about a compute resource. 
        api_response = api_instance.cluster_compute_resource_get_summary(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ComputeResourceSummary**](ComputeResourceSummary.md)

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

# **cluster_compute_resource_get_summary_ex**
> ClusterComputeResourceSummary cluster_compute_resource_get_summary_ex(mo_id)

The cluster summary. 

Deprecated do not use this property. The same information could be obtained via *ComputeResource.summary*.  The cluster summary.  ***Since:*** vSphere API 7.0.1.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_compute_resource_summary import ClusterComputeResourceSummary
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The cluster summary. 
        api_response = api_instance.cluster_compute_resource_get_summary_ex(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_summary_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_summary_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterComputeResourceSummary**](ClusterComputeResourceSummary.md)

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

# **cluster_compute_resource_get_system_vms_restricted_datastores**
> List[ManagedObjectReference] cluster_compute_resource_get_system_vms_restricted_datastores(mo_id)

Retrieve all the datastores that are either listed in *ClusterSystemVMsConfigInfo.notAllowedDatastores* or are tagged with a category from *ClusterSystemVMsConfigInfo.dsTagCategoriesToExclude*. 

Retrieve all the datastores that are either listed in *ClusterSystemVMsConfigInfo.notAllowedDatastores* or are tagged with a category from *ClusterSystemVMsConfigInfo.dsTagCategoriesToExclude*.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieve all the datastores that are either listed in *ClusterSystemVMsConfigInfo.notAllowedDatastores* or are tagged with a category from *ClusterSystemVMsConfigInfo.dsTagCategoriesToExclude*. 
        api_response = api_instance.cluster_compute_resource_get_system_vms_restricted_datastores(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_system_vms_restricted_datastores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_system_vms_restricted_datastores: %s\n" % e)
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
**200** | a list of restricted datastores.  Refers instances of *Datastore*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_get_tag**
> List[Tag] cluster_compute_resource_get_tag(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.cluster_compute_resource_get_tag(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_tag: %s\n" % e)
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

# **cluster_compute_resource_get_triggered_alarm_state**
> List[AlarmState] cluster_compute_resource_get_triggered_alarm_state(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.cluster_compute_resource_get_triggered_alarm_state(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_triggered_alarm_state: %s\n" % e)
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

# **cluster_compute_resource_get_value**
> List[CustomFieldValue] cluster_compute_resource_get_value(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.cluster_compute_resource_get_value(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_get_value: %s\n" % e)
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

# **cluster_compute_resource_move_host_into_task**
> ManagedObjectReference cluster_compute_resource_move_host_into_task(mo_id, move_host_into_request_type)

Moves an existing host into a cluster. 

Moves an existing host into a cluster.  The host must be part of the same datacenter, and if the host is part of a cluster, the host must be in maintenance mode.  If the host is a stand-alone host, the stand-alone ComputeResource is removed as part of this operation.  All virtual machines associated with the host, regardless of whether or not they are running, are moved with the host into the cluster. If there are virtual machines that should not be moved, then migrate those virtual machines off the host before initiating this operation.  If the host is a stand-alone host, the cluster supports nested resource pools, and the user specifies the optional resourcePool argument, then the stand-alone host's root resource pool becomes the specified resource pool and the stand-alone host resource hierarchy is imported into the new nested resource pool. If the cluster does not support nested resource pools or the resourcePool argument is not specified, then the stand-alone host resource hierarchy is ignored.  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_host_into_request_type import MoveHostIntoRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_host_into_request_type = vmware_vi.MoveHostIntoRequestType() # MoveHostIntoRequestType | 

    try:
        # Moves an existing host into a cluster. 
        api_response = api_instance.cluster_compute_resource_move_host_into_task(mo_id, move_host_into_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_move_host_into_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_move_host_into_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_host_into_request_type** | [**MoveHostIntoRequestType**](MoveHostIntoRequestType.md)|  | 

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
**500** | ***NotSupportedHost***: if the host is running a software version that does not support clustering.  ***TooManyHosts***: if no additional hosts can be added to the cluster.  ***InvalidArgument***: if the host is not a part of the same datacenter as the cluster or if the specified resource pool is not part of the cluster or if the source and destination clusters are the same.  ***InvalidState***: if a host is already part of a cluster and is not in maintenance mode.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_move_into_task**
> ManagedObjectReference cluster_compute_resource_move_into_task(mo_id, move_into_request_type)

Moves an existing host into a cluster. 

Moves an existing host into a cluster.  The host must be part of the same datacenter, and if the host is part of a cluster, the host must be in maintenance mode.  If the host is part of a stand-alone ComputeResource, then the stand-alone ComputeResource is removed as part of this operation.  All virtual machines associated with a host, regardless of whether or not they are running, are moved with the host into the cluster. If there are virtual machines that should not be moved, then migrate those virtual machines off the host before initiating this operation.  For stand-alone hosts, the host resource pool hierarchy is discarded in this call. To preserve a host resource pools from a stand-alone host, call moveHostInt, specifying an optional resource pool. This operation is transactional only with respect to each individual host. Hosts in the set are moved sequentially and are committed, one at a time. If a failure is detected, then the method terminates with an exception. Since hosts are moved one at a time, if this operation fails while in the process of moving multiple hosts, some hosts are left unmoved.  In addition to the privileges mentioned, the user must also hold Host.Inventory.EditCluster on the host's source ComputeResource object.  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_into_request_type import MoveIntoRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_into_request_type = vmware_vi.MoveIntoRequestType() # MoveIntoRequestType | 

    try:
        # Moves an existing host into a cluster. 
        api_response = api_instance.cluster_compute_resource_move_into_task(mo_id, move_into_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_move_into_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_move_into_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_into_request_type** | [**MoveIntoRequestType**](MoveIntoRequestType.md)|  | 

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
**500** | ***NotSupportedHost***: if the host is running a software version that does not support clustering features.  ***TooManyHosts***: if no additional hosts can be added to the cluster.  ***InvalidArgument***: if one of the hosts is not part of the same datacenter as the cluster.  ***InvalidState***: if a host is already part of a cluster and is not in maintenance mode.  ***DuplicateName***: if the host is already in the cluster  ***DisallowedOperationOnFailoverHost***: if the host is being moved from a cluster and was configured as a failover host in that cluster. See *ClusterFailoverHostAdmissionControlPolicy*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_place_vm**
> PlacementResult cluster_compute_resource_place_vm(mo_id, place_vm_request_type)

This method returns a *PlacementResult* object. 

This method returns a *PlacementResult* object.  This API can be invoked to ask DRS for a set of recommendations for moving a virtual machine and its virtual disks into a cluster.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.place_vm_request_type import PlaceVmRequestType
from vmware_vi.models.placement_result import PlacementResult
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    place_vm_request_type = vmware_vi.PlaceVmRequestType() # PlaceVmRequestType | 

    try:
        # This method returns a *PlacementResult* object. 
        api_response = api_instance.cluster_compute_resource_place_vm(mo_id, place_vm_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_place_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_place_vm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **place_vm_request_type** | [**PlaceVmRequestType**](PlaceVmRequestType.md)|  | 

### Return type

[**PlacementResult**](PlacementResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidState***: if invoked on a DRS disabled cluster.  ***InvalidArgument***: in case of errors in the input \&quot;placementSpec\&quot;. The API can be used for either intra-vCenter migration or cross-vCenter migration, with different requirements for the PlacementSpec.   For intra-vCenter migration, the requirements for PlacementSpec are: - PlacementSpec.vm is required. - PlacementSpec.relocateSpec can be used to optionally specify the   target host, target datastore, or target resource pool for the migration. - PlacementSpec.hosts can be used to optionally specify a list of   compatible hosts for the incoming virtual machine. If this list is empty,   all hosts in the cluster will be considered for placement. - PlacementSpec.datastores can be used to optionally specify a list of   compatible datastores for the incoming virtual machine. If this list is   empty, all datastores connected to the hosts in the cluster will be   considered for placement. - PlacementSpec.storagePods can be used to optionally specify a list of   compatible datastore clusters for the incoming virtual machine. If this   list is empty, all datastores connected to the hosts in the cluster will   be considered for placement. &lt;!-- --&gt;   For cross-vCenter migration, the requirements for PlacementSpec are: - PlacementSpec.configSpec is required. Within the ConfigSpec, the   following elements are required if PlacementSpec.relocateSpec.host is   empty: version, cpuAllocation, memoryAllocation, numCPUs, memoryMB;   additionally, the following elements of the ConfigSpec are required if   PlacementSpec.relocateSpec.datastore is empty: files, swapPlacement,   deviceChange. - PlacementSpec.relocateSpec can be used to optionally specify the   target host, target datastore, or target resource pool for the migration. - PlacementSpec.hosts is required, if PlacementSpec.relocateSpec.host is   empty; otherwise, the selected hosts in the PlacementResult are not   guaranteed to be compatible with the incoming virtual machine. - PlacementSpec.datastores is required, if PlacementSpec.relocateSpec.datastore   is empty; otherwise, the selected datastores in the PlacementResult are   not guaranteed to be compatible with the incoming virtual machine.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_recommend_hosts_for_vm**
> List[ClusterHostRecommendation] cluster_compute_resource_recommend_hosts_for_vm(mo_id, recommend_hosts_for_vm_request_type)

Gets a recommendation for where to power on, resume, revert from powered-off state to powered on state, or to migrate a specific virtual machine. 

Deprecated as of VI API 2.5, use *Datacenter.PowerOnMultiVM_Task*. *ClusterComputeResource.RecommendHostsForVm* cannot make any recommendations if DRS cannot find the specified host in the cluster. With *Datacenter.PowerOnMultiVM_Task*, DRS attempts to migrate virtual machines and power on hosts in standby mode, given the same conditions.  Gets a recommendation for where to power on, resume, revert from powered-off state to powered on state, or to migrate a specific virtual machine.  If no host is found, an empty list is returned.  The type of operation is implied by the state of the virtual machine. Returned hosts are intended for power-on or resume if the virtual machine is powered-off or suspended. However, if the virtual machine is powered-on, the request is assumed to be for migrating a virtual machine into a DRS enabled cluster. In that case, the ResourcePool argument should be specified and the ResourcePool and the virtual machine cannot be in the same cluster.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_host_recommendation import ClusterHostRecommendation
from vmware_vi.models.recommend_hosts_for_vm_request_type import RecommendHostsForVmRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    recommend_hosts_for_vm_request_type = vmware_vi.RecommendHostsForVmRequestType() # RecommendHostsForVmRequestType | 

    try:
        # Gets a recommendation for where to power on, resume, revert from powered-off state to powered on state, or to migrate a specific virtual machine. 
        api_response = api_instance.cluster_compute_resource_recommend_hosts_for_vm(mo_id, recommend_hosts_for_vm_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_recommend_hosts_for_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_recommend_hosts_for_vm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **recommend_hosts_for_vm_request_type** | [**RecommendHostsForVmRequestType**](RecommendHostsForVmRequestType.md)|  | 

### Return type

[**List[ClusterHostRecommendation]**](ClusterHostRecommendation.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of HostRecommendation ordered by their rating.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_reconfigure_cluster_task**
> ManagedObjectReference cluster_compute_resource_reconfigure_cluster_task(mo_id, reconfigure_cluster_request_type)

Reconfigures a cluster. 

Deprecated as of VI API 2.5, use *ComputeResource.ReconfigureComputeResource_Task*.  Reconfigures a cluster.  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfigure_cluster_request_type import ReconfigureClusterRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_cluster_request_type = vmware_vi.ReconfigureClusterRequestType() # ReconfigureClusterRequestType | 

    try:
        # Reconfigures a cluster. 
        api_response = api_instance.cluster_compute_resource_reconfigure_cluster_task(mo_id, reconfigure_cluster_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_reconfigure_cluster_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_reconfigure_cluster_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_cluster_request_type** | [**ReconfigureClusterRequestType**](ReconfigureClusterRequestType.md)|  | 

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

# **cluster_compute_resource_reconfigure_compute_resource_task**
> ManagedObjectReference cluster_compute_resource_reconfigure_compute_resource_task(mo_id, reconfigure_compute_resource_request_type)

Change the compute resource configuration. 

Change the compute resource configuration.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Inventory.EditCluster 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfigure_compute_resource_request_type import ReconfigureComputeResourceRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_compute_resource_request_type = vmware_vi.ReconfigureComputeResourceRequestType() # ReconfigureComputeResourceRequestType | 

    try:
        # Change the compute resource configuration. 
        api_response = api_instance.cluster_compute_resource_reconfigure_compute_resource_task(mo_id, reconfigure_compute_resource_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_reconfigure_compute_resource_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_reconfigure_compute_resource_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_compute_resource_request_type** | [**ReconfigureComputeResourceRequestType**](ReconfigureComputeResourceRequestType.md)|  | 

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

# **cluster_compute_resource_refresh_recommendation**
> cluster_compute_resource_refresh_recommendation(mo_id)

Make DRS invoke again and return a new list of recommendations. 

Make DRS invoke again and return a new list of recommendations.  Concurrent \"refresh\" requests may be combined together and trigger only one DRS invocation.  The recommendations generated is stored at *ClusterComputeResource.recommendation*.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Inventory.EditCluster 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Make DRS invoke again and return a new list of recommendations. 
        api_instance.cluster_compute_resource_refresh_recommendation(mo_id)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_refresh_recommendation: %s\n" % e)
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

# **cluster_compute_resource_reload**
> cluster_compute_resource_reload(mo_id)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.cluster_compute_resource_reload(mo_id)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_reload: %s\n" % e)
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

# **cluster_compute_resource_rename_task**
> ManagedObjectReference cluster_compute_resource_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** Host.Inventory.RenameCluster 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.cluster_compute_resource_rename_task(mo_id, rename_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_rename_task: %s\n" % e)
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

# **cluster_compute_resource_retrieve_das_advanced_runtime_info**
> ClusterDasAdvancedRuntimeInfo cluster_compute_resource_retrieve_das_advanced_runtime_info(mo_id)

Retrieve DAS advanced runtime info for this cluster. 

Retrieve DAS advanced runtime info for this cluster.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_das_advanced_runtime_info import ClusterDasAdvancedRuntimeInfo
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieve DAS advanced runtime info for this cluster. 
        api_response = api_instance.cluster_compute_resource_retrieve_das_advanced_runtime_info(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_retrieve_das_advanced_runtime_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_retrieve_das_advanced_runtime_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ClusterDasAdvancedRuntimeInfo**](ClusterDasAdvancedRuntimeInfo.md)

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

# **cluster_compute_resource_set_crypto_mode**
> cluster_compute_resource_set_crypto_mode(mo_id, set_crypto_mode_request_type)

Set the desired encryption mode and host key for the cluster. 

Set the desired encryption mode and host key for the cluster.  The cryptoMode parameter can be used to set crypto mode policy for the cluster. Use the value *onDemand* to have each host put into the crypto safe state automatically when needed. Use the value *forceEnable* to have all hosts in the cluster put into crypto safe state immediately.  The desired host key of the cluster can also be specified optionally using the policy parameter.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Cryptographer.RegisterHost 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_crypto_mode_request_type import SetCryptoModeRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_crypto_mode_request_type = vmware_vi.SetCryptoModeRequestType() # SetCryptoModeRequestType | 

    try:
        # Set the desired encryption mode and host key for the cluster. 
        api_instance.cluster_compute_resource_set_crypto_mode(mo_id, set_crypto_mode_request_type)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_set_crypto_mode: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_crypto_mode_request_type** | [**SetCryptoModeRequestType**](SetCryptoModeRequestType.md)|  | 

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
**500** | ***InvalidRequest***: if the interface is not implemented.  ***InvalidArgument***: if one of the parameters is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_set_custom_value**
> cluster_compute_resource_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.cluster_compute_resource_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_set_custom_value: %s\n" % e)
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

# **cluster_compute_resource_stamp_all_rules_with_uuid_task**
> ManagedObjectReference cluster_compute_resource_stamp_all_rules_with_uuid_task(mo_id)

Stamp all rules in the cluster with ruleUuid. 

Stamp all rules in the cluster with ruleUuid.  If a rule has ruleUuid field set, and it has a value, leave it untouched. If rule's ruleUuid field is unset, generate a UUID and stamp the rule.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Inventory.EditCluster 

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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Stamp all rules in the cluster with ruleUuid. 
        api_response = api_instance.cluster_compute_resource_stamp_all_rules_with_uuid_task(mo_id)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_stamp_all_rules_with_uuid_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_stamp_all_rules_with_uuid_task: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_compute_resource_validate_hci_configuration**
> List[ClusterComputeResourceValidationResultBase] cluster_compute_resource_validate_hci_configuration(mo_id, validate_hci_configuration_request_type)

Validate HCI configuration in pre-configure and post-configure use-cases. 

Validate HCI configuration in pre-configure and post-configure use-cases. 1. pre-configure use-case: Validates the HCI configuration to be applied on    the cluster. A successful validation in this case means the HCIConfigSpec    can be applied without errors on the cluster using    *ClusterComputeResource.ConfigureHCI_Task* or    *ClusterComputeResource.ExtendHCI_Task*      These are the things the API validates:    1. When providing a set of physical adapters in the       *ClusterComputeResourceHCIConfigSpec.dvsProf* argument,       the API validates that all the adapters should be present on all the       hosts to be validated. The adapters should either be unmapped or mapped       to the same vSwitch across hosts. In addition to this, if the adapters       are connected to a *DistributedVirtualSwitch*, it should be       exactly the same way as specified in the       *ClusterComputeResourceHCIConfigSpec.dvsProf* or in the       *ClusterComputeResourceHCIConfigInfo.dvsSetting*.    2. The API will also validate that the ESXi versions of the hosts are       compatible with the version of the *DistributedVirtualSwitch*       being created. 2. post-configure case: Validate the cluster has been configured correctly    as per the *ClusterComputeResourceHCIConfigInfo* for the    cluster. In this case, the API should be invoked with both params omitted    as the intent is to validate all hosts in the cluster using the existing    *ClusterComputeResourceHCIConfigInfo*     ***Since:*** vSphere API 6.7.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.cluster_compute_resource_validation_result_base import ClusterComputeResourceValidationResultBase
from vmware_vi.models.validate_hci_configuration_request_type import ValidateHCIConfigurationRequestType
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
    api_instance = vmware_vi.ClusterComputeResourceApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    validate_hci_configuration_request_type = vmware_vi.ValidateHCIConfigurationRequestType() # ValidateHCIConfigurationRequestType | 

    try:
        # Validate HCI configuration in pre-configure and post-configure use-cases. 
        api_response = api_instance.cluster_compute_resource_validate_hci_configuration(mo_id, validate_hci_configuration_request_type)
        print("The response of ClusterComputeResourceApi->cluster_compute_resource_validate_hci_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterComputeResourceApi->cluster_compute_resource_validate_hci_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **validate_hci_configuration_request_type** | [**ValidateHCIConfigurationRequestType**](ValidateHCIConfigurationRequestType.md)|  | 

### Return type

[**List[ClusterComputeResourceValidationResultBase]**](ClusterComputeResourceValidationResultBase.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of configuration errors. A non-empty list indicates validation has failed.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

