# ArrayOfInvalidClientCertificate

A boxed array of *InvalidClientCertificate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidClientCertificate]**](InvalidClientCertificate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_client_certificate import ArrayOfInvalidClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidClientCertificate from a JSON string
array_of_invalid_client_certificate_instance = ArrayOfInvalidClientCertificate.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidClientCertificate.to_json()

# convert the object into a dict
array_of_invalid_client_certificate_dict = array_of_invalid_client_certificate_instance.to_dict()
# create an instance of ArrayOfInvalidClientCertificate from a dict
array_of_invalid_client_certificate_form_dict = array_of_invalid_client_certificate.from_dict(array_of_invalid_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


