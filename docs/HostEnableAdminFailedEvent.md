# HostEnableAdminFailedEvent

This event records the failure to restore some of the administrator's permissions.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[Permission]**](Permission.md) |  | 

## Example

```python
from vmware_vi.models.host_enable_admin_failed_event import HostEnableAdminFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostEnableAdminFailedEvent from a JSON string
host_enable_admin_failed_event_instance = HostEnableAdminFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostEnableAdminFailedEvent.to_json()

# convert the object into a dict
host_enable_admin_failed_event_dict = host_enable_admin_failed_event_instance.to_dict()
# create an instance of HostEnableAdminFailedEvent from a dict
host_enable_admin_failed_event_form_dict = host_enable_admin_failed_event.from_dict(host_enable_admin_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


