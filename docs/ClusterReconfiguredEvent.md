# ClusterReconfiguredEvent

This event records when a cluster is reconfigured. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_reconfigured_event import ClusterReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterReconfiguredEvent from a JSON string
cluster_reconfigured_event_instance = ClusterReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ClusterReconfiguredEvent.to_json()

# convert the object into a dict
cluster_reconfigured_event_dict = cluster_reconfigured_event_instance.to_dict()
# create an instance of ClusterReconfiguredEvent from a dict
cluster_reconfigured_event_form_dict = cluster_reconfigured_event.from_dict(cluster_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


