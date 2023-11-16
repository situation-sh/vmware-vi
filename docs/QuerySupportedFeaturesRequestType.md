# QuerySupportedFeaturesRequestType

The parameters of *LicenseManager.QuerySupportedFeatures*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_supported_features_request_type import QuerySupportedFeaturesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySupportedFeaturesRequestType from a JSON string
query_supported_features_request_type_instance = QuerySupportedFeaturesRequestType.from_json(json)
# print the JSON string representation of the object
print QuerySupportedFeaturesRequestType.to_json()

# convert the object into a dict
query_supported_features_request_type_dict = query_supported_features_request_type_instance.to_dict()
# create an instance of QuerySupportedFeaturesRequestType from a dict
query_supported_features_request_type_form_dict = query_supported_features_request_type.from_dict(query_supported_features_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


