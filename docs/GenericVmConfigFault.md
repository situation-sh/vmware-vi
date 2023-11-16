# GenericVmConfigFault

Thrown when a running virtual machine reports an error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Message from the virtual machine  | 

## Example

```python
from vmware_vi.models.generic_vm_config_fault import GenericVmConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of GenericVmConfigFault from a JSON string
generic_vm_config_fault_instance = GenericVmConfigFault.from_json(json)
# print the JSON string representation of the object
print GenericVmConfigFault.to_json()

# convert the object into a dict
generic_vm_config_fault_dict = generic_vm_config_fault_instance.to_dict()
# create an instance of GenericVmConfigFault from a dict
generic_vm_config_fault_form_dict = generic_vm_config_fault.from_dict(generic_vm_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


