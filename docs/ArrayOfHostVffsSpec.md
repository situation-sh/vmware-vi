# ArrayOfHostVffsSpec

A boxed array of *HostVffsSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVffsSpec]**](HostVffsSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vffs_spec import ArrayOfHostVffsSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVffsSpec from a JSON string
array_of_host_vffs_spec_instance = ArrayOfHostVffsSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVffsSpec.to_json()

# convert the object into a dict
array_of_host_vffs_spec_dict = array_of_host_vffs_spec_instance.to_dict()
# create an instance of ArrayOfHostVffsSpec from a dict
array_of_host_vffs_spec_form_dict = array_of_host_vffs_spec.from_dict(array_of_host_vffs_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


