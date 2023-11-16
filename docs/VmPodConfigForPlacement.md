# VmPodConfigForPlacement

Initial VM configuration for the specified pod.  This configuration will be saved to the pod config *StorageDrsConfigInfo* when the placement recommendations are applied.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk** | [**List[PodDiskLocator]**](PodDiskLocator.md) | Array of PodDiskLocator objects.  ***Since:*** vSphere API 5.0  | [optional] 
**vm_config** | [**StorageDrsVmConfigInfo**](StorageDrsVmConfigInfo.md) |  | [optional] 
**inter_vm_rule** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) | The initial interVmRules that should during placement of this virtual machine.  It may not always be possible to specify that the virtual machine being placed is part of the rule because the virtual machine may not have been created yet. So for simplicity, we assume the virtual machine being placed is always implicitly part of any rule specified. It will be explicitly added to the rule before it is saved to the pod config.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_pod_config_for_placement import VmPodConfigForPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of VmPodConfigForPlacement from a JSON string
vm_pod_config_for_placement_instance = VmPodConfigForPlacement.from_json(json)
# print the JSON string representation of the object
print VmPodConfigForPlacement.to_json()

# convert the object into a dict
vm_pod_config_for_placement_dict = vm_pod_config_for_placement_instance.to_dict()
# create an instance of VmPodConfigForPlacement from a dict
vm_pod_config_for_placement_form_dict = vm_pod_config_for_placement.from_dict(vm_pod_config_for_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


