# HostAddFailedEvent

This event records that adding a host failed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | 

## Example

```python
from vmware_vi.models.host_add_failed_event import HostAddFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostAddFailedEvent from a JSON string
host_add_failed_event_instance = HostAddFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostAddFailedEvent.to_json()

# convert the object into a dict
host_add_failed_event_dict = host_add_failed_event_instance.to_dict()
# create an instance of HostAddFailedEvent from a dict
host_add_failed_event_form_dict = host_add_failed_event.from_dict(host_add_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


