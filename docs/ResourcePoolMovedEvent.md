# ResourcePoolMovedEvent

This event records when a resource pool is moved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_parent** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 
**new_parent** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.resource_pool_moved_event import ResourcePoolMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolMovedEvent from a JSON string
resource_pool_moved_event_instance = ResourcePoolMovedEvent.from_json(json)
# print the JSON string representation of the object
print ResourcePoolMovedEvent.to_json()

# convert the object into a dict
resource_pool_moved_event_dict = resource_pool_moved_event_instance.to_dict()
# create an instance of ResourcePoolMovedEvent from a dict
resource_pool_moved_event_form_dict = resource_pool_moved_event.from_dict(resource_pool_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


