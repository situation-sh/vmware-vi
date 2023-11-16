# ArrayOfHostOpaqueSwitch

A boxed array of *HostOpaqueSwitch*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostOpaqueSwitch]**](HostOpaqueSwitch.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_opaque_switch import ArrayOfHostOpaqueSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostOpaqueSwitch from a JSON string
array_of_host_opaque_switch_instance = ArrayOfHostOpaqueSwitch.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostOpaqueSwitch.to_json()

# convert the object into a dict
array_of_host_opaque_switch_dict = array_of_host_opaque_switch_instance.to_dict()
# create an instance of ArrayOfHostOpaqueSwitch from a dict
array_of_host_opaque_switch_form_dict = array_of_host_opaque_switch.from_dict(array_of_host_opaque_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


