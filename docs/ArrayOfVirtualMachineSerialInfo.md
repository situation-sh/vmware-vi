# ArrayOfVirtualMachineSerialInfo

A boxed array of *VirtualMachineSerialInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineSerialInfo]**](VirtualMachineSerialInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_serial_info import ArrayOfVirtualMachineSerialInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineSerialInfo from a JSON string
array_of_virtual_machine_serial_info_instance = ArrayOfVirtualMachineSerialInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineSerialInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_serial_info_dict = array_of_virtual_machine_serial_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineSerialInfo from a dict
array_of_virtual_machine_serial_info_form_dict = array_of_virtual_machine_serial_info.from_dict(array_of_virtual_machine_serial_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


