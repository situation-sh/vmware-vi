# CustomizationGuiRunOnce

The commands listed in the GuiRunOnce data object type are executed when a user logs on the first time after customization completes.  The logon may be driven by the *AutoLogon* setting.  The GuiRunOnce data object type maps to the GuiRunOnce key in the `sysprep.xml` answer file. These values are transferred into the `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_list** | **List[str]** | A list of commands to run at first user logon, after guest customization.  | 

## Example

```python
from vmware_vi.models.customization_gui_run_once import CustomizationGuiRunOnce

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationGuiRunOnce from a JSON string
customization_gui_run_once_instance = CustomizationGuiRunOnce.from_json(json)
# print the JSON string representation of the object
print CustomizationGuiRunOnce.to_json()

# convert the object into a dict
customization_gui_run_once_dict = customization_gui_run_once_instance.to_dict()
# create an instance of CustomizationGuiRunOnce from a dict
customization_gui_run_once_form_dict = customization_gui_run_once.from_dict(customization_gui_run_once_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


