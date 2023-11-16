# VmConfigFault

Base for configuration / environment issues that can be thrown when powering on or changing the configuration of a virtual machine.  Subclasses of this fault is also used as recent why a migration can fail. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_config_fault import VmConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFault from a JSON string
vm_config_fault_instance = VmConfigFault.from_json(json)
# print the JSON string representation of the object
print VmConfigFault.to_json()

# convert the object into a dict
vm_config_fault_dict = vm_config_fault_instance.to_dict()
# create an instance of VmConfigFault from a dict
vm_config_fault_form_dict = vm_config_fault.from_dict(vm_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


