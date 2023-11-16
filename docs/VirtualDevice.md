# VirtualDevice

VirtualDevice is the base data object type for devices in a virtual machine.  This type contains enough information about a virtual device to allow clients to display devices they do not recognize. For example, a client with an older version than the server to which it connects may see a device without knowing what it is. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A unique key that distinguishes this device from other devices in the same virtual machine.  Keys are immutable but may be recycled; that is, a key does not change as long as the device is associated with a particular virtual machine. However, once a device is removed, its key may be used when another device is added.  This property is not read-only, but the client cannot control its value. Persistent device keys are always assigned and managed by the server, which guarantees that all devices will have non-negative key values.  When adding new devices, it may be necessary for a client to assign keys temporarily in order to associate controllers with devices in configuring a virtual machine. However, the server does not allow a client to reassign a device key, and the server may assign a different value from the one passed during configuration. Clients should ensure that existing device keys are not reused as temporary key values for the new device to be added (for example, by using unique negative integers as temporary keys).  When editing or deleting a device, clients must use the server-provided key to refer to an existing device.  | 
**device_info** | [**Description**](Description.md) |  | [optional] 
**backing** | [**VirtualDeviceBackingInfo**](VirtualDeviceBackingInfo.md) |  | [optional] 
**connectable** | [**VirtualDeviceConnectInfo**](VirtualDeviceConnectInfo.md) |  | [optional] 
**slot_info** | [**VirtualDeviceBusSlotInfo**](VirtualDeviceBusSlotInfo.md) |  | [optional] 
**controller_key** | **int** | Object key for the controller object for this device.  This property contains the key property value of the controller device object.  | [optional] 
**unit_number** | **int** | The unit number of this device on its controller.  This property is null if the controller property is null (for example, when the device is not attached to a specific controller object).  Normally, two devices on the same controller may not be assigned the same unit number. If multiple devices could exist on a controller, then unit number has to be specified to configure respective devices.  | [optional] 
**numa_node** | **int** | The virtual NUMA node.  A negative number means there is no affinity for the device. A positive number is a vNUMA node. An unset value of numaNode is status-quo during Reconfigure time. If numaNode is unset during ConfigInfo, then it means there is no affinity for the device.  | [optional] 
**device_group_info** | [**VirtualDeviceDeviceGroupInfo**](VirtualDeviceDeviceGroupInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device import VirtualDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDevice from a JSON string
virtual_device_instance = VirtualDevice.from_json(json)
# print the JSON string representation of the object
print VirtualDevice.to_json()

# convert the object into a dict
virtual_device_dict = virtual_device_instance.to_dict()
# create an instance of VirtualDevice from a dict
virtual_device_form_dict = virtual_device.from_dict(virtual_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


