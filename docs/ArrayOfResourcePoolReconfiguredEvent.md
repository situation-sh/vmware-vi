# ArrayOfResourcePoolReconfiguredEvent

A boxed array of *ResourcePoolReconfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolReconfiguredEvent]**](ResourcePoolReconfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_reconfigured_event import ArrayOfResourcePoolReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolReconfiguredEvent from a JSON string
array_of_resource_pool_reconfigured_event_instance = ArrayOfResourcePoolReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolReconfiguredEvent.to_json()

# convert the object into a dict
array_of_resource_pool_reconfigured_event_dict = array_of_resource_pool_reconfigured_event_instance.to_dict()
# create an instance of ArrayOfResourcePoolReconfiguredEvent from a dict
array_of_resource_pool_reconfigured_event_form_dict = array_of_resource_pool_reconfigured_event.from_dict(array_of_resource_pool_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


