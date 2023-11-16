# HostVFlashResourceConfigurationResult

vFlash resource configuration result returns the newly-configured backend VFFS volume and operation result for each passed-in SSD device.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **List[str]** | The original array of device path which user had specified  ***Since:*** vSphere API 5.5  | [optional] 
**vffs** | [**HostVffsVolume**](HostVffsVolume.md) |  | [optional] 
**disk_configuration_result** | [**List[HostDiskConfigurationResult]**](HostDiskConfigurationResult.md) | Array of device operation results.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_v_flash_resource_configuration_result import HostVFlashResourceConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashResourceConfigurationResult from a JSON string
host_v_flash_resource_configuration_result_instance = HostVFlashResourceConfigurationResult.from_json(json)
# print the JSON string representation of the object
print HostVFlashResourceConfigurationResult.to_json()

# convert the object into a dict
host_v_flash_resource_configuration_result_dict = host_v_flash_resource_configuration_result_instance.to_dict()
# create an instance of HostVFlashResourceConfigurationResult from a dict
host_v_flash_resource_configuration_result_form_dict = host_v_flash_resource_configuration_result.from_dict(host_v_flash_resource_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


