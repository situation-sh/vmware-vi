# ResourcePoolEvent

This event is the base class for all resource pool events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_pool** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.resource_pool_event import ResourcePoolEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolEvent from a JSON string
resource_pool_event_instance = ResourcePoolEvent.from_json(json)
# print the JSON string representation of the object
print ResourcePoolEvent.to_json()

# convert the object into a dict
resource_pool_event_dict = resource_pool_event_instance.to_dict()
# create an instance of ResourcePoolEvent from a dict
resource_pool_event_form_dict = resource_pool_event.from_dict(resource_pool_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


