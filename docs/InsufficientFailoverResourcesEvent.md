# InsufficientFailoverResourcesEvent

This event records that the cluster resources are insufficient to satisfy the configured HA failover level. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_failover_resources_event import InsufficientFailoverResourcesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientFailoverResourcesEvent from a JSON string
insufficient_failover_resources_event_instance = InsufficientFailoverResourcesEvent.from_json(json)
# print the JSON string representation of the object
print InsufficientFailoverResourcesEvent.to_json()

# convert the object into a dict
insufficient_failover_resources_event_dict = insufficient_failover_resources_event_instance.to_dict()
# create an instance of InsufficientFailoverResourcesEvent from a dict
insufficient_failover_resources_event_form_dict = insufficient_failover_resources_event.from_dict(insufficient_failover_resources_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


