# CheckLicenseFeatureRequestType

The parameters of *LicenseManager.CheckLicenseFeature*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**feature_key** | **str** | Name of the feature to enable.  | 

## Example

```python
from vmware_vi.models.check_license_feature_request_type import CheckLicenseFeatureRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckLicenseFeatureRequestType from a JSON string
check_license_feature_request_type_instance = CheckLicenseFeatureRequestType.from_json(json)
# print the JSON string representation of the object
print CheckLicenseFeatureRequestType.to_json()

# convert the object into a dict
check_license_feature_request_type_dict = check_license_feature_request_type_instance.to_dict()
# create an instance of CheckLicenseFeatureRequestType from a dict
check_license_feature_request_type_form_dict = check_license_feature_request_type.from_dict(check_license_feature_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


