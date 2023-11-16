# ArrayOfEventArgDesc

A boxed array of *EventArgDesc*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventArgDesc]**](EventArgDesc.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_arg_desc import ArrayOfEventArgDesc

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventArgDesc from a JSON string
array_of_event_arg_desc_instance = ArrayOfEventArgDesc.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventArgDesc.to_json()

# convert the object into a dict
array_of_event_arg_desc_dict = array_of_event_arg_desc_instance.to_dict()
# create an instance of ArrayOfEventArgDesc from a dict
array_of_event_arg_desc_form_dict = array_of_event_arg_desc.from_dict(array_of_event_arg_desc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


