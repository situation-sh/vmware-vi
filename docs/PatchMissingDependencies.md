# PatchMissingDependencies

This fault is thrown if a patch install fails because the patch requires other patches or libraries that are not installed on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prerequisite_patch** | **List[str]** | The ID of required patches.  | [optional] 
**prerequisite_lib** | **List[str]** | The names of required libraries or RPMs.  | [optional] 

## Example

```python
from vmware_vi.models.patch_missing_dependencies import PatchMissingDependencies

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMissingDependencies from a JSON string
patch_missing_dependencies_instance = PatchMissingDependencies.from_json(json)
# print the JSON string representation of the object
print PatchMissingDependencies.to_json()

# convert the object into a dict
patch_missing_dependencies_dict = patch_missing_dependencies_instance.to_dict()
# create an instance of PatchMissingDependencies from a dict
patch_missing_dependencies_form_dict = patch_missing_dependencies.from_dict(patch_missing_dependencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


