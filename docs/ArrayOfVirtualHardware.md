# ArrayOfVirtualHardware

A boxed array of *VirtualHardware*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualHardware]**](VirtualHardware.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_hardware import ArrayOfVirtualHardware

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualHardware from a JSON string
array_of_virtual_hardware_instance = ArrayOfVirtualHardware.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualHardware.to_json()

# convert the object into a dict
array_of_virtual_hardware_dict = array_of_virtual_hardware_instance.to_dict()
# create an instance of ArrayOfVirtualHardware from a dict
array_of_virtual_hardware_form_dict = array_of_virtual_hardware.from_dict(array_of_virtual_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


