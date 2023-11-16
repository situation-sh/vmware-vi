# HostPortGroup

This data object type is used to describe port groups.  Port groups are used to group virtual network adapters on a virtual switch, associating them with networks and network policies. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  | [optional] 
**port** | [**List[HostPortGroupPort]**](HostPortGroupPort.md) | The ports that currently exist and are used on this port group.  | [optional] 
**vswitch** | [**HostVirtualSwitch**](HostVirtualSwitch.md) |  | [optional] 
**computed_policy** | [**HostNetworkPolicy**](HostNetworkPolicy.md) |  | 
**spec** | [**HostPortGroupSpec**](HostPortGroupSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_port_group import HostPortGroup

# TODO update the JSON string below
json = "{}"
# create an instance of HostPortGroup from a JSON string
host_port_group_instance = HostPortGroup.from_json(json)
# print the JSON string representation of the object
print HostPortGroup.to_json()

# convert the object into a dict
host_port_group_dict = host_port_group_instance.to_dict()
# create an instance of HostPortGroup from a dict
host_port_group_form_dict = host_port_group.from_dict(host_port_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


