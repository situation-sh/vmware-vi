# VmFaultToleranceOpIssuesList

Container for a list of configuration issues that can occur during operations related to fault tolerance protection for virtual machines.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[MethodFault]**](MethodFault.md) | A list of faults representing errors  ***Since:*** vSphere API 4.0  | [optional] 
**warnings** | [**List[MethodFault]**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_op_issues_list import VmFaultToleranceOpIssuesList

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceOpIssuesList from a JSON string
vm_fault_tolerance_op_issues_list_instance = VmFaultToleranceOpIssuesList.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceOpIssuesList.to_json()

# convert the object into a dict
vm_fault_tolerance_op_issues_list_dict = vm_fault_tolerance_op_issues_list_instance.to_dict()
# create an instance of VmFaultToleranceOpIssuesList from a dict
vm_fault_tolerance_op_issues_list_form_dict = vm_fault_tolerance_op_issues_list.from_dict(vm_fault_tolerance_op_issues_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


