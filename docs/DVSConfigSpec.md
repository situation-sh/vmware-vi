# DVSConfigSpec

The *DVSConfigSpec* data object contains configuration data for a *DistributedVirtualSwitch*.  Use the *DistributedVirtualSwitch.ReconfigureDvs_Task* method to apply the configuration to the switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**config_version** | **str** | The version string of the configuration that this spec is trying to change.  This property is required in reconfiguring a switch and should be set to the same value as *DVSConfigInfo.configVersion*. This property is ignored during switch creation.  ***Since:*** vSphere API 4.0  | [optional] 
**name** | **str** | The name of the switch.  Must be unique in the parent folder.  ***Since:*** vSphere API 4.0  | [optional] 
**num_standalone_ports** | **int** | The number of standalone ports in the switch.  Standalone ports are ports that do not belong to any portgroup. If set to a number larger than number of existing standalone ports in the switch, new ports get created to meet the number. If set to a number smaller than the number of existing standalone ports, free ports (uplink ports excluded) are deleted to meet the number. If the set number cannot be met by deleting free standalone ports, a fault is raised.  ***Since:*** vSphere API 4.0  | [optional] 
**max_ports** | **int** | Deprecated as of vSphere API 5.0 The default value of this propoerty is maxint and there is no reason for users to change it to a lower value.  The maximum number of DistributedVirtualPorts allowed in the switch.  If specified in a reconfigure operation, this number cannot be smaller than the number of existing DistributedVirtualPorts.  ***Since:*** vSphere API 4.0  | [optional] 
**uplink_port_policy** | [**DVSUplinkPortPolicy**](DVSUplinkPortPolicy.md) |  | [optional] 
**uplink_portgroup** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The uplink portgroups.  ***Since:*** vSphere API 4.0  Refers instances of *DistributedVirtualPortgroup*.  | [optional] 
**default_port_config** | [**DVPortSetting**](DVPortSetting.md) |  | [optional] 
**host** | [**List[DistributedVirtualSwitchHostMemberConfigSpec]**](DistributedVirtualSwitchHostMemberConfigSpec.md) | The host member specification.  A particular host should have only one entry in this array. Duplicate entries for the same host will raise a fault. The host version should be compatible with the version of *DistributedVirtualSwitch*. Use *DistributedVirtualSwitchManager.QueryDvsCheckCompatibility* to check for compatibility.  ***Since:*** vSphere API 4.0  | [optional] 
**extension_key** | **str** | The key of the extension registered by a remote server that controls the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**description** | **str** | Set the description string of the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**policy** | [**DVSPolicy**](DVSPolicy.md) |  | [optional] 
**vendor_specific_config** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Set the opaque blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**contact** | [**DVSContactInfo**](DVSContactInfo.md) |  | [optional] 
**switch_ip_address** | **str** | IP address for the switch, specified using IPv4 dot notation.  IPv6 address is not supported for this property. The utility of this address is defined by other switch features. switchIpAddress would be ignored when IPFIX collector uses IPv6.  ***Since:*** vSphere API 5.0  | [optional] 
**default_proxy_switch_max_num_ports** | **int** | The default host proxy switch maximum port number  ***Since:*** vSphere API 5.1  | [optional] 
**infrastructure_traffic_resource_config** | [**List[DvsHostInfrastructureTrafficResource]**](DvsHostInfrastructureTrafficResource.md) | The host infrastructure traffic resource allocation specification.  Only the traffic class resource allocations identified in the list will be updated. The other traffic class resource allocations that are not specified will not change.  ***Since:*** vSphere API 6.0  | [optional] 
**net_resource_pool_traffic_resource_config** | [**List[DvsHostInfrastructureTrafficResource]**](DvsHostInfrastructureTrafficResource.md) | The dynamic host infrastructure traffic resource allocation specification.  ***Since:*** vSphere API 6.7  | [optional] 
**network_resource_control_version** | **str** | Indicates the Network Resource Control APIs that are supported on the switch.  Possible value can be of *DistributedVirtualSwitchNetworkResourceControlVersion_enum*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_config_spec import DVSConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DVSConfigSpec from a JSON string
dvs_config_spec_instance = DVSConfigSpec.from_json(json)
# print the JSON string representation of the object
print DVSConfigSpec.to_json()

# convert the object into a dict
dvs_config_spec_dict = dvs_config_spec_instance.to_dict()
# create an instance of DVSConfigSpec from a dict
dvs_config_spec_form_dict = dvs_config_spec.from_dict(dvs_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


