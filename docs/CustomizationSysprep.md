# CustomizationSysprep

An object representation of a Windows `sysprep.xml` answer file.  The sysprep type encloses all the individual keys listed in a `sysprep.xml` file. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gui_unattended** | [**CustomizationGuiUnattended**](CustomizationGuiUnattended.md) |  | 
**user_data** | [**CustomizationUserData**](CustomizationUserData.md) |  | 
**gui_run_once** | [**CustomizationGuiRunOnce**](CustomizationGuiRunOnce.md) |  | [optional] 
**identification** | [**CustomizationIdentification**](CustomizationIdentification.md) |  | 
**license_file_print_data** | [**CustomizationLicenseFilePrintData**](CustomizationLicenseFilePrintData.md) |  | [optional] 

## Example

```python
from vmware_vi.models.customization_sysprep import CustomizationSysprep

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSysprep from a JSON string
customization_sysprep_instance = CustomizationSysprep.from_json(json)
# print the JSON string representation of the object
print CustomizationSysprep.to_json()

# convert the object into a dict
customization_sysprep_dict = customization_sysprep_instance.to_dict()
# create an instance of CustomizationSysprep from a dict
customization_sysprep_form_dict = customization_sysprep.from_dict(customization_sysprep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


