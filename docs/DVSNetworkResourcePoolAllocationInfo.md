# DVSNetworkResourcePoolAllocationInfo

Resource allocation information for a network resource pool.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum allowed usage for network clients belonging to this resource pool per host.  The utilization of network clients belonging to this resource pool will not exceed the specified limit even if there are available network resources. If set to -1, then there is no limit on the network resource usage for clients belonging to this resource pool. Units are in Mbits/sec. When setting the allocation of a particular resource pool, if the property is unset, it is treated as no change and the property is not updated. An unset limit value while reading back the allocation information of a network resource pool indicates that there is no limit on the network resource usage for the clients belonging to this resource group.  ***Since:*** vSphere API 4.1  | [optional] 
**shares** | [**SharesInfo**](SharesInfo.md) |  | [optional] 
**priority_tag** | **int** | 802.1p tag to be used for this resource pool.  The tag is a priority value in the range 0..7 for Quality of Service operations on network traffic.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_network_resource_pool_allocation_info import DVSNetworkResourcePoolAllocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVSNetworkResourcePoolAllocationInfo from a JSON string
dvs_network_resource_pool_allocation_info_instance = DVSNetworkResourcePoolAllocationInfo.from_json(json)
# print the JSON string representation of the object
print DVSNetworkResourcePoolAllocationInfo.to_json()

# convert the object into a dict
dvs_network_resource_pool_allocation_info_dict = dvs_network_resource_pool_allocation_info_instance.to_dict()
# create an instance of DVSNetworkResourcePoolAllocationInfo from a dict
dvs_network_resource_pool_allocation_info_form_dict = dvs_network_resource_pool_allocation_info.from_dict(dvs_network_resource_pool_allocation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


