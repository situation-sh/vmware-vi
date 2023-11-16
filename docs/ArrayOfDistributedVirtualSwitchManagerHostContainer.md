# ArrayOfDistributedVirtualSwitchManagerHostContainer

A boxed array of *DistributedVirtualSwitchManagerHostContainer*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchManagerHostContainer]**](DistributedVirtualSwitchManagerHostContainer.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_manager_host_container import ArrayOfDistributedVirtualSwitchManagerHostContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchManagerHostContainer from a JSON string
array_of_distributed_virtual_switch_manager_host_container_instance = ArrayOfDistributedVirtualSwitchManagerHostContainer.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchManagerHostContainer.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_manager_host_container_dict = array_of_distributed_virtual_switch_manager_host_container_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchManagerHostContainer from a dict
array_of_distributed_virtual_switch_manager_host_container_form_dict = array_of_distributed_virtual_switch_manager_host_container.from_dict(array_of_distributed_virtual_switch_manager_host_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


