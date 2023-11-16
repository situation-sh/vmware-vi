# ArrayOfUnlicensedVirtualMachinesFoundEvent

A boxed array of *UnlicensedVirtualMachinesFoundEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UnlicensedVirtualMachinesFoundEvent]**](UnlicensedVirtualMachinesFoundEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_unlicensed_virtual_machines_found_event import ArrayOfUnlicensedVirtualMachinesFoundEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnlicensedVirtualMachinesFoundEvent from a JSON string
array_of_unlicensed_virtual_machines_found_event_instance = ArrayOfUnlicensedVirtualMachinesFoundEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUnlicensedVirtualMachinesFoundEvent.to_json()

# convert the object into a dict
array_of_unlicensed_virtual_machines_found_event_dict = array_of_unlicensed_virtual_machines_found_event_instance.to_dict()
# create an instance of ArrayOfUnlicensedVirtualMachinesFoundEvent from a dict
array_of_unlicensed_virtual_machines_found_event_form_dict = array_of_unlicensed_virtual_machines_found_event.from_dict(array_of_unlicensed_virtual_machines_found_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


