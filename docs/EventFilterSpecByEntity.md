# EventFilterSpecByEntity

This option specifies a managed entity used to filter event history.  If the specified managed entity is a Folder or a ResourcePool, the query will actually be performed on the entities contained within that Folder or ResourcePool, so you cannot query for events on Folders and ResourcePools themselves this way. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**recursion** | [**EventFilterSpecRecursionOptionEnum**](EventFilterSpecRecursionOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.event_filter_spec_by_entity import EventFilterSpecByEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterSpecByEntity from a JSON string
event_filter_spec_by_entity_instance = EventFilterSpecByEntity.from_json(json)
# print the JSON string representation of the object
print EventFilterSpecByEntity.to_json()

# convert the object into a dict
event_filter_spec_by_entity_dict = event_filter_spec_by_entity_instance.to_dict()
# create an instance of EventFilterSpecByEntity from a dict
event_filter_spec_by_entity_form_dict = event_filter_spec_by_entity.from_dict(event_filter_spec_by_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


