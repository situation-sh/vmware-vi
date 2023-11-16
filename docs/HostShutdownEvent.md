# HostShutdownEvent

This event records the shutdown of a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the host shutdown.  | 

## Example

```python
from vmware_vi.models.host_shutdown_event import HostShutdownEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostShutdownEvent from a JSON string
host_shutdown_event_instance = HostShutdownEvent.from_json(json)
# print the JSON string representation of the object
print HostShutdownEvent.to_json()

# convert the object into a dict
host_shutdown_event_dict = host_shutdown_event_instance.to_dict()
# create an instance of HostShutdownEvent from a dict
host_shutdown_event_form_dict = host_shutdown_event.from_dict(host_shutdown_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


