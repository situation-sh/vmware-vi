# HostNotInClusterEvent

This event records that the host is not a cluster member.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_not_in_cluster_event import HostNotInClusterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostNotInClusterEvent from a JSON string
host_not_in_cluster_event_instance = HostNotInClusterEvent.from_json(json)
# print the JSON string representation of the object
print HostNotInClusterEvent.to_json()

# convert the object into a dict
host_not_in_cluster_event_dict = host_not_in_cluster_event_instance.to_dict()
# create an instance of HostNotInClusterEvent from a dict
host_not_in_cluster_event_form_dict = host_not_in_cluster_event.from_dict(host_not_in_cluster_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


