# DistributedVirtualSwitchManagerHostContainer

Check host compatibility for all hosts in the container.  If the recursive flag is true, then check hosts at all levels within this container, otherwise check only at the container level. In case of container being a *Datacenter*, the recursive flag is applied to its HostFolder.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**recursive** | **bool** | If true, include hosts of all levels in the hierarchy with container as root of the tree.  In case of container being a *Datacenter*, the recursive flag is applied to its HostFolder.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_host_container import DistributedVirtualSwitchManagerHostContainer

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerHostContainer from a JSON string
distributed_virtual_switch_manager_host_container_instance = DistributedVirtualSwitchManagerHostContainer.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerHostContainer.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_host_container_dict = distributed_virtual_switch_manager_host_container_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerHostContainer from a dict
distributed_virtual_switch_manager_host_container_form_dict = distributed_virtual_switch_manager_host_container.from_dict(distributed_virtual_switch_manager_host_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


