# InvalidDrsBehaviorForFtVm

This fault is thrown when an attempt is made to set the DRS behavior of an FT VM to an unsupported value.  Currently, the only supported behavior is **DRS Disabled**.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The name of the virtual machine  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.invalid_drs_behavior_for_ft_vm import InvalidDrsBehaviorForFtVm

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDrsBehaviorForFtVm from a JSON string
invalid_drs_behavior_for_ft_vm_instance = InvalidDrsBehaviorForFtVm.from_json(json)
# print the JSON string representation of the object
print InvalidDrsBehaviorForFtVm.to_json()

# convert the object into a dict
invalid_drs_behavior_for_ft_vm_dict = invalid_drs_behavior_for_ft_vm_instance.to_dict()
# create an instance of InvalidDrsBehaviorForFtVm from a dict
invalid_drs_behavior_for_ft_vm_form_dict = invalid_drs_behavior_for_ft_vm.from_dict(invalid_drs_behavior_for_ft_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


