# ArrayOfHostConfigAppliedEvent

A boxed array of *HostConfigAppliedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigAppliedEvent]**](HostConfigAppliedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_applied_event import ArrayOfHostConfigAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigAppliedEvent from a JSON string
array_of_host_config_applied_event_instance = ArrayOfHostConfigAppliedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigAppliedEvent.to_json()

# convert the object into a dict
array_of_host_config_applied_event_dict = array_of_host_config_applied_event_instance.to_dict()
# create an instance of ArrayOfHostConfigAppliedEvent from a dict
array_of_host_config_applied_event_form_dict = array_of_host_config_applied_event.from_dict(array_of_host_config_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


