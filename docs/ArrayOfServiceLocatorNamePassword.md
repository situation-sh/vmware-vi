# ArrayOfServiceLocatorNamePassword

A boxed array of *ServiceLocatorNamePassword*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceLocatorNamePassword]**](ServiceLocatorNamePassword.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_locator_name_password import ArrayOfServiceLocatorNamePassword

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceLocatorNamePassword from a JSON string
array_of_service_locator_name_password_instance = ArrayOfServiceLocatorNamePassword.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceLocatorNamePassword.to_json()

# convert the object into a dict
array_of_service_locator_name_password_dict = array_of_service_locator_name_password_instance.to_dict()
# create an instance of ArrayOfServiceLocatorNamePassword from a dict
array_of_service_locator_name_password_form_dict = array_of_service_locator_name_password.from_dict(array_of_service_locator_name_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


