# ArrayOfVmPrimaryFailoverEvent

A boxed array of *VmPrimaryFailoverEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPrimaryFailoverEvent]**](VmPrimaryFailoverEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_primary_failover_event import ArrayOfVmPrimaryFailoverEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPrimaryFailoverEvent from a JSON string
array_of_vm_primary_failover_event_instance = ArrayOfVmPrimaryFailoverEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPrimaryFailoverEvent.to_json()

# convert the object into a dict
array_of_vm_primary_failover_event_dict = array_of_vm_primary_failover_event_instance.to_dict()
# create an instance of ArrayOfVmPrimaryFailoverEvent from a dict
array_of_vm_primary_failover_event_form_dict = array_of_vm_primary_failover_event.from_dict(array_of_vm_primary_failover_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


