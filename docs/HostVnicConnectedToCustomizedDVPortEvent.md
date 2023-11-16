# HostVnicConnectedToCustomizedDVPortEvent

This event records when some host Virtual NICs were reconfigured to use DVPorts with port level configuration, which might be different from the DVportgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic** | [**VnicPortArgument**](VnicPortArgument.md) |  | 
**prev_port_key** | **str** | Information about the previous Virtual NIC that is using the DVport.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_vnic_connected_to_customized_dv_port_event import HostVnicConnectedToCustomizedDVPortEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostVnicConnectedToCustomizedDVPortEvent from a JSON string
host_vnic_connected_to_customized_dv_port_event_instance = HostVnicConnectedToCustomizedDVPortEvent.from_json(json)
# print the JSON string representation of the object
print HostVnicConnectedToCustomizedDVPortEvent.to_json()

# convert the object into a dict
host_vnic_connected_to_customized_dv_port_event_dict = host_vnic_connected_to_customized_dv_port_event_instance.to_dict()
# create an instance of HostVnicConnectedToCustomizedDVPortEvent from a dict
host_vnic_connected_to_customized_dv_port_event_form_dict = host_vnic_connected_to_customized_dv_port_event.from_dict(host_vnic_connected_to_customized_dv_port_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


