# StorageDrsVmConfigInfo

Storage DRS configuration for a single virtual machine.  This makes it possible to override the default behavior for an individual virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**enabled** | **bool** | Flag to indicate whether or not VirtualCenter is allowed to perform any storage migration or initial placement recommendations for this virtual machine on the pod *StoragePod*.  If this flag is false, the virtual machine is effectively excluded from storage DRS.  If no individual DRS specification exists for a virtual machine, this property defaults to true.  ***Since:*** vSphere API 5.0  | [optional] 
**behavior** | **str** | Specifies the particular storage DRS behavior for this virtual machine.  For supported values, see *StorageDrsPodConfigInfoBehavior_enum*.  ***Since:*** vSphere API 5.0  | [optional] 
**intra_vm_affinity** | **bool** | Specifies whether or not to have the affinity rule for the virtual disks of this virtual machine.  If not set, the default value is derived from the pod-wide default *StorageDrsPodConfigInfo.defaultIntraVmAffinity*.  ***Since:*** vSphere API 5.0  | [optional] 
**intra_vm_anti_affinity** | [**VirtualDiskAntiAffinityRuleSpec**](VirtualDiskAntiAffinityRuleSpec.md) |  | [optional] 
**virtual_disk_rules** | [**List[VirtualDiskRuleSpec]**](VirtualDiskRuleSpec.md) | List of the virtual disk rules that can be overridden/created.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_vm_config_info import StorageDrsVmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsVmConfigInfo from a JSON string
storage_drs_vm_config_info_instance = StorageDrsVmConfigInfo.from_json(json)
# print the JSON string representation of the object
print StorageDrsVmConfigInfo.to_json()

# convert the object into a dict
storage_drs_vm_config_info_dict = storage_drs_vm_config_info_instance.to_dict()
# create an instance of StorageDrsVmConfigInfo from a dict
storage_drs_vm_config_info_form_dict = storage_drs_vm_config_info.from_dict(storage_drs_vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


