# VmFaultToleranceConfigIssueWrapper

Configuration issues that can occur during operations related to fault tolerance protection for virtual machines.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The entity name.  Depending on the issue, it could be virtual machine or host.  ***Since:*** vSphere API 4.1  | [optional] 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_config_issue_wrapper import VmFaultToleranceConfigIssueWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceConfigIssueWrapper from a JSON string
vm_fault_tolerance_config_issue_wrapper_instance = VmFaultToleranceConfigIssueWrapper.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceConfigIssueWrapper.to_json()

# convert the object into a dict
vm_fault_tolerance_config_issue_wrapper_dict = vm_fault_tolerance_config_issue_wrapper_instance.to_dict()
# create an instance of VmFaultToleranceConfigIssueWrapper from a dict
vm_fault_tolerance_config_issue_wrapper_form_dict = vm_fault_tolerance_config_issue_wrapper.from_dict(vm_fault_tolerance_config_issue_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


