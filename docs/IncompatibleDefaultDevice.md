# IncompatibleDefaultDevice

A default device (see *VirtualMachineConfigOption.defaultDevice* for a definition) which the virtual machine is using is incompatible with the corresponding default device which will be created on the target host.  This is an issue with powered-on or suspended migration under some circumstances. The problem is that in cases where the virtual machine must be recreated, it will have the default device created with default settings that are appropriate for the target host. If those are not compatible with the settings for that device that the virtual machine is currently using, then resuming the virtual machine on the target host might fail.  This might happen if the device in question were reconfigured or the default is different between the source and the destination host. An example of a default device and associated setting which might cause this is *VirtualMachineVideoCard.videoRamSizeInKB*. This is an error.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the device.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.incompatible_default_device import IncompatibleDefaultDevice

# TODO update the JSON string below
json = "{}"
# create an instance of IncompatibleDefaultDevice from a JSON string
incompatible_default_device_instance = IncompatibleDefaultDevice.from_json(json)
# print the JSON string representation of the object
print IncompatibleDefaultDevice.to_json()

# convert the object into a dict
incompatible_default_device_dict = incompatible_default_device_instance.to_dict()
# create an instance of IncompatibleDefaultDevice from a dict
incompatible_default_device_form_dict = incompatible_default_device.from_dict(incompatible_default_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


