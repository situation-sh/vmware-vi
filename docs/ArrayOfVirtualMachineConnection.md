# ArrayOfVirtualMachineConnection

A boxed array of *VirtualMachineConnection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConnection]**](VirtualMachineConnection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_connection import ArrayOfVirtualMachineConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConnection from a JSON string
array_of_virtual_machine_connection_instance = ArrayOfVirtualMachineConnection.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConnection.to_json()

# convert the object into a dict
array_of_virtual_machine_connection_dict = array_of_virtual_machine_connection_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConnection from a dict
array_of_virtual_machine_connection_form_dict = array_of_virtual_machine_connection.from_dict(array_of_virtual_machine_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


