# AutoStartDefaults

Defines the system default auto-start/auto-stop values. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether or not auto-start manager is enabled.  | [optional] 
**start_delay** | **int** | System-default autoStart delay in seconds.  The default is 120 seconds.  | [optional] 
**stop_delay** | **int** | System-default autoStop delay in seconds.  The default is 120 seconds.  | [optional] 
**wait_for_heartbeat** | **bool** | System-default waitForHeartbeat setting.  | [optional] 
**stop_action** | **str** | System-default power-off action.  Used if the stopAction string in the AutoPowerInfo object for a particular machine is set to systemDefault. If stopAction and startAction for a virtual machine are both set to none, that virtual machine is removed from the AutoStart sequence.  | [optional] 

## Example

```python
from vmware_vi.models.auto_start_defaults import AutoStartDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of AutoStartDefaults from a JSON string
auto_start_defaults_instance = AutoStartDefaults.from_json(json)
# print the JSON string representation of the object
print AutoStartDefaults.to_json()

# convert the object into a dict
auto_start_defaults_dict = auto_start_defaults_instance.to_dict()
# create an instance of AutoStartDefaults from a dict
auto_start_defaults_form_dict = auto_start_defaults.from_dict(auto_start_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


