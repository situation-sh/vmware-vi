# DistributedVirtualSwitchManagerHostArrayFilter

Check host compatibility against all hosts specified in the array.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of hosts to consider.  ***Since:*** vSphere API 4.1  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_host_array_filter import DistributedVirtualSwitchManagerHostArrayFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerHostArrayFilter from a JSON string
distributed_virtual_switch_manager_host_array_filter_instance = DistributedVirtualSwitchManagerHostArrayFilter.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerHostArrayFilter.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_host_array_filter_dict = distributed_virtual_switch_manager_host_array_filter_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerHostArrayFilter from a dict
distributed_virtual_switch_manager_host_array_filter_form_dict = distributed_virtual_switch_manager_host_array_filter.from_dict(distributed_virtual_switch_manager_host_array_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


