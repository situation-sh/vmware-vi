# ArrayOfPatchInstallFailed

A boxed array of *PatchInstallFailed*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchInstallFailed]**](PatchInstallFailed.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_install_failed import ArrayOfPatchInstallFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchInstallFailed from a JSON string
array_of_patch_install_failed_instance = ArrayOfPatchInstallFailed.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchInstallFailed.to_json()

# convert the object into a dict
array_of_patch_install_failed_dict = array_of_patch_install_failed_instance.to_dict()
# create an instance of ArrayOfPatchInstallFailed from a dict
array_of_patch_install_failed_form_dict = array_of_patch_install_failed.from_dict(array_of_patch_install_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


