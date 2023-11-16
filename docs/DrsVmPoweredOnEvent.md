# DrsVmPoweredOnEvent

This event records when a virtual machine is powered on by DRS.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_vm_powered_on_event import DrsVmPoweredOnEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsVmPoweredOnEvent from a JSON string
drs_vm_powered_on_event_instance = DrsVmPoweredOnEvent.from_json(json)
# print the JSON string representation of the object
print DrsVmPoweredOnEvent.to_json()

# convert the object into a dict
drs_vm_powered_on_event_dict = drs_vm_powered_on_event_instance.to_dict()
# create an instance of DrsVmPoweredOnEvent from a dict
drs_vm_powered_on_event_form_dict = drs_vm_powered_on_event.from_dict(drs_vm_powered_on_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


