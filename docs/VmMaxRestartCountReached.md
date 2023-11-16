# VmMaxRestartCountReached

This event is fired when the VM reached the max restart count  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_max_restart_count_reached import VmMaxRestartCountReached

# TODO update the JSON string below
json = "{}"
# create an instance of VmMaxRestartCountReached from a JSON string
vm_max_restart_count_reached_instance = VmMaxRestartCountReached.from_json(json)
# print the JSON string representation of the object
print VmMaxRestartCountReached.to_json()

# convert the object into a dict
vm_max_restart_count_reached_dict = vm_max_restart_count_reached_instance.to_dict()
# create an instance of VmMaxRestartCountReached from a dict
vm_max_restart_count_reached_form_dict = vm_max_restart_count_reached.from_dict(vm_max_restart_count_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


