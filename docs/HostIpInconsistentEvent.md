# HostIpInconsistentEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that the IP address resolution returned different addresses on the host.  Please check your host's network configuration.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | 
**ip_address2** | **str** |  | 

## Example

```python
from vmware_vi.models.host_ip_inconsistent_event import HostIpInconsistentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpInconsistentEvent from a JSON string
host_ip_inconsistent_event_instance = HostIpInconsistentEvent.from_json(json)
# print the JSON string representation of the object
print HostIpInconsistentEvent.to_json()

# convert the object into a dict
host_ip_inconsistent_event_dict = host_ip_inconsistent_event_instance.to_dict()
# create an instance of HostIpInconsistentEvent from a dict
host_ip_inconsistent_event_form_dict = host_ip_inconsistent_event.from_dict(host_ip_inconsistent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


