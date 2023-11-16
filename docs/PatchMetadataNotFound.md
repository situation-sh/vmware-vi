# PatchMetadataNotFound

This fault is thrown if the metadata associated with a patch is not found when a patch query or install is attempted. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.patch_metadata_not_found import PatchMetadataNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMetadataNotFound from a JSON string
patch_metadata_not_found_instance = PatchMetadataNotFound.from_json(json)
# print the JSON string representation of the object
print PatchMetadataNotFound.to_json()

# convert the object into a dict
patch_metadata_not_found_dict = patch_metadata_not_found_instance.to_dict()
# create an instance of PatchMetadataNotFound from a dict
patch_metadata_not_found_form_dict = patch_metadata_not_found.from_dict(patch_metadata_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


