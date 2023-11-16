# InvalidOperationOnSecondaryVm

This fault is thrown when an attempt is made to invoke an operation on a secondary virtual machine that is only supported on the primary virtual machine of the fault tolerant group.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_uuid** | **str** | Instance UUID of the secondary virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.invalid_operation_on_secondary_vm import InvalidOperationOnSecondaryVm

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidOperationOnSecondaryVm from a JSON string
invalid_operation_on_secondary_vm_instance = InvalidOperationOnSecondaryVm.from_json(json)
# print the JSON string representation of the object
print InvalidOperationOnSecondaryVm.to_json()

# convert the object into a dict
invalid_operation_on_secondary_vm_dict = invalid_operation_on_secondary_vm_instance.to_dict()
# create an instance of InvalidOperationOnSecondaryVm from a dict
invalid_operation_on_secondary_vm_form_dict = invalid_operation_on_secondary_vm.from_dict(invalid_operation_on_secondary_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


