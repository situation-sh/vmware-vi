# ArrayOfSAMLTokenAuthentication

A boxed array of *SAMLTokenAuthentication*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SAMLTokenAuthentication]**](SAMLTokenAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.array_of_saml_token_authentication import ArrayOfSAMLTokenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSAMLTokenAuthentication from a JSON string
array_of_saml_token_authentication_instance = ArrayOfSAMLTokenAuthentication.from_json(json)
# print the JSON string representation of the object
print ArrayOfSAMLTokenAuthentication.to_json()

# convert the object into a dict
array_of_saml_token_authentication_dict = array_of_saml_token_authentication_instance.to_dict()
# create an instance of ArrayOfSAMLTokenAuthentication from a dict
array_of_saml_token_authentication_form_dict = array_of_saml_token_authentication.from_dict(array_of_saml_token_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


