# VmFaultToleranceIssue

Base object type for issues that can occur during operations related to fault tolerance protection for virtual machines.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_fault_tolerance_issue import VmFaultToleranceIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceIssue from a JSON string
vm_fault_tolerance_issue_instance = VmFaultToleranceIssue.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceIssue.to_json()

# convert the object into a dict
vm_fault_tolerance_issue_dict = vm_fault_tolerance_issue_instance.to_dict()
# create an instance of VmFaultToleranceIssue from a dict
vm_fault_tolerance_issue_form_dict = vm_fault_tolerance_issue.from_dict(vm_fault_tolerance_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


