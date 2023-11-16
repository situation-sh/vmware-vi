# ServerLicenseExpiredEvent

This event records an expired VirtualCenter server license. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** |  | 

## Example

```python
from vmware_vi.models.server_license_expired_event import ServerLicenseExpiredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ServerLicenseExpiredEvent from a JSON string
server_license_expired_event_instance = ServerLicenseExpiredEvent.from_json(json)
# print the JSON string representation of the object
print ServerLicenseExpiredEvent.to_json()

# convert the object into a dict
server_license_expired_event_dict = server_license_expired_event_instance.to_dict()
# create an instance of ServerLicenseExpiredEvent from a dict
server_license_expired_event_form_dict = server_license_expired_event.from_dict(server_license_expired_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


