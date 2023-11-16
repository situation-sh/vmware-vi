# ArrayOfUnlicensedVirtualMachinesEvent

A boxed array of *UnlicensedVirtualMachinesEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UnlicensedVirtualMachinesEvent]**](UnlicensedVirtualMachinesEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_unlicensed_virtual_machines_event import ArrayOfUnlicensedVirtualMachinesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnlicensedVirtualMachinesEvent from a JSON string
array_of_unlicensed_virtual_machines_event_instance = ArrayOfUnlicensedVirtualMachinesEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUnlicensedVirtualMachinesEvent.to_json()

# convert the object into a dict
array_of_unlicensed_virtual_machines_event_dict = array_of_unlicensed_virtual_machines_event_instance.to_dict()
# create an instance of ArrayOfUnlicensedVirtualMachinesEvent from a dict
array_of_unlicensed_virtual_machines_event_form_dict = array_of_unlicensed_virtual_machines_event.from_dict(array_of_unlicensed_virtual_machines_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


