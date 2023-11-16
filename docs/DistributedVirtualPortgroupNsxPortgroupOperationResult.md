# DistributedVirtualPortgroupNsxPortgroupOperationResult

The *DistributedVirtualPortgroupNsxPortgroupOperationResult* data object defines the result of NSX port group operations, including create, reconfigure and delete.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroups** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The management object of NSX port group.  For add operation, it indicates the port groups created successfully. For reconfigure operation, it indicates the port groups updated successfully. For delete operation, it indicates the port groups failed deleted.  ***Since:*** vSphere API 7.0  Refers instances of *DistributedVirtualPortgroup*.  | [optional] 
**problems** | [**List[DistributedVirtualPortgroupProblem]**](DistributedVirtualPortgroupProblem.md) | The failed port group operation details.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_portgroup_nsx_portgroup_operation_result import DistributedVirtualPortgroupNsxPortgroupOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualPortgroupNsxPortgroupOperationResult from a JSON string
distributed_virtual_portgroup_nsx_portgroup_operation_result_instance = DistributedVirtualPortgroupNsxPortgroupOperationResult.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualPortgroupNsxPortgroupOperationResult.to_json()

# convert the object into a dict
distributed_virtual_portgroup_nsx_portgroup_operation_result_dict = distributed_virtual_portgroup_nsx_portgroup_operation_result_instance.to_dict()
# create an instance of DistributedVirtualPortgroupNsxPortgroupOperationResult from a dict
distributed_virtual_portgroup_nsx_portgroup_operation_result_form_dict = distributed_virtual_portgroup_nsx_portgroup_operation_result.from_dict(distributed_virtual_portgroup_nsx_portgroup_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


