# ArrayOfCustomizationPassword

A boxed array of *CustomizationPassword*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationPassword]**](CustomizationPassword.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_password import ArrayOfCustomizationPassword

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationPassword from a JSON string
array_of_customization_password_instance = ArrayOfCustomizationPassword.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationPassword.to_json()

# convert the object into a dict
array_of_customization_password_dict = array_of_customization_password_instance.to_dict()
# create an instance of ArrayOfCustomizationPassword from a dict
array_of_customization_password_form_dict = array_of_customization_password.from_dict(array_of_customization_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


