# RemoveAssignedLicenseRequestType

The parameters of *LicenseAssignmentManager.RemoveAssignedLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | ID of the entity. E.g. HostSystem.  | 

## Example

```python
from vmware_vi.models.remove_assigned_license_request_type import RemoveAssignedLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAssignedLicenseRequestType from a JSON string
remove_assigned_license_request_type_instance = RemoveAssignedLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveAssignedLicenseRequestType.to_json()

# convert the object into a dict
remove_assigned_license_request_type_dict = remove_assigned_license_request_type_instance.to_dict()
# create an instance of RemoveAssignedLicenseRequestType from a dict
remove_assigned_license_request_type_form_dict = remove_assigned_license_request_type.from_dict(remove_assigned_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


