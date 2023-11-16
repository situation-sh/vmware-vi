# OvfUnsupportedDeviceBackingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_name** | **str** | The element name  ***Since:*** vSphere API 4.0  | [optional] 
**instance_id** | **str** | The InstanceId on the hardware description  ***Since:*** vSphere API 4.0  | [optional] 
**device_name** | **str** | The device name  ***Since:*** vSphere API 4.0  | 
**backing_name** | **str** | The name of the VirtualDevice Backing Info not supported on the device.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_unsupported_device_backing_info import OvfUnsupportedDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedDeviceBackingInfo from a JSON string
ovf_unsupported_device_backing_info_instance = OvfUnsupportedDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedDeviceBackingInfo.to_json()

# convert the object into a dict
ovf_unsupported_device_backing_info_dict = ovf_unsupported_device_backing_info_instance.to_dict()
# create an instance of OvfUnsupportedDeviceBackingInfo from a dict
ovf_unsupported_device_backing_info_form_dict = ovf_unsupported_device_backing_info.from_dict(ovf_unsupported_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


