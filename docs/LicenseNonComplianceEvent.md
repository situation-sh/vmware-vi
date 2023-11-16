# LicenseNonComplianceEvent

This event records that the inventory is not license compliant.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Gives the url at which more details about non-compliance can be found.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.license_non_compliance_event import LicenseNonComplianceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseNonComplianceEvent from a JSON string
license_non_compliance_event_instance = LicenseNonComplianceEvent.from_json(json)
# print the JSON string representation of the object
print LicenseNonComplianceEvent.to_json()

# convert the object into a dict
license_non_compliance_event_dict = license_non_compliance_event_instance.to_dict()
# create an instance of LicenseNonComplianceEvent from a dict
license_non_compliance_event_form_dict = license_non_compliance_event.from_dict(license_non_compliance_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


