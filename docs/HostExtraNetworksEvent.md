# HostExtraNetworksEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records the fact that a host has extra networks not used by other hosts for HA communication  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **str** | The comma-separated list of extra networks  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_extra_networks_event import HostExtraNetworksEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostExtraNetworksEvent from a JSON string
host_extra_networks_event_instance = HostExtraNetworksEvent.from_json(json)
# print the JSON string representation of the object
print HostExtraNetworksEvent.to_json()

# convert the object into a dict
host_extra_networks_event_dict = host_extra_networks_event_instance.to_dict()
# create an instance of HostExtraNetworksEvent from a dict
host_extra_networks_event_form_dict = host_extra_networks_event.from_dict(host_extra_networks_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


