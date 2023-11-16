# VmToolsUpgradeFault

A base fault to indicate that something went wrong when upgrading tools. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_tools_upgrade_fault import VmToolsUpgradeFault

# TODO update the JSON string below
json = "{}"
# create an instance of VmToolsUpgradeFault from a JSON string
vm_tools_upgrade_fault_instance = VmToolsUpgradeFault.from_json(json)
# print the JSON string representation of the object
print VmToolsUpgradeFault.to_json()

# convert the object into a dict
vm_tools_upgrade_fault_dict = vm_tools_upgrade_fault_instance.to_dict()
# create an instance of VmToolsUpgradeFault from a dict
vm_tools_upgrade_fault_form_dict = vm_tools_upgrade_fault.from_dict(vm_tools_upgrade_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


