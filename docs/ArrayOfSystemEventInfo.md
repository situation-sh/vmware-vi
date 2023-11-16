# ArrayOfSystemEventInfo

A boxed array of *SystemEventInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SystemEventInfo]**](SystemEventInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_system_event_info import ArrayOfSystemEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSystemEventInfo from a JSON string
array_of_system_event_info_instance = ArrayOfSystemEventInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfSystemEventInfo.to_json()

# convert the object into a dict
array_of_system_event_info_dict = array_of_system_event_info_instance.to_dict()
# create an instance of ArrayOfSystemEventInfo from a dict
array_of_system_event_info_form_dict = array_of_system_event_info.from_dict(array_of_system_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


