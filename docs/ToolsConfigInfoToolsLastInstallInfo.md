# ToolsConfigInfoToolsLastInstallInfo

Describes status of last tools upgrade attempt  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter** | **int** | Number of attempts that have been made to upgrade the version of tools installed on this virtual machine.  ***Since:*** vSphere API 5.0  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.tools_config_info_tools_last_install_info import ToolsConfigInfoToolsLastInstallInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsConfigInfoToolsLastInstallInfo from a JSON string
tools_config_info_tools_last_install_info_instance = ToolsConfigInfoToolsLastInstallInfo.from_json(json)
# print the JSON string representation of the object
print ToolsConfigInfoToolsLastInstallInfo.to_json()

# convert the object into a dict
tools_config_info_tools_last_install_info_dict = tools_config_info_tools_last_install_info_instance.to_dict()
# create an instance of ToolsConfigInfoToolsLastInstallInfo from a dict
tools_config_info_tools_last_install_info_form_dict = tools_config_info_tools_last_install_info.from_dict(tools_config_info_tools_last_install_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


