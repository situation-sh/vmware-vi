# ArrayOfVmPodConfigForPlacement

A boxed array of *VmPodConfigForPlacement*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPodConfigForPlacement]**](VmPodConfigForPlacement.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_pod_config_for_placement import ArrayOfVmPodConfigForPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPodConfigForPlacement from a JSON string
array_of_vm_pod_config_for_placement_instance = ArrayOfVmPodConfigForPlacement.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPodConfigForPlacement.to_json()

# convert the object into a dict
array_of_vm_pod_config_for_placement_dict = array_of_vm_pod_config_for_placement_instance.to_dict()
# create an instance of ArrayOfVmPodConfigForPlacement from a dict
array_of_vm_pod_config_for_placement_form_dict = array_of_vm_pod_config_for_placement.from_dict(array_of_vm_pod_config_for_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


