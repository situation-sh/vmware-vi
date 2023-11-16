# OvfConnectedDeviceIso


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename of the ISO  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_connected_device_iso import OvfConnectedDeviceIso

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConnectedDeviceIso from a JSON string
ovf_connected_device_iso_instance = OvfConnectedDeviceIso.from_json(json)
# print the JSON string representation of the object
print OvfConnectedDeviceIso.to_json()

# convert the object into a dict
ovf_connected_device_iso_dict = ovf_connected_device_iso_instance.to_dict()
# create an instance of OvfConnectedDeviceIso from a dict
ovf_connected_device_iso_form_dict = ovf_connected_device_iso.from_dict(ovf_connected_device_iso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


