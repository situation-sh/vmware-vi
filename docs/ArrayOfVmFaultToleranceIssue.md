# ArrayOfVmFaultToleranceIssue

A boxed array of *VmFaultToleranceIssue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceIssue]**](VmFaultToleranceIssue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_issue import ArrayOfVmFaultToleranceIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceIssue from a JSON string
array_of_vm_fault_tolerance_issue_instance = ArrayOfVmFaultToleranceIssue.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceIssue.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_issue_dict = array_of_vm_fault_tolerance_issue_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceIssue from a dict
array_of_vm_fault_tolerance_issue_form_dict = array_of_vm_fault_tolerance_issue.from_dict(array_of_vm_fault_tolerance_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


