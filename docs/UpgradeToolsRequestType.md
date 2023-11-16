# UpgradeToolsRequestType

The parameters of *VirtualMachine.UpgradeTools_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installer_options** | **str** | Command line options passed to the installer to modify the installation procedure for tools.  | [optional] 

## Example

```python
from vmware_vi.models.upgrade_tools_request_type import UpgradeToolsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeToolsRequestType from a JSON string
upgrade_tools_request_type_instance = UpgradeToolsRequestType.from_json(json)
# print the JSON string representation of the object
print UpgradeToolsRequestType.to_json()

# convert the object into a dict
upgrade_tools_request_type_dict = upgrade_tools_request_type_instance.to_dict()
# create an instance of UpgradeToolsRequestType from a dict
upgrade_tools_request_type_form_dict = upgrade_tools_request_type.from_dict(upgrade_tools_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


