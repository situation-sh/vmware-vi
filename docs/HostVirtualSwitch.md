# HostVirtualSwitch

The virtual switch is a software entity to which multiple virtual network adapters can connect to create a virtual network.  It can also be bridged to a physical network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the virtual switch.  Maximum length is 32 characters.  | 
**key** | **str** | The virtual switch key.  | 
**num_ports** | **int** | The number of ports that this virtual switch currently has.  | 
**num_ports_available** | **int** | The number of ports that are available on this virtual switch.  There are a number of networking services that utilize a port on the virtual switch and are not accounted for in the Port array of a PortGroup. For example, each physical NIC attached to a virtual switch consumes one port. This property should be used when attempting to implement admission control for new services attaching to virtual switches.  | 
**mtu** | **int** | The maximum transmission unit (MTU) associated with this virtual switch in bytes.  ***Since:*** VI API 2.5  | [optional] 
**portgroup** | [**List[HostPortGroup]**](HostPortGroup.md) | The list of port groups configured for this virtual switch.  | [optional] 
**pnic** | [**List[PhysicalNic]**](PhysicalNic.md) | The set of physical network adapters associated with this bridge.  | [optional] 
**spec** | [**HostVirtualSwitchSpec**](HostVirtualSwitchSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_virtual_switch import HostVirtualSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitch from a JSON string
host_virtual_switch_instance = HostVirtualSwitch.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitch.to_json()

# convert the object into a dict
host_virtual_switch_dict = host_virtual_switch_instance.to_dict()
# create an instance of HostVirtualSwitch from a dict
host_virtual_switch_form_dict = host_virtual_switch.from_dict(host_virtual_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


