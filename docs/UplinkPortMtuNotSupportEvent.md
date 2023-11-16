# UplinkPortMtuNotSupportEvent

Mtu health check status of an uplink port is changed, and in the latest mtu health check, not all the vlans' MTU setting on physical switch allows vSphere Distributed Switch max MTU size packets passing.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.uplink_port_mtu_not_support_event import UplinkPortMtuNotSupportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UplinkPortMtuNotSupportEvent from a JSON string
uplink_port_mtu_not_support_event_instance = UplinkPortMtuNotSupportEvent.from_json(json)
# print the JSON string representation of the object
print UplinkPortMtuNotSupportEvent.to_json()

# convert the object into a dict
uplink_port_mtu_not_support_event_dict = uplink_port_mtu_not_support_event_instance.to_dict()
# create an instance of UplinkPortMtuNotSupportEvent from a dict
uplink_port_mtu_not_support_event_form_dict = uplink_port_mtu_not_support_event.from_dict(uplink_port_mtu_not_support_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


