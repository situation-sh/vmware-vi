# ArrayOfVmPowerOffOnIsolationEvent

A boxed array of *VmPowerOffOnIsolationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPowerOffOnIsolationEvent]**](VmPowerOffOnIsolationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_power_off_on_isolation_event import ArrayOfVmPowerOffOnIsolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPowerOffOnIsolationEvent from a JSON string
array_of_vm_power_off_on_isolation_event_instance = ArrayOfVmPowerOffOnIsolationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPowerOffOnIsolationEvent.to_json()

# convert the object into a dict
array_of_vm_power_off_on_isolation_event_dict = array_of_vm_power_off_on_isolation_event_instance.to_dict()
# create an instance of ArrayOfVmPowerOffOnIsolationEvent from a dict
array_of_vm_power_off_on_isolation_event_form_dict = array_of_vm_power_off_on_isolation_event.from_dict(array_of_vm_power_off_on_isolation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


