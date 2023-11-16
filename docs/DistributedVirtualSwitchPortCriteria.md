# DistributedVirtualSwitchPortCriteria

The criteria specification for selecting ports.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**connected** | **bool** | If set, only the connected ports are qualified.  ***Since:*** vSphere API 4.0  | [optional] 
**active** | **bool** | If set, only the active ports are qualified.  ***Since:*** vSphere API 4.0  | [optional] 
**uplink_port** | **bool** | If set to true, only the uplink ports are qualified.  If set to false, only non-uplink ports are qualified.  ***Since:*** vSphere API 4.0  | [optional] 
**nsx_port** | **bool** | If set to true, only the NSX ports are qualified.  If set to false, only non-NSX ports are qualified. NSX ports are ports of NSX port group.  ***Since:*** vSphere API 7.0  | [optional] 
**scope** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**portgroup_key** | **List[str]** | The keys of the portgroup that is used for the scope of *DistributedVirtualSwitchPortCriteria.inside*.  If this property is unset, it means any portgroup. If *DistributedVirtualSwitchPortCriteria.inside* is unset, this property is ignored.  ***Since:*** vSphere API 4.0  | [optional] 
**inside** | **bool** | If unset, all ports in the switch are qualified.  If set to true, only ports inside *DistributedVirtualSwitchPortCriteria.portgroupKey* or any portgroup, if not set, are qualified. If set to false, only ports outside *DistributedVirtualSwitchPortCriteria.portgroupKey* or any portgroup, if not set, are qualified.  ***Since:*** vSphere API 4.0  | [optional] 
**port_key** | **List[str]** | If set, only the ports of which the key is in the array are qualified.  ***Since:*** vSphere API 4.0  | [optional] 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If set, only the ports that are present in one of the host are qualified.  ***Since:*** vSphere API 6.5  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_port_criteria import DistributedVirtualSwitchPortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchPortCriteria from a JSON string
distributed_virtual_switch_port_criteria_instance = DistributedVirtualSwitchPortCriteria.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchPortCriteria.to_json()

# convert the object into a dict
distributed_virtual_switch_port_criteria_dict = distributed_virtual_switch_port_criteria_instance.to_dict()
# create an instance of DistributedVirtualSwitchPortCriteria from a dict
distributed_virtual_switch_port_criteria_form_dict = distributed_virtual_switch_port_criteria.from_dict(distributed_virtual_switch_port_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


