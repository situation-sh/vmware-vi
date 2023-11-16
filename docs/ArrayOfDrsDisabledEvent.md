# ArrayOfDrsDisabledEvent

A boxed array of *DrsDisabledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsDisabledEvent]**](DrsDisabledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_disabled_event import ArrayOfDrsDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsDisabledEvent from a JSON string
array_of_drs_disabled_event_instance = ArrayOfDrsDisabledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsDisabledEvent.to_json()

# convert the object into a dict
array_of_drs_disabled_event_dict = array_of_drs_disabled_event_instance.to_dict()
# create an instance of ArrayOfDrsDisabledEvent from a dict
array_of_drs_disabled_event_form_dict = array_of_drs_disabled_event.from_dict(array_of_drs_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


