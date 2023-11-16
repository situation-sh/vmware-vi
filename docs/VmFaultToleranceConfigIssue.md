# VmFaultToleranceConfigIssue

Configuration issues that can occur during operations related to fault tolerance protection for virtual machines.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  ***Since:*** vSphere API 4.0  | [optional] 
**entity_name** | **str** | The entity name.  Depending on the issue, it could be virtual machine or host.  ***Since:*** vSphere API 4.0  | [optional] 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_config_issue import VmFaultToleranceConfigIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceConfigIssue from a JSON string
vm_fault_tolerance_config_issue_instance = VmFaultToleranceConfigIssue.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceConfigIssue.to_json()

# convert the object into a dict
vm_fault_tolerance_config_issue_dict = vm_fault_tolerance_config_issue_instance.to_dict()
# create an instance of VmFaultToleranceConfigIssue from a dict
vm_fault_tolerance_config_issue_form_dict = vm_fault_tolerance_config_issue.from_dict(vm_fault_tolerance_config_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


