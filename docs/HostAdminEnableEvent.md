# HostAdminEnableEvent

This event records that the administrator permission has been restored.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_admin_enable_event import HostAdminEnableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostAdminEnableEvent from a JSON string
host_admin_enable_event_instance = HostAdminEnableEvent.from_json(json)
# print the JSON string representation of the object
print HostAdminEnableEvent.to_json()

# convert the object into a dict
host_admin_enable_event_dict = host_admin_enable_event_instance.to_dict()
# create an instance of HostAdminEnableEvent from a dict
host_admin_enable_event_form_dict = host_admin_enable_event.from_dict(host_admin_enable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


