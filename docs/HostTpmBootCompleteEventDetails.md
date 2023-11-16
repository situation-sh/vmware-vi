# HostTpmBootCompleteEventDetails

Details of a Trusted Platform Module (TPM) event recording the measurement of boot complete event.  The event digest is hash of the string \"Boot Complete\" including the nul character. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_tpm_boot_complete_event_details import HostTpmBootCompleteEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmBootCompleteEventDetails from a JSON string
host_tpm_boot_complete_event_details_instance = HostTpmBootCompleteEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmBootCompleteEventDetails.to_json()

# convert the object into a dict
host_tpm_boot_complete_event_details_dict = host_tpm_boot_complete_event_details_instance.to_dict()
# create an instance of HostTpmBootCompleteEventDetails from a dict
host_tpm_boot_complete_event_details_form_dict = host_tpm_boot_complete_event_details.from_dict(host_tpm_boot_complete_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


