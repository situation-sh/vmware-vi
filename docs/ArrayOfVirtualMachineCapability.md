# ArrayOfVirtualMachineCapability

A boxed array of *VirtualMachineCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCapability]**](VirtualMachineCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_capability import ArrayOfVirtualMachineCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCapability from a JSON string
array_of_virtual_machine_capability_instance = ArrayOfVirtualMachineCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCapability.to_json()

# convert the object into a dict
array_of_virtual_machine_capability_dict = array_of_virtual_machine_capability_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCapability from a dict
array_of_virtual_machine_capability_form_dict = array_of_virtual_machine_capability.from_dict(array_of_virtual_machine_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


