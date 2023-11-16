# ArrayOfVmReconfiguredEvent

A boxed array of *VmReconfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmReconfiguredEvent]**](VmReconfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_reconfigured_event import ArrayOfVmReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmReconfiguredEvent from a JSON string
array_of_vm_reconfigured_event_instance = ArrayOfVmReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmReconfiguredEvent.to_json()

# convert the object into a dict
array_of_vm_reconfigured_event_dict = array_of_vm_reconfigured_event_instance.to_dict()
# create an instance of ArrayOfVmReconfiguredEvent from a dict
array_of_vm_reconfigured_event_form_dict = array_of_vm_reconfigured_event.from_dict(array_of_vm_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


