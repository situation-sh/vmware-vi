# ArrayOfVirtualMachineConfigInfoOverheadInfo

A boxed array of *VirtualMachineConfigInfoOverheadInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConfigInfoOverheadInfo]**](VirtualMachineConfigInfoOverheadInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_config_info_overhead_info import ArrayOfVirtualMachineConfigInfoOverheadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConfigInfoOverheadInfo from a JSON string
array_of_virtual_machine_config_info_overhead_info_instance = ArrayOfVirtualMachineConfigInfoOverheadInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConfigInfoOverheadInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_config_info_overhead_info_dict = array_of_virtual_machine_config_info_overhead_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConfigInfoOverheadInfo from a dict
array_of_virtual_machine_config_info_overhead_info_form_dict = array_of_virtual_machine_config_info_overhead_info.from_dict(array_of_virtual_machine_config_info_overhead_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


