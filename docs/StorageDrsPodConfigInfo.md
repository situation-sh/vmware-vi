# StorageDrsPodConfigInfo

The *StorageDrsPodConfigInfo* data object contains pod-wide configuration information for the storage DRS service.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not storage DRS is enabled.  ***Since:*** vSphere API 5.0  | 
**io_load_balance_enabled** | **bool** | Flag indicating whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.  ***Since:*** vSphere API 5.0  | 
**default_vm_behavior** | **str** | Specifies the pod-wide default storage DRS behavior for virtual machines.  For currently supported storage DRS behavior, see *StorageDrsPodConfigInfoBehavior_enum*. You can override the default behavior for a virtual machine by using the *StorageDrsVmConfigInfo* object.  ***Since:*** vSphere API 5.0  | 
**load_balance_interval** | **int** | Specify the interval that storage DRS runs to load balance among datastores within a storage pod.  Unit: minute. The valid values are from 60 (1 hour) to 43200 (30 days). If not specified, the default value is 480 (8 hours).  ***Since:*** vSphere API 5.0  | [optional] 
**default_intra_vm_affinity** | **bool** | Specifies whether or not each virtual machine in this pod should have its virtual disks on the same datastore by default.  If set to true, virtual machines will have all their virtual disks on the same datastore. If set to false, the virtual disks of a virtual machine may or may not be placed on the same datastore. If not set, the default value is true. You can override the default behavior for a virtual machine by using the *StorageDrsVmConfigInfo* object.  ***Since:*** vSphere API 5.0  | [optional] 
**space_load_balance_config** | [**StorageDrsSpaceLoadBalanceConfig**](StorageDrsSpaceLoadBalanceConfig.md) |  | [optional] 
**io_load_balance_config** | [**StorageDrsIoLoadBalanceConfig**](StorageDrsIoLoadBalanceConfig.md) |  | [optional] 
**automation_overrides** | [**StorageDrsAutomationConfig**](StorageDrsAutomationConfig.md) |  | [optional] 
**rule** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) | Pod-wide rules.  ***Since:*** vSphere API 5.0  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Advanced settings.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_pod_config_info import StorageDrsPodConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsPodConfigInfo from a JSON string
storage_drs_pod_config_info_instance = StorageDrsPodConfigInfo.from_json(json)
# print the JSON string representation of the object
print StorageDrsPodConfigInfo.to_json()

# convert the object into a dict
storage_drs_pod_config_info_dict = storage_drs_pod_config_info_instance.to_dict()
# create an instance of StorageDrsPodConfigInfo from a dict
storage_drs_pod_config_info_form_dict = storage_drs_pod_config_info.from_dict(storage_drs_pod_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


