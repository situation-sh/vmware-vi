# DasClusterIsolatedEvent

This event records that all hosts have been isolated from the network in a HA cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_cluster_isolated_event import DasClusterIsolatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasClusterIsolatedEvent from a JSON string
das_cluster_isolated_event_instance = DasClusterIsolatedEvent.from_json(json)
# print the JSON string representation of the object
print DasClusterIsolatedEvent.to_json()

# convert the object into a dict
das_cluster_isolated_event_dict = das_cluster_isolated_event_instance.to_dict()
# create an instance of DasClusterIsolatedEvent from a dict
das_cluster_isolated_event_form_dict = das_cluster_isolated_event.from_dict(das_cluster_isolated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


