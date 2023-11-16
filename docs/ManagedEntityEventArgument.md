# ManagedEntityEventArgument

The general event argument for a managed entity. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.managed_entity_event_argument import ManagedEntityEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEntityEventArgument from a JSON string
managed_entity_event_argument_instance = ManagedEntityEventArgument.from_json(json)
# print the JSON string representation of the object
print ManagedEntityEventArgument.to_json()

# convert the object into a dict
managed_entity_event_argument_dict = managed_entity_event_argument_instance.to_dict()
# create an instance of ManagedEntityEventArgument from a dict
managed_entity_event_argument_form_dict = managed_entity_event_argument.from_dict(managed_entity_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


