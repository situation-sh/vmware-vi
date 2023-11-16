# DVSNetworkResourceManagementCapability

Dataobject representing the feature capabilities of network resource management supported by the vSphere Distributed Switch.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_resource_management_supported** | **bool** | Indicates whether network I/O control is supported on the vSphere Distributed Switch.  Network I/O control is supported in vSphere Distributed Switch Version 4.1 or later.  ***Since:*** vSphere API 5.0  | 
**network_resource_pool_high_share_value** | **int** | High share level (*SharesLevel_enum*.*high*) for *DVSNetworkResourcePoolAllocationInfo*.*DVSNetworkResourcePoolAllocationInfo.shares*.  The &lt;code&gt;networkResourcePoolHighshareValue&lt;/code&gt; property implicitly defines the legal range of share values to be between 1 and this value. This property also defines values for other level types, such as *normal* being one half of this value and *low* being one fourth of this value. This feature is supported in vSphere Distributed Switch Version 4.1 or later.  ***Since:*** vSphere API 5.0  | 
**qos_supported** | **bool** | Indicates whether Qos Tag(802.1p priority tag)is supported on the vSphere Distributed Switch.  Qos Tag is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0  | 
**user_defined_network_resource_pools_supported** | **bool** | Indicates whether the switch supports creating user defined resource pools.  This feature is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0  | 
**network_resource_control_version3_supported** | **bool** | Flag to indicate whether Network Resource Control version 3 is supported.  The API supported by Network Resouce Control version 3 include: 1. VM virtual NIC network resource specification    *VirtualEthernetCardResourceAllocation* 2. VM virtual NIC network resource pool specification    *DVSVmVnicNetworkResourcePool* 3. Host infrastructure traffic network resource specification    *DvsHostInfrastructureTrafficResource*     Network Resource Control version 3 is supported for Switch Version 6.0 or later.  ***Since:*** vSphere API 6.0  | [optional] 
**user_defined_infra_traffic_pool_supported** | **bool** | Indicates whether user defined infrastructure traffic pool supported in vSphere Distributed Switch.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.dvs_network_resource_management_capability import DVSNetworkResourceManagementCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSNetworkResourceManagementCapability from a JSON string
dvs_network_resource_management_capability_instance = DVSNetworkResourceManagementCapability.from_json(json)
# print the JSON string representation of the object
print DVSNetworkResourceManagementCapability.to_json()

# convert the object into a dict
dvs_network_resource_management_capability_dict = dvs_network_resource_management_capability_instance.to_dict()
# create an instance of DVSNetworkResourceManagementCapability from a dict
dvs_network_resource_management_capability_form_dict = dvs_network_resource_management_capability.from_dict(dvs_network_resource_management_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


