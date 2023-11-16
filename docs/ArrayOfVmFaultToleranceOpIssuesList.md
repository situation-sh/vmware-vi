# ArrayOfVmFaultToleranceOpIssuesList

A boxed array of *VmFaultToleranceOpIssuesList*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceOpIssuesList]**](VmFaultToleranceOpIssuesList.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_op_issues_list import ArrayOfVmFaultToleranceOpIssuesList

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceOpIssuesList from a JSON string
array_of_vm_fault_tolerance_op_issues_list_instance = ArrayOfVmFaultToleranceOpIssuesList.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceOpIssuesList.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_op_issues_list_dict = array_of_vm_fault_tolerance_op_issues_list_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceOpIssuesList from a dict
array_of_vm_fault_tolerance_op_issues_list_form_dict = array_of_vm_fault_tolerance_op_issues_list.from_dict(array_of_vm_fault_tolerance_op_issues_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


