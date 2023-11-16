# HostNoAvailableNetworksEvent

This event records the fact that a host does not have any available networks for HA communication  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **str** | The comma-separated list of used networks  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_no_available_networks_event import HostNoAvailableNetworksEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostNoAvailableNetworksEvent from a JSON string
host_no_available_networks_event_instance = HostNoAvailableNetworksEvent.from_json(json)
# print the JSON string representation of the object
print HostNoAvailableNetworksEvent.to_json()

# convert the object into a dict
host_no_available_networks_event_dict = host_no_available_networks_event_instance.to_dict()
# create an instance of HostNoAvailableNetworksEvent from a dict
host_no_available_networks_event_form_dict = host_no_available_networks_event.from_dict(host_no_available_networks_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


