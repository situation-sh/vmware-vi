# VmReloadFromPathEvent

This event records that a virtual machine was successfully reloaded from a new configuration path.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_path** | **str** |  | 

## Example

```python
from vmware_vi.models.vm_reload_from_path_event import VmReloadFromPathEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmReloadFromPathEvent from a JSON string
vm_reload_from_path_event_instance = VmReloadFromPathEvent.from_json(json)
# print the JSON string representation of the object
print VmReloadFromPathEvent.to_json()

# convert the object into a dict
vm_reload_from_path_event_dict = vm_reload_from_path_event_instance.to_dict()
# create an instance of VmReloadFromPathEvent from a dict
vm_reload_from_path_event_form_dict = vm_reload_from_path_event.from_dict(vm_reload_from_path_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


