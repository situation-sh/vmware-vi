# ArrayOfHostVirtualNicSpec

A boxed array of *HostVirtualNicSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualNicSpec]**](HostVirtualNicSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_nic_spec import ArrayOfHostVirtualNicSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualNicSpec from a JSON string
array_of_host_virtual_nic_spec_instance = ArrayOfHostVirtualNicSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualNicSpec.to_json()

# convert the object into a dict
array_of_host_virtual_nic_spec_dict = array_of_host_virtual_nic_spec_instance.to_dict()
# create an instance of ArrayOfHostVirtualNicSpec from a dict
array_of_host_virtual_nic_spec_form_dict = array_of_host_virtual_nic_spec.from_dict(array_of_host_virtual_nic_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


