# ResourcePoolReconfiguredEvent

This event records when a resource pool configuration is changed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.resource_pool_reconfigured_event import ResourcePoolReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolReconfiguredEvent from a JSON string
resource_pool_reconfigured_event_instance = ResourcePoolReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ResourcePoolReconfiguredEvent.to_json()

# convert the object into a dict
resource_pool_reconfigured_event_dict = resource_pool_reconfigured_event_instance.to_dict()
# create an instance of ResourcePoolReconfiguredEvent from a dict
resource_pool_reconfigured_event_form_dict = resource_pool_reconfigured_event.from_dict(resource_pool_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


