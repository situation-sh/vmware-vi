# ArrayOfVmConfigFault

A boxed array of *VmConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmConfigFault]**](VmConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_config_fault import ArrayOfVmConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmConfigFault from a JSON string
array_of_vm_config_fault_instance = ArrayOfVmConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmConfigFault.to_json()

# convert the object into a dict
array_of_vm_config_fault_dict = array_of_vm_config_fault_instance.to_dict()
# create an instance of ArrayOfVmConfigFault from a dict
array_of_vm_config_fault_form_dict = array_of_vm_config_fault.from_dict(array_of_vm_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


