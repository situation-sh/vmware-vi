# HostGraphicsConfig

Data object used for graphics configuration  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_default_graphics_type** | **str** | The host default graphics type (@see GraphicsType).  This default value can be overridden by specifying graphics type for an individual device. If host supports a single graphics type, specifying an individual graphics device is optional.  ***Since:*** vSphere API 6.5  | 
**shared_passthru_assignment_policy** | **str** | The policy for assigning shared passthrough VMs to a host graphics device (see @SharedPassthruAssignmentPolicy).  ***Since:*** vSphere API 6.5  | 
**device_type** | [**List[HostGraphicsConfigDeviceType]**](HostGraphicsConfigDeviceType.md) | Graphics devices and their associated type.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_graphics_config import HostGraphicsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostGraphicsConfig from a JSON string
host_graphics_config_instance = HostGraphicsConfig.from_json(json)
# print the JSON string representation of the object
print HostGraphicsConfig.to_json()

# convert the object into a dict
host_graphics_config_dict = host_graphics_config_instance.to_dict()
# create an instance of HostGraphicsConfig from a dict
host_graphics_config_form_dict = host_graphics_config.from_dict(host_graphics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


