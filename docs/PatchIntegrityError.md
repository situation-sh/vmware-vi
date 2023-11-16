# PatchIntegrityError

This fault is thrown if a patch operation fails because the signature of the patch did not check out. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.patch_integrity_error import PatchIntegrityError

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIntegrityError from a JSON string
patch_integrity_error_instance = PatchIntegrityError.from_json(json)
# print the JSON string representation of the object
print PatchIntegrityError.to_json()

# convert the object into a dict
patch_integrity_error_dict = patch_integrity_error_instance.to_dict()
# create an instance of PatchIntegrityError from a dict
patch_integrity_error_form_dict = patch_integrity_error.from_dict(patch_integrity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


