# ArrayOfHostPatchManagerResult

A boxed array of *HostPatchManagerResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPatchManagerResult]**](HostPatchManagerResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_patch_manager_result import ArrayOfHostPatchManagerResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPatchManagerResult from a JSON string
array_of_host_patch_manager_result_instance = ArrayOfHostPatchManagerResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPatchManagerResult.to_json()

# convert the object into a dict
array_of_host_patch_manager_result_dict = array_of_host_patch_manager_result_instance.to_dict()
# create an instance of ArrayOfHostPatchManagerResult from a dict
array_of_host_patch_manager_result_form_dict = array_of_host_patch_manager_result.from_dict(array_of_host_patch_manager_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


