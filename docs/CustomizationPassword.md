# CustomizationPassword

Contains a password string and a flag that specifies whether the string is in plain text or encrypted. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The password string.  It is encrypted if the associated plainText flag is false.  | 
**plain_text** | **bool** | Flag to specify whether or not the password is in plain text, rather than encrypted.  | 

## Example

```python
from vmware_vi.models.customization_password import CustomizationPassword

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationPassword from a JSON string
customization_password_instance = CustomizationPassword.from_json(json)
# print the JSON string representation of the object
print CustomizationPassword.to_json()

# convert the object into a dict
customization_password_dict = customization_password_instance.to_dict()
# create an instance of CustomizationPassword from a dict
customization_password_form_dict = customization_password.from_dict(customization_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


