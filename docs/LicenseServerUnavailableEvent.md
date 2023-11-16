# LicenseServerUnavailableEvent

This event is reported if the LicenseServer becomes unreachable. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_server** | **str** |  | 

## Example

```python
from vmware_vi.models.license_server_unavailable_event import LicenseServerUnavailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseServerUnavailableEvent from a JSON string
license_server_unavailable_event_instance = LicenseServerUnavailableEvent.from_json(json)
# print the JSON string representation of the object
print LicenseServerUnavailableEvent.to_json()

# convert the object into a dict
license_server_unavailable_event_dict = license_server_unavailable_event_instance.to_dict()
# create an instance of LicenseServerUnavailableEvent from a dict
license_server_unavailable_event_form_dict = license_server_unavailable_event.from_dict(license_server_unavailable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


