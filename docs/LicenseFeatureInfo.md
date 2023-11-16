# LicenseFeatureInfo

Deprecated as of vSphere API 4.0, this is not used by the system.  A single feature that can be licensed.  This information is immutable. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique identifier for license as defined in License source data.  Max length of this string is 64 characters of ASCII/ISO Latin-1 character set.  | 
**feature_name** | **str** | The display string for the feature name.  | 
**feature_description** | **str** | A human readable description of what function this feature enables.  ***Since:*** VI API 2.5  | [optional] 
**state** | [**LicenseFeatureInfoStateEnum**](LicenseFeatureInfoStateEnum.md) |  | [optional] 
**cost_unit** | **str** | Each license has a cost associated with it and the value of costUnit specifies the applicable unit.  See also *LicenseFeatureInfoUnit_enum*.  | 
**source_restriction** | **str** | Describe any restriction on the source of a license for this feature.  See also *LicenseFeatureInfoSourceRestriction_enum*.  ***Since:*** VI API 2.5  | [optional] 
**dependent_key** | **List[str]** | Report List of feature keys used by this edition.  ***Since:*** VI API 2.5  | [optional] 
**edition** | **bool** | Flag to indicate whether the feature is an edition.  ***Since:*** VI API 2.5  | [optional] 
**expires_on** | **datetime** | Date representing the expiration date  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.license_feature_info import LicenseFeatureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseFeatureInfo from a JSON string
license_feature_info_instance = LicenseFeatureInfo.from_json(json)
# print the JSON string representation of the object
print LicenseFeatureInfo.to_json()

# convert the object into a dict
license_feature_info_dict = license_feature_info_instance.to_dict()
# create an instance of LicenseFeatureInfo from a dict
license_feature_info_form_dict = license_feature_info.from_dict(license_feature_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


