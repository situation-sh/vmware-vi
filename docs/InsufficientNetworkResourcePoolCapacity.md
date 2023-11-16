# InsufficientNetworkResourcePoolCapacity

Insufficient network resource pool bandwidth  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_name** | **str** | Distributed Virtual Switch containing the resource pool having unsufficient network bandwitdh.  ***Since:*** vSphere API 6.0  | 
**dvs_uuid** | **str** | UUID of the distributed Virtual Switch containing the resource pool having unsufficient network bandwitdh.  ***Since:*** vSphere API 6.0  | 
**resource_pool_key** | **str** | Key of the resource pool on which network bandwidth is requested.  ***Since:*** vSphere API 6.0  | 
**available** | **int** | Network bandwidth available (in MBs) in the requested resource pool.  ***Since:*** vSphere API 6.0  | 
**requested** | **int** | Network bandwidth amount requested (in MBs).  ***Since:*** vSphere API 6.0  | 
**device** | **List[str]** | List of network devices that are requesting or already have requested bandwidth on the network resource pool.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.insufficient_network_resource_pool_capacity import InsufficientNetworkResourcePoolCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientNetworkResourcePoolCapacity from a JSON string
insufficient_network_resource_pool_capacity_instance = InsufficientNetworkResourcePoolCapacity.from_json(json)
# print the JSON string representation of the object
print InsufficientNetworkResourcePoolCapacity.to_json()

# convert the object into a dict
insufficient_network_resource_pool_capacity_dict = insufficient_network_resource_pool_capacity_instance.to_dict()
# create an instance of InsufficientNetworkResourcePoolCapacity from a dict
insufficient_network_resource_pool_capacity_form_dict = insufficient_network_resource_pool_capacity.from_dict(insufficient_network_resource_pool_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


