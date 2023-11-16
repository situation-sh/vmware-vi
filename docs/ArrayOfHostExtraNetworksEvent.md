# ArrayOfHostExtraNetworksEvent

A boxed array of *HostExtraNetworksEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostExtraNetworksEvent]**](HostExtraNetworksEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_extra_networks_event import ArrayOfHostExtraNetworksEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostExtraNetworksEvent from a JSON string
array_of_host_extra_networks_event_instance = ArrayOfHostExtraNetworksEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostExtraNetworksEvent.to_json()

# convert the object into a dict
array_of_host_extra_networks_event_dict = array_of_host_extra_networks_event_instance.to_dict()
# create an instance of ArrayOfHostExtraNetworksEvent from a dict
array_of_host_extra_networks_event_form_dict = array_of_host_extra_networks_event.from_dict(array_of_host_extra_networks_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


