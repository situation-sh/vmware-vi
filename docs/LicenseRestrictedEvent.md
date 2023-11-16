# LicenseRestrictedEvent

This event records if the required licenses could not be reserved because of a restriction in the option file.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.license_restricted_event import LicenseRestrictedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRestrictedEvent from a JSON string
license_restricted_event_instance = LicenseRestrictedEvent.from_json(json)
# print the JSON string representation of the object
print LicenseRestrictedEvent.to_json()

# convert the object into a dict
license_restricted_event_dict = license_restricted_event_instance.to_dict()
# create an instance of LicenseRestrictedEvent from a dict
license_restricted_event_form_dict = license_restricted_event.from_dict(license_restricted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


