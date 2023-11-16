# DVSVmVnicNetworkResourcePool

DataObject describing the resource configuration and management of virtual NIC network resource pools.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | 
**name** | **str** | The name of the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | [optional] 
**description** | **str** | The description of the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | [optional] 
**config_version** | **str** | The config version for the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | 
**allocation_info** | [**DvsVmVnicResourceAllocation**](DvsVmVnicResourceAllocation.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvsvm_vnic_network_resource_pool import DVSVmVnicNetworkResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of DVSVmVnicNetworkResourcePool from a JSON string
dvsvm_vnic_network_resource_pool_instance = DVSVmVnicNetworkResourcePool.from_json(json)
# print the JSON string representation of the object
print DVSVmVnicNetworkResourcePool.to_json()

# convert the object into a dict
dvsvm_vnic_network_resource_pool_dict = dvsvm_vnic_network_resource_pool_instance.to_dict()
# create an instance of DVSVmVnicNetworkResourcePool from a dict
dvsvm_vnic_network_resource_pool_form_dict = dvsvm_vnic_network_resource_pool.from_dict(dvsvm_vnic_network_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


