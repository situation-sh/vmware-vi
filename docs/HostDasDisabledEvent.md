# HostDasDisabledEvent

This event records when HA has been disabled on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_das_disabled_event import HostDasDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDasDisabledEvent from a JSON string
host_das_disabled_event_instance = HostDasDisabledEvent.from_json(json)
# print the JSON string representation of the object
print HostDasDisabledEvent.to_json()

# convert the object into a dict
host_das_disabled_event_dict = host_das_disabled_event_instance.to_dict()
# create an instance of HostDasDisabledEvent from a dict
host_das_disabled_event_form_dict = host_das_disabled_event.from_dict(host_das_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


