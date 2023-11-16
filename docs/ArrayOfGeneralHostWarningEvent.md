# ArrayOfGeneralHostWarningEvent

A boxed array of *GeneralHostWarningEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralHostWarningEvent]**](GeneralHostWarningEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_host_warning_event import ArrayOfGeneralHostWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralHostWarningEvent from a JSON string
array_of_general_host_warning_event_instance = ArrayOfGeneralHostWarningEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralHostWarningEvent.to_json()

# convert the object into a dict
array_of_general_host_warning_event_dict = array_of_general_host_warning_event_instance.to_dict()
# create an instance of ArrayOfGeneralHostWarningEvent from a dict
array_of_general_host_warning_event_form_dict = array_of_general_host_warning_event.from_dict(array_of_general_host_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


