# ArrayOfHostIpChangedEvent

A boxed array of *HostIpChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpChangedEvent]**](HostIpChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_changed_event import ArrayOfHostIpChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpChangedEvent from a JSON string
array_of_host_ip_changed_event_instance = ArrayOfHostIpChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpChangedEvent.to_json()

# convert the object into a dict
array_of_host_ip_changed_event_dict = array_of_host_ip_changed_event_instance.to_dict()
# create an instance of ArrayOfHostIpChangedEvent from a dict
array_of_host_ip_changed_event_form_dict = array_of_host_ip_changed_event.from_dict(array_of_host_ip_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


