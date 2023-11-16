# HostDasEnabledEvent

This event records when HA has been enabled on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_das_enabled_event import HostDasEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDasEnabledEvent from a JSON string
host_das_enabled_event_instance = HostDasEnabledEvent.from_json(json)
# print the JSON string representation of the object
print HostDasEnabledEvent.to_json()

# convert the object into a dict
host_das_enabled_event_dict = host_das_enabled_event_instance.to_dict()
# create an instance of HostDasEnabledEvent from a dict
host_das_enabled_event_form_dict = host_das_enabled_event.from_dict(host_das_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


