# LicenseEvent

This is a base licensing event to group all license events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.license_event import LicenseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEvent from a JSON string
license_event_instance = LicenseEvent.from_json(json)
# print the JSON string representation of the object
print LicenseEvent.to_json()

# convert the object into a dict
license_event_dict = license_event_instance.to_dict()
# create an instance of LicenseEvent from a dict
license_event_form_dict = license_event.from_dict(license_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


