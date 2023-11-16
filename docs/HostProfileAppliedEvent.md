# HostProfileAppliedEvent

This event records that a Profile application was done on the host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEventArgument**](ProfileEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.host_profile_applied_event import HostProfileAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileAppliedEvent from a JSON string
host_profile_applied_event_instance = HostProfileAppliedEvent.from_json(json)
# print the JSON string representation of the object
print HostProfileAppliedEvent.to_json()

# convert the object into a dict
host_profile_applied_event_dict = host_profile_applied_event_instance.to_dict()
# create an instance of HostProfileAppliedEvent from a dict
host_profile_applied_event_form_dict = host_profile_applied_event.from_dict(host_profile_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


