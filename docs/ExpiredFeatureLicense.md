# ExpiredFeatureLicense

An ExpiredFeatureLicense fault is thrown if an attempt to acquire an Addon license 'feature failed for count 'count'.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** |  | 
**count** | **int** |  | 
**expiration_date** | **datetime** |  | 

## Example

```python
from vmware_vi.models.expired_feature_license import ExpiredFeatureLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiredFeatureLicense from a JSON string
expired_feature_license_instance = ExpiredFeatureLicense.from_json(json)
# print the JSON string representation of the object
print ExpiredFeatureLicense.to_json()

# convert the object into a dict
expired_feature_license_dict = expired_feature_license_instance.to_dict()
# create an instance of ExpiredFeatureLicense from a dict
expired_feature_license_form_dict = expired_feature_license.from_dict(expired_feature_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


