# DeviceUnsupportedForVmVersion

A DeviceUnsupportedForVmVersion exception is thrown if a specific device is not supported for a given version of the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_version** | **str** | The current version of the virtual machine.  ***Since:*** vSphere API 4.0  | 
**expected_version** | **str** | The minimum expected virtual mahcine version needed to support this device.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.device_unsupported_for_vm_version import DeviceUnsupportedForVmVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUnsupportedForVmVersion from a JSON string
device_unsupported_for_vm_version_instance = DeviceUnsupportedForVmVersion.from_json(json)
# print the JSON string representation of the object
print DeviceUnsupportedForVmVersion.to_json()

# convert the object into a dict
device_unsupported_for_vm_version_dict = device_unsupported_for_vm_version_instance.to_dict()
# create an instance of DeviceUnsupportedForVmVersion from a dict
device_unsupported_for_vm_version_form_dict = device_unsupported_for_vm_version.from_dict(device_unsupported_for_vm_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


