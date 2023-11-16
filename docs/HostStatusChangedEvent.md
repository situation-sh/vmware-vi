# HostStatusChangedEvent

This event records when a host's overall status changed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_status_changed_event import HostStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostStatusChangedEvent from a JSON string
host_status_changed_event_instance = HostStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print HostStatusChangedEvent.to_json()

# convert the object into a dict
host_status_changed_event_dict = host_status_changed_event_instance.to_dict()
# create an instance of HostStatusChangedEvent from a dict
host_status_changed_event_form_dict = host_status_changed_event.from_dict(host_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


