# ArrayOfVirtualMachineDynamicPassthroughInfo

A boxed array of *VirtualMachineDynamicPassthroughInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineDynamicPassthroughInfo]**](VirtualMachineDynamicPassthroughInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_dynamic_passthrough_info import ArrayOfVirtualMachineDynamicPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineDynamicPassthroughInfo from a JSON string
array_of_virtual_machine_dynamic_passthrough_info_instance = ArrayOfVirtualMachineDynamicPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineDynamicPassthroughInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_dynamic_passthrough_info_dict = array_of_virtual_machine_dynamic_passthrough_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineDynamicPassthroughInfo from a dict
array_of_virtual_machine_dynamic_passthrough_info_form_dict = array_of_virtual_machine_dynamic_passthrough_info.from_dict(array_of_virtual_machine_dynamic_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


