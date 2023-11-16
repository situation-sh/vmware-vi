# NoClientCertificate

This exception is thrown when a client has connected without supplying a certificate but the associated call expects that the client has done so.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_client_certificate import NoClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of NoClientCertificate from a JSON string
no_client_certificate_instance = NoClientCertificate.from_json(json)
# print the JSON string representation of the object
print NoClientCertificate.to_json()

# convert the object into a dict
no_client_certificate_dict = no_client_certificate_instance.to_dict()
# create an instance of NoClientCertificate from a dict
no_client_certificate_form_dict = no_client_certificate.from_dict(no_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


