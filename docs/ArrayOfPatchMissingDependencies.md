# ArrayOfPatchMissingDependencies

A boxed array of *PatchMissingDependencies*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchMissingDependencies]**](PatchMissingDependencies.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_missing_dependencies import ArrayOfPatchMissingDependencies

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchMissingDependencies from a JSON string
array_of_patch_missing_dependencies_instance = ArrayOfPatchMissingDependencies.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchMissingDependencies.to_json()

# convert the object into a dict
array_of_patch_missing_dependencies_dict = array_of_patch_missing_dependencies_instance.to_dict()
# create an instance of ArrayOfPatchMissingDependencies from a dict
array_of_patch_missing_dependencies_form_dict = array_of_patch_missing_dependencies.from_dict(array_of_patch_missing_dependencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


