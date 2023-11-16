# HostAddedEvent

This event records the addition of a host to VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_added_event import HostAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostAddedEvent from a JSON string
host_added_event_instance = HostAddedEvent.from_json(json)
# print the JSON string representation of the object
print HostAddedEvent.to_json()

# convert the object into a dict
host_added_event_dict = host_added_event_instance.to_dict()
# create an instance of HostAddedEvent from a dict
host_added_event_form_dict = host_added_event.from_dict(host_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


