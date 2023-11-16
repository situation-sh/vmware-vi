# MultipleCertificatesVerifyFaultThumbprintData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | The port used by the service.  ***Since:*** vSphere API 4.0  | 
**thumbprint** | **str** | The SSL thumbprint of the host&#39;s certificate used by the service.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.multiple_certificates_verify_fault_thumbprint_data import MultipleCertificatesVerifyFaultThumbprintData

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleCertificatesVerifyFaultThumbprintData from a JSON string
multiple_certificates_verify_fault_thumbprint_data_instance = MultipleCertificatesVerifyFaultThumbprintData.from_json(json)
# print the JSON string representation of the object
print MultipleCertificatesVerifyFaultThumbprintData.to_json()

# convert the object into a dict
multiple_certificates_verify_fault_thumbprint_data_dict = multiple_certificates_verify_fault_thumbprint_data_instance.to_dict()
# create an instance of MultipleCertificatesVerifyFaultThumbprintData from a dict
multiple_certificates_verify_fault_thumbprint_data_form_dict = multiple_certificates_verify_fault_thumbprint_data.from_dict(multiple_certificates_verify_fault_thumbprint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


