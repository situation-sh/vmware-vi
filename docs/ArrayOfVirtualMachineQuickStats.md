# ArrayOfVirtualMachineQuickStats

A boxed array of *VirtualMachineQuickStats*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineQuickStats]**](VirtualMachineQuickStats.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_quick_stats import ArrayOfVirtualMachineQuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineQuickStats from a JSON string
array_of_virtual_machine_quick_stats_instance = ArrayOfVirtualMachineQuickStats.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineQuickStats.to_json()

# convert the object into a dict
array_of_virtual_machine_quick_stats_dict = array_of_virtual_machine_quick_stats_instance.to_dict()
# create an instance of ArrayOfVirtualMachineQuickStats from a dict
array_of_virtual_machine_quick_stats_form_dict = array_of_virtual_machine_quick_stats.from_dict(array_of_virtual_machine_quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


