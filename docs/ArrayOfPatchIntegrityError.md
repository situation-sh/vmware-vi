# ArrayOfPatchIntegrityError

A boxed array of *PatchIntegrityError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchIntegrityError]**](PatchIntegrityError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_integrity_error import ArrayOfPatchIntegrityError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchIntegrityError from a JSON string
array_of_patch_integrity_error_instance = ArrayOfPatchIntegrityError.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchIntegrityError.to_json()

# convert the object into a dict
array_of_patch_integrity_error_dict = array_of_patch_integrity_error_instance.to_dict()
# create an instance of ArrayOfPatchIntegrityError from a dict
array_of_patch_integrity_error_form_dict = array_of_patch_integrity_error.from_dict(array_of_patch_integrity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


