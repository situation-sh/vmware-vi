# HostAdminDisableEvent

This event records that the permission on the host has been changed such that only the user account used for VirtualCenter operation will have Administrator permission.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_admin_disable_event import HostAdminDisableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostAdminDisableEvent from a JSON string
host_admin_disable_event_instance = HostAdminDisableEvent.from_json(json)
# print the JSON string representation of the object
print HostAdminDisableEvent.to_json()

# convert the object into a dict
host_admin_disable_event_dict = host_admin_disable_event_instance.to_dict()
# create an instance of HostAdminDisableEvent from a dict
host_admin_disable_event_form_dict = host_admin_disable_event.from_dict(host_admin_disable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


