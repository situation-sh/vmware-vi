# DVSConfigInfo

Configuration of a *DistributedVirtualSwitch*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Generated UUID of the switch.  Unique across vCenter Server inventory and instances.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of the switch.  ***Since:*** vSphere API 4.0  | 
**num_standalone_ports** | **int** | Number of standalone ports in the switch.  Standalone ports are ports that do not belong to any portgroup.  ***Since:*** vSphere API 4.0  | 
**num_ports** | **int** | Current number of ports, not including conflict ports.  ***Since:*** vSphere API 4.0  | 
**max_ports** | **int** | Maximum number of ports allowed in the switch, not including conflict ports.  ***Since:*** vSphere API 4.0  | 
**uplink_port_policy** | [**DVSUplinkPortPolicy**](DVSUplinkPortPolicy.md) |  | 
**uplink_portgroup** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of uplink portgroups.  When adding host members, the server uses the *DVSConfigInfo.uplinkPortPolicy* to create a number of uplink ports for the host. If portgroups are shown here, those uplink ports will be added to the portgroups, with uplink ports evenly spread among the portgroups.  ***Since:*** vSphere API 4.0  Refers instances of *DistributedVirtualPortgroup*.  | [optional] 
**default_port_config** | [**DVPortSetting**](DVPortSetting.md) |  | 
**host** | [**List[DistributedVirtualSwitchHostMember]**](DistributedVirtualSwitchHostMember.md) | Hosts that join the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 
**target_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 
**extension_key** | **str** | Key of the extension registered by the remote server that controls the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**vendor_specific_config** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**policy** | [**DVSPolicy**](DVSPolicy.md) |  | [optional] 
**description** | **str** | Description string for the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**config_version** | **str** | Version string of the configuration.  ***Since:*** vSphere API 4.0  | 
**contact** | [**DVSContactInfo**](DVSContactInfo.md) |  | 
**switch_ip_address** | **str** | IP address for the switch, specified using IPv4 dot notation.  The utility of this address is defined by other switch features.  ***Since:*** vSphere API 5.0  | [optional] 
**create_time** | **datetime** | Create time of the switch.  ***Since:*** vSphere API 4.0  | 
**network_resource_management_enabled** | **bool** | Boolean to indicate if network I/O control is enabled on the switch.  ***Since:*** vSphere API 4.1  | 
**default_proxy_switch_max_num_ports** | **int** | Default host proxy switch maximum port number  ***Since:*** vSphere API 5.1  | [optional] 
**health_check_config** | [**List[DVSHealthCheckConfig]**](DVSHealthCheckConfig.md) | VDS health check configuration.  ***Since:*** vSphere API 5.1  | [optional] 
**infrastructure_traffic_resource_config** | [**List[DvsHostInfrastructureTrafficResource]**](DvsHostInfrastructureTrafficResource.md) | Host infrastructure traffic class resource configuration.  ***Since:*** vSphere API 6.0  | [optional] 
**net_resource_pool_traffic_resource_config** | [**List[DvsHostInfrastructureTrafficResource]**](DvsHostInfrastructureTrafficResource.md) | Dynamic Host infrastructure traffic class resource configuration.  ***Since:*** vSphere API 6.7  | [optional] 
**network_resource_control_version** | **str** | Network resource control version of the switch.  Possible value can be of *DistributedVirtualSwitchNetworkResourceControlVersion_enum*.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_vnic_network_resource_pool** | [**List[DVSVmVnicNetworkResourcePool]**](DVSVmVnicNetworkResourcePool.md) | The Virtual NIC network resource pool information for the switch.  ***Since:*** vSphere API 6.0  | [optional] 
**pnic_capacity_ratio_for_reservation** | **int** | The percentage of physical nic link speed *PhysicalNicLinkInfo.speedMb* available for infrastructure traffic reservation.  If this value is 75, then for a 1Gbps physical nic, only 750Mbps is allowed for all infrastructure traffic reservations.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_config_info import DVSConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVSConfigInfo from a JSON string
dvs_config_info_instance = DVSConfigInfo.from_json(json)
# print the JSON string representation of the object
print DVSConfigInfo.to_json()

# convert the object into a dict
dvs_config_info_dict = dvs_config_info_instance.to_dict()
# create an instance of DVSConfigInfo from a dict
dvs_config_info_form_dict = dvs_config_info.from_dict(dvs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


