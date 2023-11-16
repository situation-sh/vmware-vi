# ArrayOfPatchMetadataInvalid

A boxed array of *PatchMetadataInvalid*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchMetadataInvalid]**](PatchMetadataInvalid.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_metadata_invalid import ArrayOfPatchMetadataInvalid

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchMetadataInvalid from a JSON string
array_of_patch_metadata_invalid_instance = ArrayOfPatchMetadataInvalid.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchMetadataInvalid.to_json()

# convert the object into a dict
array_of_patch_metadata_invalid_dict = array_of_patch_metadata_invalid_instance.to_dict()
# create an instance of ArrayOfPatchMetadataInvalid from a dict
array_of_patch_metadata_invalid_form_dict = array_of_patch_metadata_invalid.from_dict(array_of_patch_metadata_invalid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


