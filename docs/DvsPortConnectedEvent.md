# DvsPortConnectedEvent

A port is connected in the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **str** | The port key.  ***Since:*** vSphere API 4.0  | 
**connectee** | [**DistributedVirtualSwitchPortConnectee**](DistributedVirtualSwitchPortConnectee.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_port_connected_event import DvsPortConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortConnectedEvent from a JSON string
dvs_port_connected_event_instance = DvsPortConnectedEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortConnectedEvent.to_json()

# convert the object into a dict
dvs_port_connected_event_dict = dvs_port_connected_event_instance.to_dict()
# create an instance of DvsPortConnectedEvent from a dict
dvs_port_connected_event_form_dict = dvs_port_connected_event.from_dict(dvs_port_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


