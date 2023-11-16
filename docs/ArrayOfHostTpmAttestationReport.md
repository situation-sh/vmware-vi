# ArrayOfHostTpmAttestationReport

A boxed array of *HostTpmAttestationReport*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmAttestationReport]**](HostTpmAttestationReport.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_attestation_report import ArrayOfHostTpmAttestationReport

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmAttestationReport from a JSON string
array_of_host_tpm_attestation_report_instance = ArrayOfHostTpmAttestationReport.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmAttestationReport.to_json()

# convert the object into a dict
array_of_host_tpm_attestation_report_dict = array_of_host_tpm_attestation_report_instance.to_dict()
# create an instance of ArrayOfHostTpmAttestationReport from a dict
array_of_host_tpm_attestation_report_form_dict = array_of_host_tpm_attestation_report.from_dict(array_of_host_tpm_attestation_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


