# ArrayOfLicenseServerUnavailableEvent

A boxed array of *LicenseServerUnavailableEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseServerUnavailableEvent]**](LicenseServerUnavailableEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_server_unavailable_event import ArrayOfLicenseServerUnavailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseServerUnavailableEvent from a JSON string
array_of_license_server_unavailable_event_instance = ArrayOfLicenseServerUnavailableEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseServerUnavailableEvent.to_json()

# convert the object into a dict
array_of_license_server_unavailable_event_dict = array_of_license_server_unavailable_event_instance.to_dict()
# create an instance of ArrayOfLicenseServerUnavailableEvent from a dict
array_of_license_server_unavailable_event_form_dict = array_of_license_server_unavailable_event.from_dict(array_of_license_server_unavailable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


