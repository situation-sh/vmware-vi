# ArrayOfVmFaultToleranceConfigIssue

A boxed array of *VmFaultToleranceConfigIssue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceConfigIssue]**](VmFaultToleranceConfigIssue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_config_issue import ArrayOfVmFaultToleranceConfigIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceConfigIssue from a JSON string
array_of_vm_fault_tolerance_config_issue_instance = ArrayOfVmFaultToleranceConfigIssue.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceConfigIssue.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_config_issue_dict = array_of_vm_fault_tolerance_config_issue_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceConfigIssue from a dict
array_of_vm_fault_tolerance_config_issue_form_dict = array_of_vm_fault_tolerance_config_issue.from_dict(array_of_vm_fault_tolerance_config_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


