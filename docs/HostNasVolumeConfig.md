# HostNasVolumeConfig

This describes the NAS Volume configuration containing the configurable properties on a NAS Volume  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | Indicates the change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**spec** | [**HostNasVolumeSpec**](HostNasVolumeSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_nas_volume_config import HostNasVolumeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostNasVolumeConfig from a JSON string
host_nas_volume_config_instance = HostNasVolumeConfig.from_json(json)
# print the JSON string representation of the object
print HostNasVolumeConfig.to_json()

# convert the object into a dict
host_nas_volume_config_dict = host_nas_volume_config_instance.to_dict()
# create an instance of HostNasVolumeConfig from a dict
host_nas_volume_config_form_dict = host_nas_volume_config.from_dict(host_nas_volume_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


