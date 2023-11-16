# VirtualDeviceOption

The VirtualDeviceOption data object type contains information about a virtual device type, the options for configuring the virtual device, and the relationship between this virtual device and other devices.  The vSphere API groups device configurations that are mutually exclusive into different configuration objects; each of these configuration objects may define subtypes for virtual device backing options that are independent of the virtual device. Backing-dependent options should appear in a subtype of *VirtualDeviceBackingOption*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The name of the run-time class the client should instantiate to create a run-time instance of this device.  | 
**connect_option** | [**VirtualDeviceConnectOption**](VirtualDeviceConnectOption.md) |  | [optional] 
**bus_slot_option** | [**VirtualDeviceBusSlotOption**](VirtualDeviceBusSlotOption.md) |  | [optional] 
**controller_type** | **str** | Data object type that denotes the controller option object that is valid for controlling this device.  | [optional] 
**auto_assign_controller** | [**BoolOption**](BoolOption.md) |  | [optional] 
**backing_option** | [**List[VirtualDeviceBackingOption]**](VirtualDeviceBackingOption.md) | A list of backing options that can be used to map the virtual device to the host.  The list is optional, since some devices exist only within the virtual machine; for example, a VirtualController.  | [optional] 
**default_backing_option_index** | **int** | Index into the backingOption list, indicating the default backing.  | [optional] 
**licensing_limit** | **List[str]** | List of property names enforced by a licensing restriction of the underlying product.  For example, a limit that is not derived based on the product or hardware features; the property name \&quot;numCPU\&quot;.  | [optional] 
**deprecated** | **bool** | Indicates whether this device is deprecated.  Hence, if set the device cannot be used when creating a new virtual machine or be added to an existing virtual machine. However, the device is still supported by the platform.  | 
**plug_and_play** | **bool** | Indicates if this type of device can be hot-added to the virtual machine via a reconfigure operation when the virtual machine is powered on.  | 
**hot_remove_supported** | **bool** | Indicates if this type of device can be hot-removed from the virtual machine via a reconfigure operation when the virtual machine is powered on.  ***Since:*** vSphere API 4.0  | 
**numa_supported** | **bool** |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_option import VirtualDeviceOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceOption from a JSON string
virtual_device_option_instance = VirtualDeviceOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceOption.to_json()

# convert the object into a dict
virtual_device_option_dict = virtual_device_option_instance.to_dict()
# create an instance of VirtualDeviceOption from a dict
virtual_device_option_form_dict = virtual_device_option.from_dict(virtual_device_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


