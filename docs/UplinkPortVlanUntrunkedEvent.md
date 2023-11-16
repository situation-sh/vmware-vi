# UplinkPortVlanUntrunkedEvent

Vlans health check status of an uplink port is changed, and in the latest vlan health check, not all the vlans are trunked by the physical switch connected to the uplink port.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.uplink_port_vlan_untrunked_event import UplinkPortVlanUntrunkedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UplinkPortVlanUntrunkedEvent from a JSON string
uplink_port_vlan_untrunked_event_instance = UplinkPortVlanUntrunkedEvent.from_json(json)
# print the JSON string representation of the object
print UplinkPortVlanUntrunkedEvent.to_json()

# convert the object into a dict
uplink_port_vlan_untrunked_event_dict = uplink_port_vlan_untrunked_event_instance.to_dict()
# create an instance of UplinkPortVlanUntrunkedEvent from a dict
uplink_port_vlan_untrunked_event_form_dict = uplink_port_vlan_untrunked_event.from_dict(uplink_port_vlan_untrunked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


