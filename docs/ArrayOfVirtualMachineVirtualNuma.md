# ArrayOfVirtualMachineVirtualNuma

A boxed array of *VirtualMachineVirtualNuma*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVirtualNuma]**](VirtualMachineVirtualNuma.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_virtual_numa import ArrayOfVirtualMachineVirtualNuma

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVirtualNuma from a JSON string
array_of_virtual_machine_virtual_numa_instance = ArrayOfVirtualMachineVirtualNuma.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVirtualNuma.to_json()

# convert the object into a dict
array_of_virtual_machine_virtual_numa_dict = array_of_virtual_machine_virtual_numa_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVirtualNuma from a dict
array_of_virtual_machine_virtual_numa_form_dict = array_of_virtual_machine_virtual_numa.from_dict(array_of_virtual_machine_virtual_numa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


