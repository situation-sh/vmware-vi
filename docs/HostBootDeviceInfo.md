# HostBootDeviceInfo

This data object represents the boot device information of the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_devices** | [**List[HostBootDevice]**](HostBootDevice.md) | The list of boot devices present on the host  ***Since:*** VI API 2.5  | [optional] 
**current_boot_device_key** | **str** | The key of the current boot device that the host is configured to boot.  This property is unset if the current boot device is disabled.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_boot_device_info import HostBootDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostBootDeviceInfo from a JSON string
host_boot_device_info_instance = HostBootDeviceInfo.from_json(json)
# print the JSON string representation of the object
print HostBootDeviceInfo.to_json()

# convert the object into a dict
host_boot_device_info_dict = host_boot_device_info_instance.to_dict()
# create an instance of HostBootDeviceInfo from a dict
host_boot_device_info_form_dict = host_boot_device_info.from_dict(host_boot_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


