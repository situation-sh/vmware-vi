# CustomizationUserData

Personal data pertaining to the owner of the virtual machine.  The UserData data object type maps to the UserData key in the `sysprep.xml` answer file. These values are transferred directly into the `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** | User&#39;s full name.  | 
**org_name** | **str** | User&#39;s organization.  | 
**computer_name** | [**CustomizationName**](CustomizationName.md) |  | 
**product_id** | **str** | Microsoft Sysprep requires that a valid serial number be included in the answer file when mini-setup runs.  This serial number is ignored if the original guest operating system was installed using a volume-licensed CD.  | 

## Example

```python
from vmware_vi.models.customization_user_data import CustomizationUserData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationUserData from a JSON string
customization_user_data_instance = CustomizationUserData.from_json(json)
# print the JSON string representation of the object
print CustomizationUserData.to_json()

# convert the object into a dict
customization_user_data_dict = customization_user_data_instance.to_dict()
# create an instance of CustomizationUserData from a dict
customization_user_data_form_dict = customization_user_data.from_dict(customization_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


