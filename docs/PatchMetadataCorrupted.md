# PatchMetadataCorrupted

This fault is thrown if the metadata associated with a patch is corrupted or unreadable when a patch query or install is attempted. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.patch_metadata_corrupted import PatchMetadataCorrupted

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMetadataCorrupted from a JSON string
patch_metadata_corrupted_instance = PatchMetadataCorrupted.from_json(json)
# print the JSON string representation of the object
print PatchMetadataCorrupted.to_json()

# convert the object into a dict
patch_metadata_corrupted_dict = patch_metadata_corrupted_instance.to_dict()
# create an instance of PatchMetadataCorrupted from a dict
patch_metadata_corrupted_form_dict = patch_metadata_corrupted.from_dict(patch_metadata_corrupted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


