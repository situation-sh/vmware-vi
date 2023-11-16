# QueryLicenseSourceAvailabilityRequestType

The parameters of *LicenseManager.QueryLicenseSourceAvailability*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_license_source_availability_request_type import QueryLicenseSourceAvailabilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryLicenseSourceAvailabilityRequestType from a JSON string
query_license_source_availability_request_type_instance = QueryLicenseSourceAvailabilityRequestType.from_json(json)
# print the JSON string representation of the object
print QueryLicenseSourceAvailabilityRequestType.to_json()

# convert the object into a dict
query_license_source_availability_request_type_dict = query_license_source_availability_request_type_instance.to_dict()
# create an instance of QueryLicenseSourceAvailabilityRequestType from a dict
query_license_source_availability_request_type_form_dict = query_license_source_availability_request_type.from_dict(query_license_source_availability_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


