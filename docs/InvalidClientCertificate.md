# InvalidClientCertificate

This exception is thrown when a client has provided a certificate that fails certificate validation at the server.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_client_certificate import InvalidClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidClientCertificate from a JSON string
invalid_client_certificate_instance = InvalidClientCertificate.from_json(json)
# print the JSON string representation of the object
print InvalidClientCertificate.to_json()

# convert the object into a dict
invalid_client_certificate_dict = invalid_client_certificate_instance.to_dict()
# create an instance of InvalidClientCertificate from a dict
invalid_client_certificate_form_dict = invalid_client_certificate.from_dict(invalid_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


