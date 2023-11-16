# ArrayOfLicenseFeatureInfoState

A boxed array of *LicenseFeatureInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseFeatureInfoStateEnum]**](LicenseFeatureInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_feature_info_state import ArrayOfLicenseFeatureInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseFeatureInfoState from a JSON string
array_of_license_feature_info_state_instance = ArrayOfLicenseFeatureInfoState.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseFeatureInfoState.to_json()

# convert the object into a dict
array_of_license_feature_info_state_dict = array_of_license_feature_info_state_instance.to_dict()
# create an instance of ArrayOfLicenseFeatureInfoState from a dict
array_of_license_feature_info_state_form_dict = array_of_license_feature_info_state.from_dict(array_of_license_feature_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


