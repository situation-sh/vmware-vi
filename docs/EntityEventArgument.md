# EntityEventArgument

The event argument is a managed entity object.  Subclasses of this type distinguish the different managed entities referenced in event objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the entity, including its full path from the root of the inventory.  | 

## Example

```python
from vmware_vi.models.entity_event_argument import EntityEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of EntityEventArgument from a JSON string
entity_event_argument_instance = EntityEventArgument.from_json(json)
# print the JSON string representation of the object
print EntityEventArgument.to_json()

# convert the object into a dict
entity_event_argument_dict = entity_event_argument_instance.to_dict()
# create an instance of EntityEventArgument from a dict
entity_event_argument_form_dict = entity_event_argument.from_dict(entity_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


