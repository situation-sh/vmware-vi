# ArrayOfVirtualMachineCloneSpec

A boxed array of *VirtualMachineCloneSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCloneSpec]**](VirtualMachineCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_clone_spec import ArrayOfVirtualMachineCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCloneSpec from a JSON string
array_of_virtual_machine_clone_spec_instance = ArrayOfVirtualMachineCloneSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCloneSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_clone_spec_dict = array_of_virtual_machine_clone_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCloneSpec from a dict
array_of_virtual_machine_clone_spec_form_dict = array_of_virtual_machine_clone_spec.from_dict(array_of_virtual_machine_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


