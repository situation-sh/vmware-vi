# ToolsUpgradeCancelled

Thrown when tools install or upgrade fails because the operation was canclled by the user.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_upgrade_cancelled import ToolsUpgradeCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsUpgradeCancelled from a JSON string
tools_upgrade_cancelled_instance = ToolsUpgradeCancelled.from_json(json)
# print the JSON string representation of the object
print ToolsUpgradeCancelled.to_json()

# convert the object into a dict
tools_upgrade_cancelled_dict = tools_upgrade_cancelled_instance.to_dict()
# create an instance of ToolsUpgradeCancelled from a dict
tools_upgrade_cancelled_form_dict = tools_upgrade_cancelled.from_dict(tools_upgrade_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


