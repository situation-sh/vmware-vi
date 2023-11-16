# DistributedVirtualSwitchManagerHostContainerFilter

Check host compatibility against all hosts in this *DistributedVirtualSwitchManagerHostContainer*  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_container** | [**DistributedVirtualSwitchManagerHostContainer**](DistributedVirtualSwitchManagerHostContainer.md) |  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_host_container_filter import DistributedVirtualSwitchManagerHostContainerFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerHostContainerFilter from a JSON string
distributed_virtual_switch_manager_host_container_filter_instance = DistributedVirtualSwitchManagerHostContainerFilter.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerHostContainerFilter.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_host_container_filter_dict = distributed_virtual_switch_manager_host_container_filter_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerHostContainerFilter from a dict
distributed_virtual_switch_manager_host_container_filter_form_dict = distributed_virtual_switch_manager_host_container_filter.from_dict(distributed_virtual_switch_manager_host_container_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


