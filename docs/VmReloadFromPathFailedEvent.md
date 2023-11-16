# VmReloadFromPathFailedEvent

This event records that a virtual machine reload from a new configuration path failed.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_path** | **str** |  | 

## Example

```python
from vmware_vi.models.vm_reload_from_path_failed_event import VmReloadFromPathFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmReloadFromPathFailedEvent from a JSON string
vm_reload_from_path_failed_event_instance = VmReloadFromPathFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmReloadFromPathFailedEvent.to_json()

# convert the object into a dict
vm_reload_from_path_failed_event_dict = vm_reload_from_path_failed_event_instance.to_dict()
# create an instance of VmReloadFromPathFailedEvent from a dict
vm_reload_from_path_failed_event_form_dict = vm_reload_from_path_failed_event.from_dict(vm_reload_from_path_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


