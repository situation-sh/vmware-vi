# LicenseAssignmentManagerLicenseAssignment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Id for the entity  ***Since:*** vSphere API 4.0  | 
**scope** | **str** | Scope of the entityId  ***Since:*** vSphere API 4.0  | [optional] 
**entity_display_name** | **str** | Display name of the entity  ***Since:*** vSphere API 4.0  | [optional] 
**assigned_license** | [**LicenseManagerLicenseInfo**](LicenseManagerLicenseInfo.md) |  | 
**properties** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Additional properties associated with this assignment Some of the properties are: \&quot;inUseFeatures\&quot; -- Features in the license key that are being used by the entity \&quot;ProductName\&quot; -- Name of the entity.  Should match the product name of the assigned license. \&quot;ProductVersion\&quot; -- Version of the entity. Should match the product version of the assigned license. \&quot;Evaluation\&quot; -- EvaluationInfo object representing the evaluation left for the entity.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.license_assignment_manager_license_assignment import LicenseAssignmentManagerLicenseAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseAssignmentManagerLicenseAssignment from a JSON string
license_assignment_manager_license_assignment_instance = LicenseAssignmentManagerLicenseAssignment.from_json(json)
# print the JSON string representation of the object
print LicenseAssignmentManagerLicenseAssignment.to_json()

# convert the object into a dict
license_assignment_manager_license_assignment_dict = license_assignment_manager_license_assignment_instance.to_dict()
# create an instance of LicenseAssignmentManagerLicenseAssignment from a dict
license_assignment_manager_license_assignment_form_dict = license_assignment_manager_license_assignment.from_dict(license_assignment_manager_license_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


