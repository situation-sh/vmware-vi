# ArrayOfResourcePoolEvent

A boxed array of *ResourcePoolEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolEvent]**](ResourcePoolEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_event import ArrayOfResourcePoolEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolEvent from a JSON string
array_of_resource_pool_event_instance = ArrayOfResourcePoolEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolEvent.to_json()

# convert the object into a dict
array_of_resource_pool_event_dict = array_of_resource_pool_event_instance.to_dict()
# create an instance of ArrayOfResourcePoolEvent from a dict
array_of_resource_pool_event_form_dict = array_of_resource_pool_event.from_dict(array_of_resource_pool_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


