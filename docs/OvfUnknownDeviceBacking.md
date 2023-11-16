# OvfUnknownDeviceBacking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing** | [**VirtualDeviceBackingInfo**](VirtualDeviceBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.ovf_unknown_device_backing import OvfUnknownDeviceBacking

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnknownDeviceBacking from a JSON string
ovf_unknown_device_backing_instance = OvfUnknownDeviceBacking.from_json(json)
# print the JSON string representation of the object
print OvfUnknownDeviceBacking.to_json()

# convert the object into a dict
ovf_unknown_device_backing_dict = ovf_unknown_device_backing_instance.to_dict()
# create an instance of OvfUnknownDeviceBacking from a dict
ovf_unknown_device_backing_form_dict = ovf_unknown_device_backing.from_dict(ovf_unknown_device_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


