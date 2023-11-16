# ArrayOfLicenseNonComplianceEvent

A boxed array of *LicenseNonComplianceEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseNonComplianceEvent]**](LicenseNonComplianceEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_non_compliance_event import ArrayOfLicenseNonComplianceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseNonComplianceEvent from a JSON string
array_of_license_non_compliance_event_instance = ArrayOfLicenseNonComplianceEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseNonComplianceEvent.to_json()

# convert the object into a dict
array_of_license_non_compliance_event_dict = array_of_license_non_compliance_event_instance.to_dict()
# create an instance of ArrayOfLicenseNonComplianceEvent from a dict
array_of_license_non_compliance_event_form_dict = array_of_license_non_compliance_event.from_dict(array_of_license_non_compliance_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


