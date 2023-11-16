# ArrayOfVirtualMachineWindowsQuiesceSpec

A boxed array of *VirtualMachineWindowsQuiesceSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineWindowsQuiesceSpec]**](VirtualMachineWindowsQuiesceSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_windows_quiesce_spec import ArrayOfVirtualMachineWindowsQuiesceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineWindowsQuiesceSpec from a JSON string
array_of_virtual_machine_windows_quiesce_spec_instance = ArrayOfVirtualMachineWindowsQuiesceSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineWindowsQuiesceSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_windows_quiesce_spec_dict = array_of_virtual_machine_windows_quiesce_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineWindowsQuiesceSpec from a dict
array_of_virtual_machine_windows_quiesce_spec_form_dict = array_of_virtual_machine_windows_quiesce_spec.from_dict(array_of_virtual_machine_windows_quiesce_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


