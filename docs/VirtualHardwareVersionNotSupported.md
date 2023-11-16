# VirtualHardwareVersionNotSupported

The virtual machine's virtual hardware version is not supported on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.virtual_hardware_version_not_supported import VirtualHardwareVersionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHardwareVersionNotSupported from a JSON string
virtual_hardware_version_not_supported_instance = VirtualHardwareVersionNotSupported.from_json(json)
# print the JSON string representation of the object
print VirtualHardwareVersionNotSupported.to_json()

# convert the object into a dict
virtual_hardware_version_not_supported_dict = virtual_hardware_version_not_supported_instance.to_dict()
# create an instance of VirtualHardwareVersionNotSupported from a dict
virtual_hardware_version_not_supported_form_dict = virtual_hardware_version_not_supported.from_dict(virtual_hardware_version_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


