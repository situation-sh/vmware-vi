# VirtualVMIROMOption

This data object type contains the options for the *VirtualVMIROM* data object type.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_vmirom_option import VirtualVMIROMOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVMIROMOption from a JSON string
virtual_vmirom_option_instance = VirtualVMIROMOption.from_json(json)
# print the JSON string representation of the object
print VirtualVMIROMOption.to_json()

# convert the object into a dict
virtual_vmirom_option_dict = virtual_vmirom_option_instance.to_dict()
# create an instance of VirtualVMIROMOption from a dict
virtual_vmirom_option_form_dict = virtual_vmirom_option.from_dict(virtual_vmirom_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


