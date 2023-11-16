# ArrayOfVirtualMachineMessage

A boxed array of *VirtualMachineMessage*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMessage]**](VirtualMachineMessage.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_message import ArrayOfVirtualMachineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMessage from a JSON string
array_of_virtual_machine_message_instance = ArrayOfVirtualMachineMessage.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMessage.to_json()

# convert the object into a dict
array_of_virtual_machine_message_dict = array_of_virtual_machine_message_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMessage from a dict
array_of_virtual_machine_message_form_dict = array_of_virtual_machine_message.from_dict(array_of_virtual_machine_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


