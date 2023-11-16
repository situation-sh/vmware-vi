# HostDiskConfigurationResult

Disk configuration result returns success or fault of the operation on the disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The device path.  See *ScsiDisk*  ***Since:*** vSphere API 5.5  | [optional] 
**success** | **bool** | Flag to indicate if the operation is successful  ***Since:*** vSphere API 5.5  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_disk_configuration_result import HostDiskConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskConfigurationResult from a JSON string
host_disk_configuration_result_instance = HostDiskConfigurationResult.from_json(json)
# print the JSON string representation of the object
print HostDiskConfigurationResult.to_json()

# convert the object into a dict
host_disk_configuration_result_dict = host_disk_configuration_result_instance.to_dict()
# create an instance of HostDiskConfigurationResult from a dict
host_disk_configuration_result_form_dict = host_disk_configuration_result.from_dict(host_disk_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


