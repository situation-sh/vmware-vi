# OvfUnknownDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**VirtualDevice**](VirtualDevice.md) |  | [optional] 
**vm_name** | **str** | The name of the Virtual Machine containing the unkown device  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unknown_device import OvfUnknownDevice

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnknownDevice from a JSON string
ovf_unknown_device_instance = OvfUnknownDevice.from_json(json)
# print the JSON string representation of the object
print OvfUnknownDevice.to_json()

# convert the object into a dict
ovf_unknown_device_dict = ovf_unknown_device_instance.to_dict()
# create an instance of OvfUnknownDevice from a dict
ovf_unknown_device_form_dict = ovf_unknown_device.from_dict(ovf_unknown_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


