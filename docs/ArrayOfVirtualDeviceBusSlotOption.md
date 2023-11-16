# ArrayOfVirtualDeviceBusSlotOption

A boxed array of *VirtualDeviceBusSlotOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceBusSlotOption]**](VirtualDeviceBusSlotOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_bus_slot_option import ArrayOfVirtualDeviceBusSlotOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceBusSlotOption from a JSON string
array_of_virtual_device_bus_slot_option_instance = ArrayOfVirtualDeviceBusSlotOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceBusSlotOption.to_json()

# convert the object into a dict
array_of_virtual_device_bus_slot_option_dict = array_of_virtual_device_bus_slot_option_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceBusSlotOption from a dict
array_of_virtual_device_bus_slot_option_form_dict = array_of_virtual_device_bus_slot_option.from_dict(array_of_virtual_device_bus_slot_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


