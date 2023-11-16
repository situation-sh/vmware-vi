# ServiceLocatorSAMLCredential

The data object type specifies the SAML token (SSO) based credential for authenticating to a service endpoint.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The SAML token for authentication  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.service_locator_saml_credential import ServiceLocatorSAMLCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocatorSAMLCredential from a JSON string
service_locator_saml_credential_instance = ServiceLocatorSAMLCredential.from_json(json)
# print the JSON string representation of the object
print ServiceLocatorSAMLCredential.to_json()

# convert the object into a dict
service_locator_saml_credential_dict = service_locator_saml_credential_instance.to_dict()
# create an instance of ServiceLocatorSAMLCredential from a dict
service_locator_saml_credential_form_dict = service_locator_saml_credential.from_dict(service_locator_saml_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


