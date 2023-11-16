# CustomizationGuiUnattended

The GuiUnattended type maps to the GuiUnattended key in the `sysprep.xml` answer file.  These values are plugged directly into the `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**CustomizationPassword**](CustomizationPassword.md) |  | [optional] 
**time_zone** | **int** | The time zone index for the virtual machine.  Numbers correspond to time zones listed at &lt;a href&#x3D;\&quot;https://support.microsoft.com/en-us/help/973627/microsoft-time-zone-index-values\&quot;target&#x3D;\&quot;_blank\&quot;&gt;Microsoft Time Zone Index Values&lt;/a&gt;.  | 
**auto_logon** | **bool** | Flag to determine whether or not the machine automatically logs on as Administrator.  See also the password property.  If the AutoLogon flag is set, *CustomizationGuiUnattended.password* must not be blank or the guest customization will fail.  | 
**auto_logon_count** | **int** | If the AutoLogon flag is set, then the AutoLogonCount property specifies the number of times the machine should automatically log on as Administrator.  Generally it should be 1, but if your setup requires a number of reboots, you may want to increase it. This number may be determined by the list of commands executed by the *GuiRunOnce* command.  | 

## Example

```python
from vmware_vi.models.customization_gui_unattended import CustomizationGuiUnattended

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationGuiUnattended from a JSON string
customization_gui_unattended_instance = CustomizationGuiUnattended.from_json(json)
# print the JSON string representation of the object
print CustomizationGuiUnattended.to_json()

# convert the object into a dict
customization_gui_unattended_dict = customization_gui_unattended_instance.to_dict()
# create an instance of CustomizationGuiUnattended from a dict
customization_gui_unattended_form_dict = customization_gui_unattended.from_dict(customization_gui_unattended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


