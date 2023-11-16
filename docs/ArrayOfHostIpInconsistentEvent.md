# ArrayOfHostIpInconsistentEvent

A boxed array of *HostIpInconsistentEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpInconsistentEvent]**](HostIpInconsistentEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_inconsistent_event import ArrayOfHostIpInconsistentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpInconsistentEvent from a JSON string
array_of_host_ip_inconsistent_event_instance = ArrayOfHostIpInconsistentEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpInconsistentEvent.to_json()

# convert the object into a dict
array_of_host_ip_inconsistent_event_dict = array_of_host_ip_inconsistent_event_instance.to_dict()
# create an instance of ArrayOfHostIpInconsistentEvent from a dict
array_of_host_ip_inconsistent_event_form_dict = array_of_host_ip_inconsistent_event.from_dict(array_of_host_ip_inconsistent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


