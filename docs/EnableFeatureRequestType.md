# EnableFeatureRequestType

The parameters of *LicenseManager.EnableFeature*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**feature_key** | **str** | Name of the feature to enable.  | 

## Example

```python
from vmware_vi.models.enable_feature_request_type import EnableFeatureRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableFeatureRequestType from a JSON string
enable_feature_request_type_instance = EnableFeatureRequestType.from_json(json)
# print the JSON string representation of the object
print EnableFeatureRequestType.to_json()

# convert the object into a dict
enable_feature_request_type_dict = enable_feature_request_type_instance.to_dict()
# create an instance of EnableFeatureRequestType from a dict
enable_feature_request_type_form_dict = enable_feature_request_type.from_dict(enable_feature_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


