# QueryLicenseUsageRequestType

The parameters of *LicenseManager.QueryLicenseUsage*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_license_usage_request_type import QueryLicenseUsageRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryLicenseUsageRequestType from a JSON string
query_license_usage_request_type_instance = QueryLicenseUsageRequestType.from_json(json)
# print the JSON string representation of the object
print QueryLicenseUsageRequestType.to_json()

# convert the object into a dict
query_license_usage_request_type_dict = query_license_usage_request_type_instance.to_dict()
# create an instance of QueryLicenseUsageRequestType from a dict
query_license_usage_request_type_form_dict = query_license_usage_request_type.from_dict(query_license_usage_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


