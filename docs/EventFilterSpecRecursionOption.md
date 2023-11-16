# EventFilterSpecRecursionOption

A boxed *EventFilterSpecRecursionOption_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**EventFilterSpecRecursionOptionEnum**](EventFilterSpecRecursionOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.event_filter_spec_recursion_option import EventFilterSpecRecursionOption

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterSpecRecursionOption from a JSON string
event_filter_spec_recursion_option_instance = EventFilterSpecRecursionOption.from_json(json)
# print the JSON string representation of the object
print EventFilterSpecRecursionOption.to_json()

# convert the object into a dict
event_filter_spec_recursion_option_dict = event_filter_spec_recursion_option_instance.to_dict()
# create an instance of EventFilterSpecRecursionOption from a dict
event_filter_spec_recursion_option_form_dict = event_filter_spec_recursion_option.from_dict(event_filter_spec_recursion_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


