# MarkAsVirtualMachineRequestType

The parameters of *VirtualMachine.MarkAsVirtualMachine*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.mark_as_virtual_machine_request_type import MarkAsVirtualMachineRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsVirtualMachineRequestType from a JSON string
mark_as_virtual_machine_request_type_instance = MarkAsVirtualMachineRequestType.from_json(json)
# print the JSON string representation of the object
print MarkAsVirtualMachineRequestType.to_json()

# convert the object into a dict
mark_as_virtual_machine_request_type_dict = mark_as_virtual_machine_request_type_instance.to_dict()
# create an instance of MarkAsVirtualMachineRequestType from a dict
mark_as_virtual_machine_request_type_form_dict = mark_as_virtual_machine_request_type.from_dict(mark_as_virtual_machine_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


