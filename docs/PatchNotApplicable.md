# PatchNotApplicable

This fault is thrown if a patch install fails because the patch is not applicable to the host.  Typically, a subclass of this exception is thrown, indicating a problem such as the patch is superseded, already installed, or has dependencies missing, and so on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** | The ID of the patch that is not applicable to the host.  | 

## Example

```python
from vmware_vi.models.patch_not_applicable import PatchNotApplicable

# TODO update the JSON string below
json = "{}"
# create an instance of PatchNotApplicable from a JSON string
patch_not_applicable_instance = PatchNotApplicable.from_json(json)
# print the JSON string representation of the object
print PatchNotApplicable.to_json()

# convert the object into a dict
patch_not_applicable_dict = patch_not_applicable_instance.to_dict()
# create an instance of PatchNotApplicable from a dict
patch_not_applicable_form_dict = patch_not_applicable.from_dict(patch_not_applicable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


