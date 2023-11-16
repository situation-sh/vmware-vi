# ResourcePoolEventArgument

The event argument is a ResourcePool object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.resource_pool_event_argument import ResourcePoolEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolEventArgument from a JSON string
resource_pool_event_argument_instance = ResourcePoolEventArgument.from_json(json)
# print the JSON string representation of the object
print ResourcePoolEventArgument.to_json()

# convert the object into a dict
resource_pool_event_argument_dict = resource_pool_event_argument_instance.to_dict()
# create an instance of ResourcePoolEventArgument from a dict
resource_pool_event_argument_form_dict = resource_pool_event_argument.from_dict(resource_pool_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


