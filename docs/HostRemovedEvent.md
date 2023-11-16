# HostRemovedEvent

This event records the removal of a host from VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_removed_event import HostRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostRemovedEvent from a JSON string
host_removed_event_instance = HostRemovedEvent.from_json(json)
# print the JSON string representation of the object
print HostRemovedEvent.to_json()

# convert the object into a dict
host_removed_event_dict = host_removed_event_instance.to_dict()
# create an instance of HostRemovedEvent from a dict
host_removed_event_form_dict = host_removed_event.from_dict(host_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


