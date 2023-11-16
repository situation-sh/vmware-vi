# LicenseExpiredEvent

This event records the expiration of a license. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**LicenseFeatureInfo**](LicenseFeatureInfo.md) |  | 

## Example

```python
from vmware_vi.models.license_expired_event import LicenseExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseExpiredEvent from a JSON string
license_expired_event_instance = LicenseExpiredEvent.from_json(json)
# print the JSON string representation of the object
print LicenseExpiredEvent.to_json()

# convert the object into a dict
license_expired_event_dict = license_expired_event_instance.to_dict()
# create an instance of LicenseExpiredEvent from a dict
license_expired_event_form_dict = license_expired_event.from_dict(license_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


