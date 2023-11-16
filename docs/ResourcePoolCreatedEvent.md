# ResourcePoolCreatedEvent

This event records when a new resource pool is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.resource_pool_created_event import ResourcePoolCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolCreatedEvent from a JSON string
resource_pool_created_event_instance = ResourcePoolCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ResourcePoolCreatedEvent.to_json()

# convert the object into a dict
resource_pool_created_event_dict = resource_pool_created_event_instance.to_dict()
# create an instance of ResourcePoolCreatedEvent from a dict
resource_pool_created_event_form_dict = resource_pool_created_event.from_dict(resource_pool_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


