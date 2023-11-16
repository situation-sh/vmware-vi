# ArrayOfPatchAlreadyInstalled

A boxed array of *PatchAlreadyInstalled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchAlreadyInstalled]**](PatchAlreadyInstalled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_already_installed import ArrayOfPatchAlreadyInstalled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchAlreadyInstalled from a JSON string
array_of_patch_already_installed_instance = ArrayOfPatchAlreadyInstalled.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchAlreadyInstalled.to_json()

# convert the object into a dict
array_of_patch_already_installed_dict = array_of_patch_already_installed_instance.to_dict()
# create an instance of ArrayOfPatchAlreadyInstalled from a dict
array_of_patch_already_installed_form_dict = array_of_patch_already_installed.from_dict(array_of_patch_already_installed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


