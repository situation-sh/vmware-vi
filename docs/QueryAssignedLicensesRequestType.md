# QueryAssignedLicensesRequestType

The parameters of *LicenseAssignmentManager.QueryAssignedLicenses*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | ID of the entity. E.g. HostSystem.  | [optional] 

## Example

```python
from vmware_vi.models.query_assigned_licenses_request_type import QueryAssignedLicensesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAssignedLicensesRequestType from a JSON string
query_assigned_licenses_request_type_instance = QueryAssignedLicensesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAssignedLicensesRequestType.to_json()

# convert the object into a dict
query_assigned_licenses_request_type_dict = query_assigned_licenses_request_type_instance.to_dict()
# create an instance of QueryAssignedLicensesRequestType from a dict
query_assigned_licenses_request_type_form_dict = query_assigned_licenses_request_type.from_dict(query_assigned_licenses_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


