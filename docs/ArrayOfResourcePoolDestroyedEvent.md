# ArrayOfResourcePoolDestroyedEvent

A boxed array of *ResourcePoolDestroyedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolDestroyedEvent]**](ResourcePoolDestroyedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_destroyed_event import ArrayOfResourcePoolDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolDestroyedEvent from a JSON string
array_of_resource_pool_destroyed_event_instance = ArrayOfResourcePoolDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolDestroyedEvent.to_json()

# convert the object into a dict
array_of_resource_pool_destroyed_event_dict = array_of_resource_pool_destroyed_event_instance.to_dict()
# create an instance of ArrayOfResourcePoolDestroyedEvent from a dict
array_of_resource_pool_destroyed_event_form_dict = array_of_resource_pool_destroyed_event.from_dict(array_of_resource_pool_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


