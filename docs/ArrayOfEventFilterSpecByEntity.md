# ArrayOfEventFilterSpecByEntity

A boxed array of *EventFilterSpecByEntity*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventFilterSpecByEntity]**](EventFilterSpecByEntity.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_filter_spec_by_entity import ArrayOfEventFilterSpecByEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventFilterSpecByEntity from a JSON string
array_of_event_filter_spec_by_entity_instance = ArrayOfEventFilterSpecByEntity.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventFilterSpecByEntity.to_json()

# convert the object into a dict
array_of_event_filter_spec_by_entity_dict = array_of_event_filter_spec_by_entity_instance.to_dict()
# create an instance of ArrayOfEventFilterSpecByEntity from a dict
array_of_event_filter_spec_by_entity_form_dict = array_of_event_filter_spec_by_entity.from_dict(array_of_event_filter_spec_by_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


