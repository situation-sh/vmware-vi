# ArrayOfHostNoAvailableNetworksEvent

A boxed array of *HostNoAvailableNetworksEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNoAvailableNetworksEvent]**](HostNoAvailableNetworksEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_no_available_networks_event import ArrayOfHostNoAvailableNetworksEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNoAvailableNetworksEvent from a JSON string
array_of_host_no_available_networks_event_instance = ArrayOfHostNoAvailableNetworksEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNoAvailableNetworksEvent.to_json()

# convert the object into a dict
array_of_host_no_available_networks_event_dict = array_of_host_no_available_networks_event_instance.to_dict()
# create an instance of ArrayOfHostNoAvailableNetworksEvent from a dict
array_of_host_no_available_networks_event_form_dict = array_of_host_no_available_networks_event.from_dict(array_of_host_no_available_networks_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


