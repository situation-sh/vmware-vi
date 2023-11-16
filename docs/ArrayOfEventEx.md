# ArrayOfEventEx

A boxed array of *EventEx*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventEx]**](EventEx.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_ex import ArrayOfEventEx

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventEx from a JSON string
array_of_event_ex_instance = ArrayOfEventEx.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventEx.to_json()

# convert the object into a dict
array_of_event_ex_dict = array_of_event_ex_instance.to_dict()
# create an instance of ArrayOfEventEx from a dict
array_of_event_ex_form_dict = array_of_event_ex.from_dict(array_of_event_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


