# HostOpaqueSwitch

The OpaqueSwitch contains basic information about virtual switches that are managed by a management plane outside of vSphere.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**key** | **str** | The opaque switch ID.  ***Since:*** vSphere API 5.5  | 
**name** | **str** | The opaque switch name.  ***Since:*** vSphere API 5.5  | [optional] 
**pnic** | [**List[PhysicalNic]**](PhysicalNic.md) | The set of physical network adapters associated with this switch.  ***Since:*** vSphere API 5.5  | [optional] 
**pnic_zone** | [**List[HostOpaqueSwitchPhysicalNicZone]**](HostOpaqueSwitchPhysicalNicZone.md) | The IDs of networking zones associated with this switch.  ***Since:*** vSphere API 6.0  | [optional] 
**status** | **str** | Opaque switch status.  See *OpaqueSwitchState* for valid values.  ***Since:*** vSphere API 6.0  | [optional] 
**vtep** | [**List[HostVirtualNic]**](HostVirtualNic.md) | List of VTEPs associated with this switch.  ***Since:*** vSphere API 6.0  | [optional] 
**extra_config** | [**List[OptionValue]**](OptionValue.md) | Extra NSX specific properties for opaque switch.  ***Since:*** vSphere API 6.5  | [optional] 
**feature_capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | Array of host specific feature capabilities that the switch has.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_opaque_switch import HostOpaqueSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of HostOpaqueSwitch from a JSON string
host_opaque_switch_instance = HostOpaqueSwitch.from_json(json)
# print the JSON string representation of the object
print HostOpaqueSwitch.to_json()

# convert the object into a dict
host_opaque_switch_dict = host_opaque_switch_instance.to_dict()
# create an instance of HostOpaqueSwitch from a dict
host_opaque_switch_form_dict = host_opaque_switch.from_dict(host_opaque_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


