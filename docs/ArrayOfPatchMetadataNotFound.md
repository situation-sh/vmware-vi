# ArrayOfPatchMetadataNotFound

A boxed array of *PatchMetadataNotFound*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PatchMetadataNotFound]**](PatchMetadataNotFound.md) |  | 

## Example

```python
from vmware_vi.models.array_of_patch_metadata_not_found import ArrayOfPatchMetadataNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPatchMetadataNotFound from a JSON string
array_of_patch_metadata_not_found_instance = ArrayOfPatchMetadataNotFound.from_json(json)
# print the JSON string representation of the object
print ArrayOfPatchMetadataNotFound.to_json()

# convert the object into a dict
array_of_patch_metadata_not_found_dict = array_of_patch_metadata_not_found_instance.to_dict()
# create an instance of ArrayOfPatchMetadataNotFound from a dict
array_of_patch_metadata_not_found_form_dict = array_of_patch_metadata_not_found.from_dict(array_of_patch_metadata_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


