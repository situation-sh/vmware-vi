# ArrayOfLicenseExpiredEvent

A boxed array of *LicenseExpiredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseExpiredEvent]**](LicenseExpiredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_expired_event import ArrayOfLicenseExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseExpiredEvent from a JSON string
array_of_license_expired_event_instance = ArrayOfLicenseExpiredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseExpiredEvent.to_json()

# convert the object into a dict
array_of_license_expired_event_dict = array_of_license_expired_event_instance.to_dict()
# create an instance of ArrayOfLicenseExpiredEvent from a dict
array_of_license_expired_event_form_dict = array_of_license_expired_event.from_dict(array_of_license_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


