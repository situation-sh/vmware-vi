# PasswordField

DataObject which represents a Password field.  Password is functionally equivalent to String.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.password_field import PasswordField

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordField from a JSON string
password_field_instance = PasswordField.from_json(json)
# print the JSON string representation of the object
print PasswordField.to_json()

# convert the object into a dict
password_field_dict = password_field_instance.to_dict()
# create an instance of PasswordField from a dict
password_field_form_dict = password_field.from_dict(password_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


