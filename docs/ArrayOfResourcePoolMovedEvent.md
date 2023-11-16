# ArrayOfResourcePoolMovedEvent

A boxed array of *ResourcePoolMovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolMovedEvent]**](ResourcePoolMovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_moved_event import ArrayOfResourcePoolMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolMovedEvent from a JSON string
array_of_resource_pool_moved_event_instance = ArrayOfResourcePoolMovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolMovedEvent.to_json()

# convert the object into a dict
array_of_resource_pool_moved_event_dict = array_of_resource_pool_moved_event_instance.to_dict()
# create an instance of ArrayOfResourcePoolMovedEvent from a dict
array_of_resource_pool_moved_event_form_dict = array_of_resource_pool_moved_event.from_dict(array_of_resource_pool_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


