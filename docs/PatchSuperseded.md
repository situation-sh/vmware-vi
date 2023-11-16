# PatchSuperseded

This fault is thrown if a patch install fails because the patch is superseded by patches already installed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supersede** | **List[str]** | The patches that supersede this patch.  | [optional] 

## Example

```python
from vmware_vi.models.patch_superseded import PatchSuperseded

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSuperseded from a JSON string
patch_superseded_instance = PatchSuperseded.from_json(json)
# print the JSON string representation of the object
print PatchSuperseded.to_json()

# convert the object into a dict
patch_superseded_dict = patch_superseded_instance.to_dict()
# create an instance of PatchSuperseded from a dict
patch_superseded_form_dict = patch_superseded.from_dict(patch_superseded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


