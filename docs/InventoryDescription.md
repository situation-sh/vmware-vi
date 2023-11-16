# InventoryDescription

Data object to capture all information needed to describe a sample inventory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_hosts** | **int** | The number of hosts.  ***Since:*** vSphere API 4.0  | 
**num_virtual_machines** | **int** | The number of virtual machines.  ***Since:*** vSphere API 4.0  | 
**num_resource_pools** | **int** | The number of resource pools.  Default value is equal to numHosts  ***Since:*** vSphere API 4.0  | [optional] 
**num_clusters** | **int** | The number of clusters.  Default value is equal to numHosts/5.  ***Since:*** vSphere API 4.0  | [optional] 
**num_cpu_dev** | **int** | The number cpu devices per host.  Default value is 4.  ***Since:*** vSphere API 4.0  | [optional] 
**num_net_dev** | **int** | The number network devices per host.  Default value is 2.  ***Since:*** vSphere API 4.0  | [optional] 
**num_disk_dev** | **int** | The number disk devices per host.  Default value is 10.  ***Since:*** vSphere API 4.0  | [optional] 
**numv_cpu_dev** | **int** | The number cpu devices per vm.  Default value is 2.  ***Since:*** vSphere API 4.0  | [optional] 
**numv_net_dev** | **int** | The number network devices per vm.  Default value is 1.  ***Since:*** vSphere API 4.0  | [optional] 
**numv_disk_dev** | **int** | The number disk devices per vm.  Default value is 4.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.inventory_description import InventoryDescription

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDescription from a JSON string
inventory_description_instance = InventoryDescription.from_json(json)
# print the JSON string representation of the object
print InventoryDescription.to_json()

# convert the object into a dict
inventory_description_dict = inventory_description_instance.to_dict()
# create an instance of InventoryDescription from a dict
inventory_description_form_dict = inventory_description.from_dict(inventory_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


