# HostLicenseExpiredEvent

This event records an expired host license. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_license_expired_event import HostLicenseExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostLicenseExpiredEvent from a JSON string
host_license_expired_event_instance = HostLicenseExpiredEvent.from_json(json)
# print the JSON string representation of the object
print HostLicenseExpiredEvent.to_json()

# convert the object into a dict
host_license_expired_event_dict = host_license_expired_event_instance.to_dict()
# create an instance of HostLicenseExpiredEvent from a dict
host_license_expired_event_form_dict = host_license_expired_event.from_dict(host_license_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


