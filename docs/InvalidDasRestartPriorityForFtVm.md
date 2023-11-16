# InvalidDasRestartPriorityForFtVm

This fault is thrown when an attempt is made to set the DAS restart priority of a FT VM to disabled.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The name of the virtual machine  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.invalid_das_restart_priority_for_ft_vm import InvalidDasRestartPriorityForFtVm

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDasRestartPriorityForFtVm from a JSON string
invalid_das_restart_priority_for_ft_vm_instance = InvalidDasRestartPriorityForFtVm.from_json(json)
# print the JSON string representation of the object
print InvalidDasRestartPriorityForFtVm.to_json()

# convert the object into a dict
invalid_das_restart_priority_for_ft_vm_dict = invalid_das_restart_priority_for_ft_vm_instance.to_dict()
# create an instance of InvalidDasRestartPriorityForFtVm from a dict
invalid_das_restart_priority_for_ft_vm_form_dict = invalid_das_restart_priority_for_ft_vm.from_dict(invalid_das_restart_priority_for_ft_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


