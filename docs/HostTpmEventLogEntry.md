# HostTpmEventLogEntry

This data object represents a single entry of an event log created by Trusted Platform Module (TPM).  An TPM event log entry represents a single change to the value of a Platform Configuration Register (PCR). It contains detailed information about the reason of PCR value change, and the specifics of the event.  Multiple objects of this type form an TPM event log. This log allows for verification of the both the software stack running on a host and the attestation process itself.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pcr_index** | **int** | Index of the PCR that was affected by the event.  ***Since:*** vSphere API 5.1  | 
**event_details** | [**HostTpmEventDetails**](HostTpmEventDetails.md) |  | 

## Example

```python
from vmware_vi.models.host_tpm_event_log_entry import HostTpmEventLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmEventLogEntry from a JSON string
host_tpm_event_log_entry_instance = HostTpmEventLogEntry.from_json(json)
# print the JSON string representation of the object
print HostTpmEventLogEntry.to_json()

# convert the object into a dict
host_tpm_event_log_entry_dict = host_tpm_event_log_entry_instance.to_dict()
# create an instance of HostTpmEventLogEntry from a dict
host_tpm_event_log_entry_form_dict = host_tpm_event_log_entry.from_dict(host_tpm_event_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


