# HostIpChangedEvent

This event records a change in host IP address.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_ip** | **str** | Old IP address of the host.  ***Since:*** VI API 2.5  | 
**new_ip** | **str** | New IP address of the host.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_ip_changed_event import HostIpChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpChangedEvent from a JSON string
host_ip_changed_event_instance = HostIpChangedEvent.from_json(json)
# print the JSON string representation of the object
print HostIpChangedEvent.to_json()

# convert the object into a dict
host_ip_changed_event_dict = host_ip_changed_event_instance.to_dict()
# create an instance of HostIpChangedEvent from a dict
host_ip_changed_event_form_dict = host_ip_changed_event.from_dict(host_ip_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


