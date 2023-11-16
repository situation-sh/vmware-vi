# ArrayOfDrsEnabledEvent

A boxed array of *DrsEnabledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsEnabledEvent]**](DrsEnabledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_enabled_event import ArrayOfDrsEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsEnabledEvent from a JSON string
array_of_drs_enabled_event_instance = ArrayOfDrsEnabledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsEnabledEvent.to_json()

# convert the object into a dict
array_of_drs_enabled_event_dict = array_of_drs_enabled_event_instance.to_dict()
# create an instance of ArrayOfDrsEnabledEvent from a dict
array_of_drs_enabled_event_form_dict = array_of_drs_enabled_event.from_dict(array_of_drs_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


