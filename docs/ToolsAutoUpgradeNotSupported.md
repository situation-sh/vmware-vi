# ToolsAutoUpgradeNotSupported

Thrown when tools upgrade fails because the virtual machine's guest operating system doesn't support tools auto-upgrades.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_auto_upgrade_not_supported import ToolsAutoUpgradeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsAutoUpgradeNotSupported from a JSON string
tools_auto_upgrade_not_supported_instance = ToolsAutoUpgradeNotSupported.from_json(json)
# print the JSON string representation of the object
print ToolsAutoUpgradeNotSupported.to_json()

# convert the object into a dict
tools_auto_upgrade_not_supported_dict = tools_auto_upgrade_not_supported_instance.to_dict()
# create an instance of ToolsAutoUpgradeNotSupported from a dict
tools_auto_upgrade_not_supported_form_dict = tools_auto_upgrade_not_supported.from_dict(tools_auto_upgrade_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


