# HostConfigAppliedEvent

This event records that a configuration was applied on a host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_config_applied_event import HostConfigAppliedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigAppliedEvent from a JSON string
host_config_applied_event_instance = HostConfigAppliedEvent.from_json(json)
# print the JSON string representation of the object
print HostConfigAppliedEvent.to_json()

# convert the object into a dict
host_config_applied_event_dict = host_config_applied_event_instance.to_dict()
# create an instance of HostConfigAppliedEvent from a dict
host_config_applied_event_form_dict = host_config_applied_event.from_dict(host_config_applied_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


