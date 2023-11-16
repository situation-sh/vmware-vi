# VMotionLicenseExpiredEvent

This event records an expired VMotion license. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_motion_license_expired_event import VMotionLicenseExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionLicenseExpiredEvent from a JSON string
v_motion_license_expired_event_instance = VMotionLicenseExpiredEvent.from_json(json)
# print the JSON string representation of the object
print VMotionLicenseExpiredEvent.to_json()

# convert the object into a dict
v_motion_license_expired_event_dict = v_motion_license_expired_event_instance.to_dict()
# create an instance of VMotionLicenseExpiredEvent from a dict
v_motion_license_expired_event_form_dict = v_motion_license_expired_event.from_dict(v_motion_license_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


