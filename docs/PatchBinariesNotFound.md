# PatchBinariesNotFound

This fault is thrown if a patch install fails because the binaries associated with the patch are not found. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** | The patch whose associated binaries are not found.  | 
**binary** | **List[str]** | The binaries that are not found.  | [optional] 

## Example

```python
from vmware_vi.models.patch_binaries_not_found import PatchBinariesNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of PatchBinariesNotFound from a JSON string
patch_binaries_not_found_instance = PatchBinariesNotFound.from_json(json)
# print the JSON string representation of the object
print PatchBinariesNotFound.to_json()

# convert the object into a dict
patch_binaries_not_found_dict = patch_binaries_not_found_instance.to_dict()
# create an instance of PatchBinariesNotFound from a dict
patch_binaries_not_found_form_dict = patch_binaries_not_found.from_dict(patch_binaries_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


