# ArrayOfHostVnicConnectedToCustomizedDVPortEvent

A boxed array of *HostVnicConnectedToCustomizedDVPortEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVnicConnectedToCustomizedDVPortEvent]**](HostVnicConnectedToCustomizedDVPortEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vnic_connected_to_customized_dv_port_event import ArrayOfHostVnicConnectedToCustomizedDVPortEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVnicConnectedToCustomizedDVPortEvent from a JSON string
array_of_host_vnic_connected_to_customized_dv_port_event_instance = ArrayOfHostVnicConnectedToCustomizedDVPortEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVnicConnectedToCustomizedDVPortEvent.to_json()

# convert the object into a dict
array_of_host_vnic_connected_to_customized_dv_port_event_dict = array_of_host_vnic_connected_to_customized_dv_port_event_instance.to_dict()
# create an instance of ArrayOfHostVnicConnectedToCustomizedDVPortEvent from a dict
array_of_host_vnic_connected_to_customized_dv_port_event_form_dict = array_of_host_vnic_connected_to_customized_dv_port_event.from_dict(array_of_host_vnic_connected_to_customized_dv_port_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


