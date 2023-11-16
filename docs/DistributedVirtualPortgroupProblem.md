# DistributedVirtualPortgroupProblem

The *DistributedVirtualPortgroupProblem* data object defines the error while excuting NSX port group operations.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_switch_uuid** | **str** | The problematic logical switch UUID  ***Since:*** vSphere API 7.0  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.distributed_virtual_portgroup_problem import DistributedVirtualPortgroupProblem

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualPortgroupProblem from a JSON string
distributed_virtual_portgroup_problem_instance = DistributedVirtualPortgroupProblem.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualPortgroupProblem.to_json()

# convert the object into a dict
distributed_virtual_portgroup_problem_dict = distributed_virtual_portgroup_problem_instance.to_dict()
# create an instance of DistributedVirtualPortgroupProblem from a dict
distributed_virtual_portgroup_problem_form_dict = distributed_virtual_portgroup_problem.from_dict(distributed_virtual_portgroup_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


