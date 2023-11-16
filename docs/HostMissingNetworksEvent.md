# HostMissingNetworksEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records the fact that a host is missing networks that other hosts are using for HA communication  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.host_missing_networks_event import HostMissingNetworksEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostMissingNetworksEvent from a JSON string
host_missing_networks_event_instance = HostMissingNetworksEvent.from_json(json)
# print the JSON string representation of the object
print HostMissingNetworksEvent.to_json()

# convert the object into a dict
host_missing_networks_event_dict = host_missing_networks_event_instance.to_dict()
# create an instance of HostMissingNetworksEvent from a dict
host_missing_networks_event_form_dict = host_missing_networks_event.from_dict(host_missing_networks_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


