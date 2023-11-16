# VirtualDeviceBusSlotOption

The *VirtualDeviceBusSlotOption* data class defines options for device-specific bus slot objects.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The name of the class the client should use to instantiate bus slot object for the virtual device.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_device_bus_slot_option import VirtualDeviceBusSlotOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceBusSlotOption from a JSON string
virtual_device_bus_slot_option_instance = VirtualDeviceBusSlotOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceBusSlotOption.to_json()

# convert the object into a dict
virtual_device_bus_slot_option_dict = virtual_device_bus_slot_option_instance.to_dict()
# create an instance of VirtualDeviceBusSlotOption from a dict
virtual_device_bus_slot_option_form_dict = virtual_device_bus_slot_option.from_dict(virtual_device_bus_slot_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


