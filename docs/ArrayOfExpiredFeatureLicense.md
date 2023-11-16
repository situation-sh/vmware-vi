# ArrayOfExpiredFeatureLicense

A boxed array of *ExpiredFeatureLicense*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExpiredFeatureLicense]**](ExpiredFeatureLicense.md) |  | 

## Example

```python
from vmware_vi.models.array_of_expired_feature_license import ArrayOfExpiredFeatureLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExpiredFeatureLicense from a JSON string
array_of_expired_feature_license_instance = ArrayOfExpiredFeatureLicense.from_json(json)
# print the JSON string representation of the object
print ArrayOfExpiredFeatureLicense.to_json()

# convert the object into a dict
array_of_expired_feature_license_dict = array_of_expired_feature_license_instance.to_dict()
# create an instance of ArrayOfExpiredFeatureLicense from a dict
array_of_expired_feature_license_form_dict = array_of_expired_feature_license.from_dict(array_of_expired_feature_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


