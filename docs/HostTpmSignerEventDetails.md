# HostTpmSignerEventDetails

Details of a Trusted Platform Module (TPM) event recording the measurement of a signing key. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_tpm_signer_event_details import HostTpmSignerEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmSignerEventDetails from a JSON string
host_tpm_signer_event_details_instance = HostTpmSignerEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmSignerEventDetails.to_json()

# convert the object into a dict
host_tpm_signer_event_details_dict = host_tpm_signer_event_details_instance.to_dict()
# create an instance of HostTpmSignerEventDetails from a dict
host_tpm_signer_event_details_form_dict = host_tpm_signer_event_details.from_dict(host_tpm_signer_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


