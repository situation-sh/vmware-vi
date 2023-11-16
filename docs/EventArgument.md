# EventArgument

This is the base type for event argument types.  Event argument objects, which inherit from a common subtype, are used to manage supplementary properties of different kinds of event objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.event_argument import EventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of EventArgument from a JSON string
event_argument_instance = EventArgument.from_json(json)
# print the JSON string representation of the object
print EventArgument.to_json()

# convert the object into a dict
event_argument_dict = event_argument_instance.to_dict()
# create an instance of EventArgument from a dict
event_argument_form_dict = event_argument.from_dict(event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


