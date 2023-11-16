# ArrayOfVirtualMachineInstantCloneSpec

A boxed array of *VirtualMachineInstantCloneSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineInstantCloneSpec]**](VirtualMachineInstantCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_instant_clone_spec import ArrayOfVirtualMachineInstantCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineInstantCloneSpec from a JSON string
array_of_virtual_machine_instant_clone_spec_instance = ArrayOfVirtualMachineInstantCloneSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineInstantCloneSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_instant_clone_spec_dict = array_of_virtual_machine_instant_clone_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineInstantCloneSpec from a dict
array_of_virtual_machine_instant_clone_spec_form_dict = array_of_virtual_machine_instant_clone_spec.from_dict(array_of_virtual_machine_instant_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


