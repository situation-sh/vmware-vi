# VmMaxFTRestartCountReached

This event is fired when FT VM reached the max restart count  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_max_ft_restart_count_reached import VmMaxFTRestartCountReached

# TODO update the JSON string below
json = "{}"
# create an instance of VmMaxFTRestartCountReached from a JSON string
vm_max_ft_restart_count_reached_instance = VmMaxFTRestartCountReached.from_json(json)
# print the JSON string representation of the object
print VmMaxFTRestartCountReached.to_json()

# convert the object into a dict
vm_max_ft_restart_count_reached_dict = vm_max_ft_restart_count_reached_instance.to_dict()
# create an instance of VmMaxFTRestartCountReached from a dict
vm_max_ft_restart_count_reached_form_dict = vm_max_ft_restart_count_reached.from_dict(vm_max_ft_restart_count_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


