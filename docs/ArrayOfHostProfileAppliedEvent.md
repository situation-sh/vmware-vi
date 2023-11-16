# ArrayOfHostProfileAppliedEvent

A boxed array of *HostProfileAppliedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProfileAppliedEvent]**](HostProfileAppliedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_profile_applied_event import ArrayOfHostProfileAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProfileAppliedEvent from a JSON string
array_of_host_profile_applied_event_instance = ArrayOfHostProfileAppliedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProfileAppliedEvent.to_json()

# convert the object into a dict
array_of_host_profile_applied_event_dict = array_of_host_profile_applied_event_instance.to_dict()
# create an instance of ArrayOfHostProfileAppliedEvent from a dict
array_of_host_profile_applied_event_form_dict = array_of_host_profile_applied_event.from_dict(array_of_host_profile_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


