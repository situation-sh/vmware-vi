# ArrayOfVirtualMachineProfileSpec

A boxed array of *VirtualMachineProfileSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_profile_spec import ArrayOfVirtualMachineProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineProfileSpec from a JSON string
array_of_virtual_machine_profile_spec_instance = ArrayOfVirtualMachineProfileSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineProfileSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_profile_spec_dict = array_of_virtual_machine_profile_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineProfileSpec from a dict
array_of_virtual_machine_profile_spec_form_dict = array_of_virtual_machine_profile_spec.from_dict(array_of_virtual_machine_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


