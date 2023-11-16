# ArrayOfNoClientCertificate

A boxed array of *NoClientCertificate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoClientCertificate]**](NoClientCertificate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_client_certificate import ArrayOfNoClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoClientCertificate from a JSON string
array_of_no_client_certificate_instance = ArrayOfNoClientCertificate.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoClientCertificate.to_json()

# convert the object into a dict
array_of_no_client_certificate_dict = array_of_no_client_certificate_instance.to_dict()
# create an instance of ArrayOfNoClientCertificate from a dict
array_of_no_client_certificate_form_dict = array_of_no_client_certificate.from_dict(array_of_no_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


