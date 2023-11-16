# CustomizationWinOptions

Optional operations supported by the customization process for Windows. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_sid** | **bool** | The customization process should modify the machine&#39;s security identifier (SID).  For Vista OS and greater, SID will always be modified and a value of false will generate an error.  | 
**delete_accounts** | **bool** | Deprecated as of VI API 2.5, this value is ignored. Removing user accounts during customization is no longer supported. To change the administrator password, set the administrator password to blank in the master vm. Sysprep will then be able to change the password to the one specified by the *CustomizationGuiUnattended.password*.  If deleteAccounts is true, then all user accounts are removed from the system as part of the customization.  Mini-setup creates a new Administrator account with a blank password.  | 
**reboot** | [**CustomizationSysprepRebootOptionEnum**](CustomizationSysprepRebootOptionEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.customization_win_options import CustomizationWinOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationWinOptions from a JSON string
customization_win_options_instance = CustomizationWinOptions.from_json(json)
# print the JSON string representation of the object
print CustomizationWinOptions.to_json()

# convert the object into a dict
customization_win_options_dict = customization_win_options_instance.to_dict()
# create an instance of CustomizationWinOptions from a dict
customization_win_options_form_dict = customization_win_options.from_dict(customization_win_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


