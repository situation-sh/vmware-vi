# DVSNetworkResourcePoolConfigSpec

The *DVSNetworkResourcePoolConfigSpec* data object contains properties to create or update a network resource pool for a distributed virtual switch.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**key** | **str** | Key of the network resource pool.  The property is ignored for *DistributedVirtualSwitch*.*DistributedVirtualSwitch.AddNetworkResourcePool* operations.  ***Since:*** vSphere API 4.1  | 
**config_version** | **str** | Unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.  If you specify the configuration version when you update the resource configuration, the Server will apply the changes only if the specified identifier matches the current *DVSNetworkResourcePool*.*DVSNetworkResourcePool.configVersion* value. You can use this field to guard against updates that may have occurred between the time when the client reads *DVSNetworkResourcePool.configVersion* and when the configuration is applied.  ***Since:*** vSphere API 4.1  | [optional] 
**allocation_info** | [**DVSNetworkResourcePoolAllocationInfo**](DVSNetworkResourcePoolAllocationInfo.md) |  | [optional] 
**name** | **str** | User defined name for the resource pool.  The property is required for *DistributedVirtualSwitch*.*DistributedVirtualSwitch.AddNetworkResourcePool* operations.  ***Since:*** vSphere API 5.0  | [optional] 
**description** | **str** | User-defined description for the resource pool.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_network_resource_pool_config_spec import DVSNetworkResourcePoolConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DVSNetworkResourcePoolConfigSpec from a JSON string
dvs_network_resource_pool_config_spec_instance = DVSNetworkResourcePoolConfigSpec.from_json(json)
# print the JSON string representation of the object
print DVSNetworkResourcePoolConfigSpec.to_json()

# convert the object into a dict
dvs_network_resource_pool_config_spec_dict = dvs_network_resource_pool_config_spec_instance.to_dict()
# create an instance of DVSNetworkResourcePoolConfigSpec from a dict
dvs_network_resource_pool_config_spec_form_dict = dvs_network_resource_pool_config_spec.from_dict(dvs_network_resource_pool_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


