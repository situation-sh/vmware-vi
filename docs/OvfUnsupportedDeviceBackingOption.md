# OvfUnsupportedDeviceBackingOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_name** | **str** | The element name  ***Since:*** vSphere API 4.0  | [optional] 
**instance_id** | **str** | The InstanceId for the hardware element  ***Since:*** vSphere API 4.0  | [optional] 
**device_name** | **str** | The device name  ***Since:*** vSphere API 4.0  | 
**backing_name** | **str** | The name of the VirtualDevice Backing Option not supported on the device.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_unsupported_device_backing_option import OvfUnsupportedDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedDeviceBackingOption from a JSON string
ovf_unsupported_device_backing_option_instance = OvfUnsupportedDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedDeviceBackingOption.to_json()

# convert the object into a dict
ovf_unsupported_device_backing_option_dict = ovf_unsupported_device_backing_option_instance.to_dict()
# create an instance of OvfUnsupportedDeviceBackingOption from a dict
ovf_unsupported_device_backing_option_form_dict = ovf_unsupported_device_backing_option.from_dict(ovf_unsupported_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


