# UpdateAssignedLicenseRequestType

The parameters of *LicenseAssignmentManager.UpdateAssignedLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | ID of the entity. E.g. HostSystem.  | 
**license_key** | **str** | A license.  | 
**entity_display_name** | **str** | Display name for the entity  | [optional] 

## Example

```python
from vmware_vi.models.update_assigned_license_request_type import UpdateAssignedLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssignedLicenseRequestType from a JSON string
update_assigned_license_request_type_instance = UpdateAssignedLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateAssignedLicenseRequestType.to_json()

# convert the object into a dict
update_assigned_license_request_type_dict = update_assigned_license_request_type_instance.to_dict()
# create an instance of UpdateAssignedLicenseRequestType from a dict
update_assigned_license_request_type_form_dict = update_assigned_license_request_type.from_dict(update_assigned_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


