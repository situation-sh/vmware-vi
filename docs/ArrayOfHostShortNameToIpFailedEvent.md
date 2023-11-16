# ArrayOfHostShortNameToIpFailedEvent

A boxed array of *HostShortNameToIpFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostShortNameToIpFailedEvent]**](HostShortNameToIpFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_short_name_to_ip_failed_event import ArrayOfHostShortNameToIpFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostShortNameToIpFailedEvent from a JSON string
array_of_host_short_name_to_ip_failed_event_instance = ArrayOfHostShortNameToIpFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostShortNameToIpFailedEvent.to_json()

# convert the object into a dict
array_of_host_short_name_to_ip_failed_event_dict = array_of_host_short_name_to_ip_failed_event_instance.to_dict()
# create an instance of ArrayOfHostShortNameToIpFailedEvent from a dict
array_of_host_short_name_to_ip_failed_event_form_dict = array_of_host_short_name_to_ip_failed_event.from_dict(array_of_host_short_name_to_ip_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


