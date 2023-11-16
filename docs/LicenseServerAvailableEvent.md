# LicenseServerAvailableEvent

This event is reported if the LicenseServer was previously unreachable and is now reachable. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_server** | **str** |  | 

## Example

```python
from vmware_vi.models.license_server_available_event import LicenseServerAvailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseServerAvailableEvent from a JSON string
license_server_available_event_instance = LicenseServerAvailableEvent.from_json(json)
# print the JSON string representation of the object
print LicenseServerAvailableEvent.to_json()

# convert the object into a dict
license_server_available_event_dict = license_server_available_event_instance.to_dict()
# create an instance of LicenseServerAvailableEvent from a dict
license_server_available_event_form_dict = license_server_available_event.from_dict(license_server_available_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


