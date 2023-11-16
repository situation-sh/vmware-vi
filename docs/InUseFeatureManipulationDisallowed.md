# InUseFeatureManipulationDisallowed

A InUseFeatureManipulationDisallowed fault is thrown if an Vim.LicenseAssignmentManager.SetFeatureInUse or Vim.LicenseAssignmentManager.ResetFeatureInUse call can not complete because a feature is not available or the manipulation is not allowed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.in_use_feature_manipulation_disallowed import InUseFeatureManipulationDisallowed

# TODO update the JSON string below
json = "{}"
# create an instance of InUseFeatureManipulationDisallowed from a JSON string
in_use_feature_manipulation_disallowed_instance = InUseFeatureManipulationDisallowed.from_json(json)
# print the JSON string representation of the object
print InUseFeatureManipulationDisallowed.to_json()

# convert the object into a dict
in_use_feature_manipulation_disallowed_dict = in_use_feature_manipulation_disallowed_instance.to_dict()
# create an instance of InUseFeatureManipulationDisallowed from a dict
in_use_feature_manipulation_disallowed_form_dict = in_use_feature_manipulation_disallowed.from_dict(in_use_feature_manipulation_disallowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


