# ArrayOfVirtualHardwareOption

A boxed array of *VirtualHardwareOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualHardwareOption]**](VirtualHardwareOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_hardware_option import ArrayOfVirtualHardwareOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualHardwareOption from a JSON string
array_of_virtual_hardware_option_instance = ArrayOfVirtualHardwareOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualHardwareOption.to_json()

# convert the object into a dict
array_of_virtual_hardware_option_dict = array_of_virtual_hardware_option_instance.to_dict()
# create an instance of ArrayOfVirtualHardwareOption from a dict
array_of_virtual_hardware_option_form_dict = array_of_virtual_hardware_option.from_dict(array_of_virtual_hardware_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


