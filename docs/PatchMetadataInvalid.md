# PatchMetadataInvalid

This fault is thrown if a patch query or installation operation fails because of a problem with the metadata associated with the patch.  Typically, a subclass of this exception is thrown, indicating a problem such as the metadata is not found or the metadata is corrupted. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** | The patch ID whose associated metadata is invalid.  | 
**meta_data** | **List[str]** | The metadata file that is not available or corrupted.  | [optional] 

## Example

```python
from vmware_vi.models.patch_metadata_invalid import PatchMetadataInvalid

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMetadataInvalid from a JSON string
patch_metadata_invalid_instance = PatchMetadataInvalid.from_json(json)
# print the JSON string representation of the object
print PatchMetadataInvalid.to_json()

# convert the object into a dict
patch_metadata_invalid_dict = patch_metadata_invalid_instance.to_dict()
# create an instance of PatchMetadataInvalid from a dict
patch_metadata_invalid_form_dict = patch_metadata_invalid.from_dict(patch_metadata_invalid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


