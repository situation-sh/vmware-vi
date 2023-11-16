# ArrayOfHostPatchManagerStatus

A boxed array of *HostPatchManagerStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPatchManagerStatus]**](HostPatchManagerStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_patch_manager_status import ArrayOfHostPatchManagerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPatchManagerStatus from a JSON string
array_of_host_patch_manager_status_instance = ArrayOfHostPatchManagerStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPatchManagerStatus.to_json()

# convert the object into a dict
array_of_host_patch_manager_status_dict = array_of_host_patch_manager_status_instance.to_dict()
# create an instance of ArrayOfHostPatchManagerStatus from a dict
array_of_host_patch_manager_status_form_dict = array_of_host_patch_manager_status.from_dict(array_of_host_patch_manager_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


