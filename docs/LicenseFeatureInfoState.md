# LicenseFeatureInfoState

A boxed *LicenseFeatureInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**LicenseFeatureInfoStateEnum**](LicenseFeatureInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.license_feature_info_state import LicenseFeatureInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseFeatureInfoState from a JSON string
license_feature_info_state_instance = LicenseFeatureInfoState.from_json(json)
# print the JSON string representation of the object
print LicenseFeatureInfoState.to_json()

# convert the object into a dict
license_feature_info_state_dict = license_feature_info_state_instance.to_dict()
# create an instance of LicenseFeatureInfoState from a dict
license_feature_info_state_form_dict = license_feature_info_state.from_dict(license_feature_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


