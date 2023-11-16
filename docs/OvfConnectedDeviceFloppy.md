# OvfConnectedDeviceFloppy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename of the floppy image  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_connected_device_floppy import OvfConnectedDeviceFloppy

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConnectedDeviceFloppy from a JSON string
ovf_connected_device_floppy_instance = OvfConnectedDeviceFloppy.from_json(json)
# print the JSON string representation of the object
print OvfConnectedDeviceFloppy.to_json()

# convert the object into a dict
ovf_connected_device_floppy_dict = ovf_connected_device_floppy_instance.to_dict()
# create an instance of OvfConnectedDeviceFloppy from a dict
ovf_connected_device_floppy_form_dict = ovf_connected_device_floppy.from_dict(ovf_connected_device_floppy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


