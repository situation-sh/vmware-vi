# VmConfigMissingEvent

This event records if the configuration file can not be found. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_config_missing_event import VmConfigMissingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigMissingEvent from a JSON string
vm_config_missing_event_instance = VmConfigMissingEvent.from_json(json)
# print the JSON string representation of the object
print VmConfigMissingEvent.to_json()

# convert the object into a dict
vm_config_missing_event_dict = vm_config_missing_event_instance.to_dict()
# create an instance of VmConfigMissingEvent from a dict
vm_config_missing_event_form_dict = vm_config_missing_event.from_dict(vm_config_missing_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


