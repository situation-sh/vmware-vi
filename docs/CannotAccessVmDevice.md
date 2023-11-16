# CannotAccessVmDevice

One of the virtual machine's devices uses a backing that is not accessible on the host.  Following is a discussion of this fault's use in migration validation. This is an error if the device is currently connected and a warning otherwise. Devices that can be disconnected can only be connected if the virtual machine is powered on.  The usage of this fault is slightly different if the backing of a device is inherently host-local, and therefore not shared or globally named among hosts. (Examples of such backings: physical CD-ROM drive, physical serial port.) If a device with such a backing is currently connected, that will be a migration error. If the device is disconnected, there will be a warning if no backing with the same name exists on the destination host. If the device is disconnected and a backing with the same name exists on the destination host, this is neither a warning nor an error case, even though the destination host's backing is not the same instance as the source host's. It is assumed that use of the host-local backing is what is desired for the device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the device.  | 
**backing** | **str** | The backing of the device.  | 
**connected** | **bool** | The connected/disconnected state of the device.  | 

## Example

```python
from vmware_vi.models.cannot_access_vm_device import CannotAccessVmDevice

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessVmDevice from a JSON string
cannot_access_vm_device_instance = CannotAccessVmDevice.from_json(json)
# print the JSON string representation of the object
print CannotAccessVmDevice.to_json()

# convert the object into a dict
cannot_access_vm_device_dict = cannot_access_vm_device_instance.to_dict()
# create an instance of CannotAccessVmDevice from a dict
cannot_access_vm_device_form_dict = cannot_access_vm_device.from_dict(cannot_access_vm_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


