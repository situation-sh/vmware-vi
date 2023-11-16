# LicenseAssignmentFailed

A LicenseAssignmentFailed fault is thrown when VirtualCenter fails to assign a license to an entity.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the assignment failed, if known.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.license_assignment_failed import LicenseAssignmentFailed

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseAssignmentFailed from a JSON string
license_assignment_failed_instance = LicenseAssignmentFailed.from_json(json)
# print the JSON string representation of the object
print LicenseAssignmentFailed.to_json()

# convert the object into a dict
license_assignment_failed_dict = license_assignment_failed_instance.to_dict()
# create an instance of LicenseAssignmentFailed from a dict
license_assignment_failed_form_dict = license_assignment_failed.from_dict(license_assignment_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


