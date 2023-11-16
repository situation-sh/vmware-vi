# HostOvercommittedEvent

This event records when a host's capacity cannot satisfy resource configuration constraints.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_overcommitted_event import HostOvercommittedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostOvercommittedEvent from a JSON string
host_overcommitted_event_instance = HostOvercommittedEvent.from_json(json)
# print the JSON string representation of the object
print HostOvercommittedEvent.to_json()

# convert the object into a dict
host_overcommitted_event_dict = host_overcommitted_event_instance.to_dict()
# create an instance of HostOvercommittedEvent from a dict
host_overcommitted_event_form_dict = host_overcommitted_event.from_dict(host_overcommitted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


