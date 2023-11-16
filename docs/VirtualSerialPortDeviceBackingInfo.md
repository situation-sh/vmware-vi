# VirtualSerialPortDeviceBackingInfo

The <code>*VirtualSerialPortDeviceBackingInfo*</code> data object defines information for using a host serial port device as backing for a <code>*VirtualSerialPort*</code>.  On a host, the first virtual machine to configure physical device backing for a virtual serial port will obtain the mapping. As long as that machine maintains the backing, any additional attempts to configure backing using that device will fail (a recoverable error, see the connection info <code>*VirtualDeviceConnectInfo.status*</code>). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_serial_port_device_backing_info import VirtualSerialPortDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSerialPortDeviceBackingInfo from a JSON string
virtual_serial_port_device_backing_info_instance = VirtualSerialPortDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualSerialPortDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_serial_port_device_backing_info_dict = virtual_serial_port_device_backing_info_instance.to_dict()
# create an instance of VirtualSerialPortDeviceBackingInfo from a dict
virtual_serial_port_device_backing_info_form_dict = virtual_serial_port_device_backing_info.from_dict(virtual_serial_port_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


