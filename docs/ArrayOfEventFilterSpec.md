# ArrayOfEventFilterSpec

A boxed array of *EventFilterSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventFilterSpec]**](EventFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_filter_spec import ArrayOfEventFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventFilterSpec from a JSON string
array_of_event_filter_spec_instance = ArrayOfEventFilterSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventFilterSpec.to_json()

# convert the object into a dict
array_of_event_filter_spec_dict = array_of_event_filter_spec_instance.to_dict()
# create an instance of ArrayOfEventFilterSpec from a dict
array_of_event_filter_spec_form_dict = array_of_event_filter_spec.from_dict(array_of_event_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


