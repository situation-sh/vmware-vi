# VirtualDeviceConnectInfo

The <code>*VirtualDeviceConnectInfo*</code> data object type contains information about connectable virtual devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrate_connect** | **str** | Specifies whether the virtual machine should override the virtual device connection state upon the completion of a migration.  At this time, this property is only applicable to instant clone operations, and will be ignored for other migration types. The property is also only valid with VirtualEthernetCards, and any attempt to set this property on an unsupported device will result in an error. This property will persist only until the virtual machine undergoes a supported migration, at which point it will be consumed and unset on the destination virtual machine, preventing the property from affecting future migrations. The migration&#39;s success is not dependent on whether the device reaches the desired connection state. The set of possible values are described in *VirtualDeviceConnectInfoMigrateConnectOp_enum*.  ***Since:*** vSphere API 6.7  | [optional] 
**start_connected** | **bool** | Specifies whether or not to connect the device when the virtual machine starts.  | 
**allow_guest_control** | **bool** | Enables guest control over whether the connectable device is connected.  | 
**connected** | **bool** | Indicates whether the device is currently connected.  Valid only while the virtual machine is running.  | 
**status** | **str** | Indicates the current status of the connectable device.  Valid only while the virtual machine is running. The set of possible values is described in *VirtualDeviceConnectInfoStatus_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_connect_info import VirtualDeviceConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConnectInfo from a JSON string
virtual_device_connect_info_instance = VirtualDeviceConnectInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConnectInfo.to_json()

# convert the object into a dict
virtual_device_connect_info_dict = virtual_device_connect_info_instance.to_dict()
# create an instance of VirtualDeviceConnectInfo from a dict
virtual_device_connect_info_form_dict = virtual_device_connect_info.from_dict(virtual_device_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


