# VirtualMachineFloppyInfo

FloppyInfo class contains information about a physical floppy drive on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_floppy_info import VirtualMachineFloppyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFloppyInfo from a JSON string
virtual_machine_floppy_info_instance = VirtualMachineFloppyInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFloppyInfo.to_json()

# convert the object into a dict
virtual_machine_floppy_info_dict = virtual_machine_floppy_info_instance.to_dict()
# create an instance of VirtualMachineFloppyInfo from a dict
virtual_machine_floppy_info_form_dict = virtual_machine_floppy_info.from_dict(virtual_machine_floppy_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


