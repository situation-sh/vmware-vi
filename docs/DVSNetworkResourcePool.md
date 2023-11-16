# DVSNetworkResourcePool

Deprecated as of vSphere API 6.0 Use *DvsHostInfrastructureTrafficResource* to manage resource allocation for host infrastructure traffic. Use *DVSVmVnicNetworkResourcePool* to manage resource allocation for user defined pools.  The *DVSNetworkResourcePool* data object describes the resource configuration and management of network resource pools.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the network resource pool.  ***Since:*** vSphere API 4.1  | 
**name** | **str** | Name of the network resource pool.  ***Since:*** vSphere API 4.1  | [optional] 
**description** | **str** | Description of the network resource pool.  ***Since:*** vSphere API 4.1  | [optional] 
**config_version** | **str** | Configuration version for the network resource pool.  ***Since:*** vSphere API 4.1  | 
**allocation_info** | [**DVSNetworkResourcePoolAllocationInfo**](DVSNetworkResourcePoolAllocationInfo.md) |  | 

## Example

```python
from vmware_vi.models.dvs_network_resource_pool import DVSNetworkResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of DVSNetworkResourcePool from a JSON string
dvs_network_resource_pool_instance = DVSNetworkResourcePool.from_json(json)
# print the JSON string representation of the object
print DVSNetworkResourcePool.to_json()

# convert the object into a dict
dvs_network_resource_pool_dict = dvs_network_resource_pool_instance.to_dict()
# create an instance of DVSNetworkResourcePool from a dict
dvs_network_resource_pool_form_dict = dvs_network_resource_pool.from_dict(dvs_network_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


