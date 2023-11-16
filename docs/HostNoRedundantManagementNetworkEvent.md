# HostNoRedundantManagementNetworkEvent

This event records the fact that a host does not have a redundant management network.  It is recommended that host management networks be configured with redundancy.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_no_redundant_management_network_event import HostNoRedundantManagementNetworkEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostNoRedundantManagementNetworkEvent from a JSON string
host_no_redundant_management_network_event_instance = HostNoRedundantManagementNetworkEvent.from_json(json)
# print the JSON string representation of the object
print HostNoRedundantManagementNetworkEvent.to_json()

# convert the object into a dict
host_no_redundant_management_network_event_dict = host_no_redundant_management_network_event_instance.to_dict()
# create an instance of HostNoRedundantManagementNetworkEvent from a dict
host_no_redundant_management_network_event_form_dict = host_no_redundant_management_network_event.from_dict(host_no_redundant_management_network_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


