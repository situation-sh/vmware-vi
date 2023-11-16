# ArrayOfHostIpToShortNameFailedEvent

A boxed array of *HostIpToShortNameFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpToShortNameFailedEvent]**](HostIpToShortNameFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_to_short_name_failed_event import ArrayOfHostIpToShortNameFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpToShortNameFailedEvent from a JSON string
array_of_host_ip_to_short_name_failed_event_instance = ArrayOfHostIpToShortNameFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpToShortNameFailedEvent.to_json()

# convert the object into a dict
array_of_host_ip_to_short_name_failed_event_dict = array_of_host_ip_to_short_name_failed_event_instance.to_dict()
# create an instance of ArrayOfHostIpToShortNameFailedEvent from a dict
array_of_host_ip_to_short_name_failed_event_form_dict = array_of_host_ip_to_short_name_failed_event.from_dict(array_of_host_ip_to_short_name_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


