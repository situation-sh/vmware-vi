# ArrayOfHostVirtualSwitch

A boxed array of *HostVirtualSwitch*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualSwitch]**](HostVirtualSwitch.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_switch import ArrayOfHostVirtualSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualSwitch from a JSON string
array_of_host_virtual_switch_instance = ArrayOfHostVirtualSwitch.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualSwitch.to_json()

# convert the object into a dict
array_of_host_virtual_switch_dict = array_of_host_virtual_switch_instance.to_dict()
# create an instance of ArrayOfHostVirtualSwitch from a dict
array_of_host_virtual_switch_form_dict = array_of_host_virtual_switch.from_dict(array_of_host_virtual_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


