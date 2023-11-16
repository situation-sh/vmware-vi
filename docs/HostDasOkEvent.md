# HostDasOkEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records when HA on a host returns to normal after an error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_das_ok_event import HostDasOkEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDasOkEvent from a JSON string
host_das_ok_event_instance = HostDasOkEvent.from_json(json)
# print the JSON string representation of the object
print HostDasOkEvent.to_json()

# convert the object into a dict
host_das_ok_event_dict = host_das_ok_event_instance.to_dict()
# create an instance of HostDasOkEvent from a dict
host_das_ok_event_form_dict = host_das_ok_event.from_dict(host_das_ok_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


