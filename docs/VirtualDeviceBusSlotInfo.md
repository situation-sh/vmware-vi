# VirtualDeviceBusSlotInfo

<code>*VirtualDeviceBusSlotInfo*</code> is a base data object type for information about device connection to its bus.  This base type does not define any properties. It is used as a namespace for general-purpose subtypes. Specific devices types are represented by subtypes which define properties for device-specific backing information.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_device_bus_slot_info import VirtualDeviceBusSlotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceBusSlotInfo from a JSON string
virtual_device_bus_slot_info_instance = VirtualDeviceBusSlotInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceBusSlotInfo.to_json()

# convert the object into a dict
virtual_device_bus_slot_info_dict = virtual_device_bus_slot_info_instance.to_dict()
# create an instance of VirtualDeviceBusSlotInfo from a dict
virtual_device_bus_slot_info_form_dict = virtual_device_bus_slot_info.from_dict(virtual_device_bus_slot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


