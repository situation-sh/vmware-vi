# ArrayOfVirtualMachineConfigSpec

A boxed array of *VirtualMachineConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConfigSpec]**](VirtualMachineConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_config_spec import ArrayOfVirtualMachineConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConfigSpec from a JSON string
array_of_virtual_machine_config_spec_instance = ArrayOfVirtualMachineConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConfigSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_config_spec_dict = array_of_virtual_machine_config_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConfigSpec from a dict
array_of_virtual_machine_config_spec_form_dict = array_of_virtual_machine_config_spec.from_dict(array_of_virtual_machine_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


