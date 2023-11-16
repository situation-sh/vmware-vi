# ArrayOfVirtualMachineMksConnection

A boxed array of *VirtualMachineMksConnection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMksConnection]**](VirtualMachineMksConnection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_mks_connection import ArrayOfVirtualMachineMksConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMksConnection from a JSON string
array_of_virtual_machine_mks_connection_instance = ArrayOfVirtualMachineMksConnection.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMksConnection.to_json()

# convert the object into a dict
array_of_virtual_machine_mks_connection_dict = array_of_virtual_machine_mks_connection_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMksConnection from a dict
array_of_virtual_machine_mks_connection_form_dict = array_of_virtual_machine_mks_connection.from_dict(array_of_virtual_machine_mks_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


