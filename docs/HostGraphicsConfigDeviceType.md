# HostGraphicsConfigDeviceType

A particular graphics device and its associated type.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Graphics device identifier (ex.  PCI ID).  ***Since:*** vSphere API 6.5  | 
**graphics_type** | **str** | Graphics type (@see GraphicsType).  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.host_graphics_config_device_type import HostGraphicsConfigDeviceType

# TODO update the JSON string below
json = "{}"
# create an instance of HostGraphicsConfigDeviceType from a JSON string
host_graphics_config_device_type_instance = HostGraphicsConfigDeviceType.from_json(json)
# print the JSON string representation of the object
print HostGraphicsConfigDeviceType.to_json()

# convert the object into a dict
host_graphics_config_device_type_dict = host_graphics_config_device_type_instance.to_dict()
# create an instance of HostGraphicsConfigDeviceType from a dict
host_graphics_config_device_type_form_dict = host_graphics_config_device_type.from_dict(host_graphics_config_device_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


