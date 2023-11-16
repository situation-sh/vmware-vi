# ResourcePoolDestroyedEvent

This event records when a resource pool is destroyed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.resource_pool_destroyed_event import ResourcePoolDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolDestroyedEvent from a JSON string
resource_pool_destroyed_event_instance = ResourcePoolDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print ResourcePoolDestroyedEvent.to_json()

# convert the object into a dict
resource_pool_destroyed_event_dict = resource_pool_destroyed_event_instance.to_dict()
# create an instance of ResourcePoolDestroyedEvent from a dict
resource_pool_destroyed_event_form_dict = resource_pool_destroyed_event.from_dict(resource_pool_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


