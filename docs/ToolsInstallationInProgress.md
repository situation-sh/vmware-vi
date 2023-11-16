# ToolsInstallationInProgress

The virtual machine is currently in the progress of guest tools installation that prevents the migration operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_installation_in_progress import ToolsInstallationInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsInstallationInProgress from a JSON string
tools_installation_in_progress_instance = ToolsInstallationInProgress.from_json(json)
# print the JSON string representation of the object
print ToolsInstallationInProgress.to_json()

# convert the object into a dict
tools_installation_in_progress_dict = tools_installation_in_progress_instance.to_dict()
# create an instance of ToolsInstallationInProgress from a dict
tools_installation_in_progress_form_dict = tools_installation_in_progress.from_dict(tools_installation_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


