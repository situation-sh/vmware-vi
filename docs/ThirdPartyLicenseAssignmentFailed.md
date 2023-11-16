# ThirdPartyLicenseAssignmentFailed

A ThirdPartyLicenseAssignmentFailed fault is thrown when the license assignment to a 3rd party module fails.  The 3rd-party modules are installed and ran on ESX hosts, so this fault provides both host and module IDs.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**module** | **str** | The asset-id of 3rd party module  ***Since:*** vSphere API 5.0  | 
**reason** | **str** | The reason why the assignment failed, if known.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.third_party_license_assignment_failed import ThirdPartyLicenseAssignmentFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyLicenseAssignmentFailed from a JSON string
third_party_license_assignment_failed_instance = ThirdPartyLicenseAssignmentFailed.from_json(json)
# print the JSON string representation of the object
print ThirdPartyLicenseAssignmentFailed.to_json()

# convert the object into a dict
third_party_license_assignment_failed_dict = third_party_license_assignment_failed_instance.to_dict()
# create an instance of ThirdPartyLicenseAssignmentFailed from a dict
third_party_license_assignment_failed_form_dict = third_party_license_assignment_failed.from_dict(third_party_license_assignment_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


