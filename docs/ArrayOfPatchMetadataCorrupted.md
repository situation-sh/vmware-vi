# ArrayOfPatchMetadataCorrupted

A boxed array of *PatchMetadataCorrupted*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchMetadataCorrupted]**](PatchMetadataCorrupted.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_metadata_corrupted import ArrayOfPatchMetadataCorrupted

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchMetadataCorrupted from a JSON string
array_of_patch_metadata_corrupted_instance = ArrayOfPatchMetadataCorrupted.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchMetadataCorrupted.to_json()

# convert the object into a dict
array_of_patch_metadata_corrupted_dict = array_of_patch_metadata_corrupted_instance.to_dict()
# create an instance of ArrayOfPatchMetadataCorrupted from a dict
array_of_patch_metadata_corrupted_form_dict = array_of_patch_metadata_corrupted.from_dict(array_of_patch_metadata_corrupted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


