# CustomizationLicenseFilePrintData

The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in the `sysprep.xml` answer file.  These values are transferred into the `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. LicenseFilePrintData provides licensing information for Windows server operating systems. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_mode** | [**CustomizationLicenseDataModeEnum**](CustomizationLicenseDataModeEnum.md) |  | 
**auto_users** | **int** | This key is valid only if AutoMode &#x3D; PerServer.  The integer value indicates the number of client licenses purchased for the VirtualCenter server being installed.  | [optional] 

## Example

```python
from vmware_vi.models.customization_license_file_print_data import CustomizationLicenseFilePrintData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationLicenseFilePrintData from a JSON string
customization_license_file_print_data_instance = CustomizationLicenseFilePrintData.from_json(json)
# print the JSON string representation of the object
print CustomizationLicenseFilePrintData.to_json()

# convert the object into a dict
customization_license_file_print_data_dict = customization_license_file_print_data_instance.to_dict()
# create an instance of CustomizationLicenseFilePrintData from a dict
customization_license_file_print_data_form_dict = customization_license_file_print_data.from_dict(customization_license_file_print_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


