# VmDasUpdateOkEvent

This event records that HA agents have been updated with the current state of the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_das_update_ok_event import VmDasUpdateOkEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDasUpdateOkEvent from a JSON string
vm_das_update_ok_event_instance = VmDasUpdateOkEvent.from_json(json)
# print the JSON string representation of the object
print VmDasUpdateOkEvent.to_json()

# convert the object into a dict
vm_das_update_ok_event_dict = vm_das_update_ok_event_instance.to_dict()
# create an instance of VmDasUpdateOkEvent from a dict
vm_das_update_ok_event_form_dict = vm_das_update_ok_event.from_dict(vm_das_update_ok_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


