# CustomizationIdentification

The Identification data object type provides information needed to join a workgroup or domain.  The Identification data object type maps to the Identification key in the `sysprep.xml` answer file. These values are transferred into the `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For more detailed information, see <a href=\"https://technet.microsoft.com/en-us/library/cc771830(v=ws.10).aspx\"target=\"_blank\">Performing Unattended Installations</a>. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_workgroup** | **str** | The workgroup that the virtual machine should join.  If this value is supplied, then the domain name and authentication fields must be empty.  | [optional] 
**join_domain** | **str** | The domain that the virtual machine should join.  If this value is supplied, then domainAdmin and domainAdminPassword must also be supplied, and the workgroup name must be empty.  | [optional] 
**domain_admin** | **str** | This is the domain user account used for authentication if the virtual machine is joining a domain.  The user does not need to be a domain administrator, but the account must have the privileges required to add computers to the domain.  | [optional] 
**domain_admin_password** | [**CustomizationPassword**](CustomizationPassword.md) |  | [optional] 

## Example

```python
from vmware_vi.models.customization_identification import CustomizationIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationIdentification from a JSON string
customization_identification_instance = CustomizationIdentification.from_json(json)
# print the JSON string representation of the object
print CustomizationIdentification.to_json()

# convert the object into a dict
customization_identification_dict = customization_identification_instance.to_dict()
# create an instance of CustomizationIdentification from a dict
customization_identification_form_dict = customization_identification.from_dict(customization_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


