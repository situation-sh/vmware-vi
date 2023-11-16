# HostTpmBootSecurityOptionEventDetails

Details of a Trusted Platform Module (TPM) event recording kernel security option passed at boot time and currently in effect.  This event type exists to simplify parsing of the security-related information by internal and third-party solutions. Each boot option may be passed to kernel multiple times and/or in different forms. Replicating the parsing logic of the kernel would be neither convinient, nor secure for the client applications.  Each instance of this event reports details of a single security-related boot option, as set in the kernel.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_security_option** | **str** | Security-related options string, reflecting the state of an option set in the kernel.  This string is in the form of a KEY&#x3D;VALUE pair.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_tpm_boot_security_option_event_details import HostTpmBootSecurityOptionEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmBootSecurityOptionEventDetails from a JSON string
host_tpm_boot_security_option_event_details_instance = HostTpmBootSecurityOptionEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmBootSecurityOptionEventDetails.to_json()

# convert the object into a dict
host_tpm_boot_security_option_event_details_dict = host_tpm_boot_security_option_event_details_instance.to_dict()
# create an instance of HostTpmBootSecurityOptionEventDetails from a dict
host_tpm_boot_security_option_event_details_form_dict = host_tpm_boot_security_option_event_details.from_dict(host_tpm_boot_security_option_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


