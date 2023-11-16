# HostAutoStartManagerConfig

Contains the entire auto-start/auto-stop configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaults** | [**AutoStartDefaults**](AutoStartDefaults.md) |  | [optional] 
**power_info** | [**List[AutoStartPowerInfo]**](AutoStartPowerInfo.md) | Lists the auto-start/auto-stop configuration.  If a virtual machine is not mentioned in this array, it does not participate in auto-start/auto-stop operations.  | [optional] 

## Example

```python
from vmware_vi.models.host_auto_start_manager_config import HostAutoStartManagerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostAutoStartManagerConfig from a JSON string
host_auto_start_manager_config_instance = HostAutoStartManagerConfig.from_json(json)
# print the JSON string representation of the object
print HostAutoStartManagerConfig.to_json()

# convert the object into a dict
host_auto_start_manager_config_dict = host_auto_start_manager_config_instance.to_dict()
# create an instance of HostAutoStartManagerConfig from a dict
host_auto_start_manager_config_form_dict = host_auto_start_manager_config.from_dict(host_auto_start_manager_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


