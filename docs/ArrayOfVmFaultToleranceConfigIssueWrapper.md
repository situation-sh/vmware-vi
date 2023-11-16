# ArrayOfVmFaultToleranceConfigIssueWrapper

A boxed array of *VmFaultToleranceConfigIssueWrapper*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceConfigIssueWrapper]**](VmFaultToleranceConfigIssueWrapper.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_config_issue_wrapper import ArrayOfVmFaultToleranceConfigIssueWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceConfigIssueWrapper from a JSON string
array_of_vm_fault_tolerance_config_issue_wrapper_instance = ArrayOfVmFaultToleranceConfigIssueWrapper.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceConfigIssueWrapper.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_config_issue_wrapper_dict = array_of_vm_fault_tolerance_config_issue_wrapper_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceConfigIssueWrapper from a dict
array_of_vm_fault_tolerance_config_issue_wrapper_form_dict = array_of_vm_fault_tolerance_config_issue_wrapper.from_dict(array_of_vm_fault_tolerance_config_issue_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


