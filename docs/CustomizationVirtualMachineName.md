# CustomizationVirtualMachineName

Specifies that VirtualCenter should generate a virtual machine name from a base prefix comprising the virtual machine entity name.  A number is appended, if necessary, to make it unique.  Virtual machine names are unique across the set of hosts and virtual machines known to the VirtualCenter instance. VMware Tools reports the names of existing virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_virtual_machine_name import CustomizationVirtualMachineName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationVirtualMachineName from a JSON string
customization_virtual_machine_name_instance = CustomizationVirtualMachineName.from_json(json)
# print the JSON string representation of the object
print CustomizationVirtualMachineName.to_json()

# convert the object into a dict
customization_virtual_machine_name_dict = customization_virtual_machine_name_instance.to_dict()
# create an instance of CustomizationVirtualMachineName from a dict
customization_virtual_machine_name_form_dict = customization_virtual_machine_name.from_dict(customization_virtual_machine_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


