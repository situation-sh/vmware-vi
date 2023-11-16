# ServiceLocatorCredential

The data object type is a base type of credential for authentication such as username/password or SAML token.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.service_locator_credential import ServiceLocatorCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocatorCredential from a JSON string
service_locator_credential_instance = ServiceLocatorCredential.from_json(json)
# print the JSON string representation of the object
print ServiceLocatorCredential.to_json()

# convert the object into a dict
service_locator_credential_dict = service_locator_credential_instance.to_dict()
# create an instance of ServiceLocatorCredential from a dict
service_locator_credential_form_dict = service_locator_credential.from_dict(service_locator_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


