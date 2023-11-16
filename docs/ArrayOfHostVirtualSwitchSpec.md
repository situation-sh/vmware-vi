# ArrayOfHostVirtualSwitchSpec

A boxed array of *HostVirtualSwitchSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualSwitchSpec]**](HostVirtualSwitchSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_switch_spec import ArrayOfHostVirtualSwitchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualSwitchSpec from a JSON string
array_of_host_virtual_switch_spec_instance = ArrayOfHostVirtualSwitchSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualSwitchSpec.to_json()

# convert the object into a dict
array_of_host_virtual_switch_spec_dict = array_of_host_virtual_switch_spec_instance.to_dict()
# create an instance of ArrayOfHostVirtualSwitchSpec from a dict
array_of_host_virtual_switch_spec_form_dict = array_of_host_virtual_switch_spec.from_dict(array_of_host_virtual_switch_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


