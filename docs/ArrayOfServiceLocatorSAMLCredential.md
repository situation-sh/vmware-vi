# ArrayOfServiceLocatorSAMLCredential

A boxed array of *ServiceLocatorSAMLCredential*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceLocatorSAMLCredential]**](ServiceLocatorSAMLCredential.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_locator_saml_credential import ArrayOfServiceLocatorSAMLCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceLocatorSAMLCredential from a JSON string
array_of_service_locator_saml_credential_instance = ArrayOfServiceLocatorSAMLCredential.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceLocatorSAMLCredential.to_json()

# convert the object into a dict
array_of_service_locator_saml_credential_dict = array_of_service_locator_saml_credential_instance.to_dict()
# create an instance of ArrayOfServiceLocatorSAMLCredential from a dict
array_of_service_locator_saml_credential_form_dict = array_of_service_locator_saml_credential.from_dict(array_of_service_locator_saml_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


