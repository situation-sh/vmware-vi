# StorageDrsPodConfigSpec

The *StorageDrsPodConfigSpec* data object provides a set of update specifications for pod-wide storage DRS configuration.  To support incremental changes, these properties are all optional.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not storage DRS is enabled.  ***Since:*** vSphere API 5.0  | [optional] 
**io_load_balance_enabled** | **bool** | Flag indicating whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.  ***Since:*** vSphere API 5.0  | [optional] 
**default_vm_behavior** | **str** | Specifies the pod-wide default storage DRS behavior for virtual machines.  For currently supported storage DRS behavior, see *StorageDrsPodConfigInfoBehavior_enum*. You can override the default behavior for a virtual machine by using the *StorageDrsVmConfigInfo* object.  ***Since:*** vSphere API 5.0  | [optional] 
**load_balance_interval** | **int** | Specify the interval that storage DRS runs to load balance among datastores within a storage pod.  ***Since:*** vSphere API 5.0  | [optional] 
**default_intra_vm_affinity** | **bool** | Specifies whether or not each virtual machine in this pod should have its virtual disks on the same datastore by default.  ***Since:*** vSphere API 5.0  | [optional] 
**space_load_balance_config** | [**StorageDrsSpaceLoadBalanceConfig**](StorageDrsSpaceLoadBalanceConfig.md) |  | [optional] 
**io_load_balance_config** | [**StorageDrsIoLoadBalanceConfig**](StorageDrsIoLoadBalanceConfig.md) |  | [optional] 
**automation_overrides** | [**StorageDrsAutomationConfig**](StorageDrsAutomationConfig.md) |  | [optional] 
**rule** | [**List[ClusterRuleSpec]**](ClusterRuleSpec.md) | Changes to the set of rules.  ***Since:*** vSphere API 5.0  | [optional] 
**option** | [**List[StorageDrsOptionSpec]**](StorageDrsOptionSpec.md) | Changes to advance settings.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_pod_config_spec import StorageDrsPodConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsPodConfigSpec from a JSON string
storage_drs_pod_config_spec_instance = StorageDrsPodConfigSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsPodConfigSpec.to_json()

# convert the object into a dict
storage_drs_pod_config_spec_dict = storage_drs_pod_config_spec_instance.to_dict()
# create an instance of StorageDrsPodConfigSpec from a dict
storage_drs_pod_config_spec_form_dict = storage_drs_pod_config_spec.from_dict(storage_drs_pod_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


