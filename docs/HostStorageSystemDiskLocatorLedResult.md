# HostStorageSystemDiskLocatorLedResult

Contains the result of turn Disk Locator Led On/Off request.  Used as return value by *HostStorageSystem.TurnDiskLocatorLedOn_Task* and *HostStorageSystem.TurnDiskLocatorLedOff_Task*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | UUID of LUN that has failed to turn on/off disk locator LED.  ***Since:*** vSphere API 6.0  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.host_storage_system_disk_locator_led_result import HostStorageSystemDiskLocatorLedResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageSystemDiskLocatorLedResult from a JSON string
host_storage_system_disk_locator_led_result_instance = HostStorageSystemDiskLocatorLedResult.from_json(json)
# print the JSON string representation of the object
print HostStorageSystemDiskLocatorLedResult.to_json()

# convert the object into a dict
host_storage_system_disk_locator_led_result_dict = host_storage_system_disk_locator_led_result_instance.to_dict()
# create an instance of HostStorageSystemDiskLocatorLedResult from a dict
host_storage_system_disk_locator_led_result_form_dict = host_storage_system_disk_locator_led_result.from_dict(host_storage_system_disk_locator_led_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


