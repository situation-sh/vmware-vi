# DeviceUnsupportedForVmPlatform

A DeviceUnsupportedForVmPlatform exception is thrown if the specified device is not supported on the platform on which the virtual machine is being created/configured.  For example, this exception might be thrown if a client incorrectly attempts to add a device supported only on ESX Server to a virtual machine on a hosted product.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.device_unsupported_for_vm_platform import DeviceUnsupportedForVmPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUnsupportedForVmPlatform from a JSON string
device_unsupported_for_vm_platform_instance = DeviceUnsupportedForVmPlatform.from_json(json)
# print the JSON string representation of the object
print DeviceUnsupportedForVmPlatform.to_json()

# convert the object into a dict
device_unsupported_for_vm_platform_dict = device_unsupported_for_vm_platform_instance.to_dict()
# create an instance of DeviceUnsupportedForVmPlatform from a dict
device_unsupported_for_vm_platform_form_dict = device_unsupported_for_vm_platform.from_dict(device_unsupported_for_vm_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


