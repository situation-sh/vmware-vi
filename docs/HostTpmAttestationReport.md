# HostTpmAttestationReport

This class is used to report Trusted Platform Module (TPM) attestation information - values of the Platform Configuration Registers (PCRs) and the TPM event log to the external clients.  This information can be used to determine the integrity of the software stack running as reported by the platform.  The TPM stores digests (hashes) of the software stack components running on the host. Both binary modules and configuration information can be hashed. The calculated hash values are stored in special-purpose hardware registers called PCRs. Each PCR is defined to hold cumulative digest(s) of specific part(s) of the software stack.  Due to the limited amount of PCRs available a hash-chaining scheme is implemented. When adding new information to a PCR the new value of hash is computed according to the following formula: NewHash = hash\\_function(OldHash + hash\\_function(NewData)) This scheme allows storing measurements of an unlimited amount of components.  The TPM event log provides an exact sequence of the events that contributed to the value of a PCR. It contains information about the type of the event and event-specific information. The presence of the log allows verification of both the final PCR state and the entire attestation path that formed it.  It is possible for this report to be unreliable. This could be due to missing package information in the host database, errors in creation of the events. Only first 1000 events are recorded by the kernel. Further events will not be recorded in the log and will cause the log to be marked as incomplete.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tpm_pcr_values** | [**List[HostTpmDigestInfo]**](HostTpmDigestInfo.md) | The array of PCR digest values stored in the TPM device since the last host boot time.  ***Since:*** vSphere API 5.1  | 
**tpm_events** | [**List[HostTpmEventLogEntry]**](HostTpmEventLogEntry.md) | Log of TPM software stack attestation events.  ***Since:*** vSphere API 5.1  | 
**tpm_log_reliable** | **bool** | This flag indicates whether the provided TPM events are a complete and reliable information about host boot status.  TPM event log may be incomplete (and therfore unreliable) if certain modules have inappropriate origin or if the package information is incomplete. Only first 1000 events are recorded by the kernel. Further events will not be recorded in the log and will cause the log to be marked as unreliable.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_tpm_attestation_report import HostTpmAttestationReport

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmAttestationReport from a JSON string
host_tpm_attestation_report_instance = HostTpmAttestationReport.from_json(json)
# print the JSON string representation of the object
print HostTpmAttestationReport.to_json()

# convert the object into a dict
host_tpm_attestation_report_dict = host_tpm_attestation_report_instance.to_dict()
# create an instance of HostTpmAttestationReport from a dict
host_tpm_attestation_report_form_dict = host_tpm_attestation_report.from_dict(host_tpm_attestation_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


