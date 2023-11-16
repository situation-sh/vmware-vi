# VmDateRolledBackEvent

This event records when the VirtualCenter server date rolled back. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_date_rolled_back_event import VmDateRolledBackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDateRolledBackEvent from a JSON string
vm_date_rolled_back_event_instance = VmDateRolledBackEvent.from_json(json)
# print the JSON string representation of the object
print VmDateRolledBackEvent.to_json()

# convert the object into a dict
vm_date_rolled_back_event_dict = vm_date_rolled_back_event_instance.to_dict()
# create an instance of VmDateRolledBackEvent from a dict
vm_date_rolled_back_event_form_dict = vm_date_rolled_back_event.from_dict(vm_date_rolled_back_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


