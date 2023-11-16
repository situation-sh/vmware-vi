# DVPortgroupConfigSpec

The *DVPortgroupConfigSpec* data object contains configuration data for a *DistributedVirtualPortgroup*.  Use the *DistributedVirtualPortgroup.ReconfigureDVPortgroup_Task* method to apply the configuration to the portgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**config_version** | **str** | Version string of the configuration that this spec is trying to change.  This property is required in reconfiguring a portgroup and should be set to the same value as the *DVPortgroupConfigInfo.configVersion*. This property is ignored in creating a portgroup if set.  ***Since:*** vSphere API 4.0  | [optional] 
**name** | **str** | Name of the portgroup.  ***Since:*** vSphere API 4.0  | [optional] 
**num_ports** | **int** | Number of ports in the portgroup.  Setting this number larger than the number of existing ports in the portgroup causes new ports to be added to the portgroup to meet the number. Setting this property smaller than the number of existing ports deletes the free ports from the portgroup. If the number cannot be met by deleting free ports, a fault is raised. If new ports are added to the portgroup, they are also added to the switch. For portgroups of type ephemeral this property is ignored.  ***Since:*** vSphere API 4.0  | [optional] 
**port_name_format** | **str** | Format of the name of the ports when ports are created in the portgroup.  For details see *DVPortgroupConfigInfo.portNameFormat*.  ***Since:*** vSphere API 4.0  | [optional] 
**default_port_config** | [**DVPortSetting**](DVPortSetting.md) |  | [optional] 
**description** | **str** | Description of the portgroup.  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | Type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupPortgroupType_enum* for possible values.  ***Since:*** vSphere API 4.0  | [optional] 
**backing_type** | **str** | Backing type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupBackingType_enum* for possible values. The default value is \&quot;standard\&quot;  ***Since:*** vSphere API 7.0  | [optional] 
**scope** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Deprecated as of vSphere API 5.5.  Eligible entities that can connect to the port.  See *DVPortgroupConfigInfo*.*DVPortgroupConfigInfo.scope*.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*.  | [optional] 
**policy** | [**DVPortgroupPolicy**](DVPortgroupPolicy.md) |  | [optional] 
**vendor_specific_config** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**auto_expand** | **bool** | If set to true, this property ignores the limit on the number of ports in the portgroup.  When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.  Setting this property to true makes the portgroup a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.  ***Since:*** vSphere API 5.0  | [optional] 
**vm_vnic_network_resource_pool_key** | **str** | The key of virtual NIC network resource pool to be associated with a portgroup.  Setting this property to \&quot;-1\&quot;, would mean that this portgroup is not associated with any virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | [optional] 
**transport_zone_uuid** | **str** | The UUID of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0  | [optional] 
**transport_zone_name** | **str** | The name of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0  | [optional] 
**logical_switch_uuid** | **str** | The logical switch UUID, which is used by NSX portgroup  ***Since:*** vSphere API 7.0  | [optional] 
**segment_id** | **str** | The segment ID of logical switch  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.dv_portgroup_config_spec import DVPortgroupConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupConfigSpec from a JSON string
dv_portgroup_config_spec_instance = DVPortgroupConfigSpec.from_json(json)
# print the JSON string representation of the object
print DVPortgroupConfigSpec.to_json()

# convert the object into a dict
dv_portgroup_config_spec_dict = dv_portgroup_config_spec_instance.to_dict()
# create an instance of DVPortgroupConfigSpec from a dict
dv_portgroup_config_spec_form_dict = dv_portgroup_config_spec.from_dict(dv_portgroup_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


