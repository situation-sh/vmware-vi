# ArrayOfAutoStartWaitHeartbeatSetting

A boxed array of *AutoStartWaitHeartbeatSetting_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AutoStartWaitHeartbeatSettingEnum]**](AutoStartWaitHeartbeatSettingEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_auto_start_wait_heartbeat_setting import ArrayOfAutoStartWaitHeartbeatSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAutoStartWaitHeartbeatSetting from a JSON string
array_of_auto_start_wait_heartbeat_setting_instance = ArrayOfAutoStartWaitHeartbeatSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfAutoStartWaitHeartbeatSetting.to_json()

# convert the object into a dict
array_of_auto_start_wait_heartbeat_setting_dict = array_of_auto_start_wait_heartbeat_setting_instance.to_dict()
# create an instance of ArrayOfAutoStartWaitHeartbeatSetting from a dict
array_of_auto_start_wait_heartbeat_setting_form_dict = array_of_auto_start_wait_heartbeat_setting.from_dict(array_of_auto_start_wait_heartbeat_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


