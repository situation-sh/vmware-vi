# ArrayOfMultipleCertificatesVerifyFault

A boxed array of *MultipleCertificatesVerifyFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MultipleCertificatesVerifyFault]**](MultipleCertificatesVerifyFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_multiple_certificates_verify_fault import ArrayOfMultipleCertificatesVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMultipleCertificatesVerifyFault from a JSON string
array_of_multiple_certificates_verify_fault_instance = ArrayOfMultipleCertificatesVerifyFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfMultipleCertificatesVerifyFault.to_json()

# convert the object into a dict
array_of_multiple_certificates_verify_fault_dict = array_of_multiple_certificates_verify_fault_instance.to_dict()
# create an instance of ArrayOfMultipleCertificatesVerifyFault from a dict
array_of_multiple_certificates_verify_fault_form_dict = array_of_multiple_certificates_verify_fault.from_dict(array_of_multiple_certificates_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


