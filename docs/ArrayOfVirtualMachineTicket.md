# ArrayOfVirtualMachineTicket

A boxed array of *VirtualMachineTicket*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineTicket]**](VirtualMachineTicket.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_ticket import ArrayOfVirtualMachineTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineTicket from a JSON string
array_of_virtual_machine_ticket_instance = ArrayOfVirtualMachineTicket.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineTicket.to_json()

# convert the object into a dict
array_of_virtual_machine_ticket_dict = array_of_virtual_machine_ticket_instance.to_dict()
# create an instance of ArrayOfVirtualMachineTicket from a dict
array_of_virtual_machine_ticket_form_dict = array_of_virtual_machine_ticket.from_dict(array_of_virtual_machine_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


