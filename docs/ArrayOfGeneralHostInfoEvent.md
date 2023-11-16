# ArrayOfGeneralHostInfoEvent

A boxed array of *GeneralHostInfoEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralHostInfoEvent]**](GeneralHostInfoEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_host_info_event import ArrayOfGeneralHostInfoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralHostInfoEvent from a JSON string
array_of_general_host_info_event_instance = ArrayOfGeneralHostInfoEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralHostInfoEvent.to_json()

# convert the object into a dict
array_of_general_host_info_event_dict = array_of_general_host_info_event_instance.to_dict()
# create an instance of ArrayOfGeneralHostInfoEvent from a dict
array_of_general_host_info_event_form_dict = array_of_general_host_info_event.from_dict(array_of_general_host_info_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


