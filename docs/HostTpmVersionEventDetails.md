# HostTpmVersionEventDetails

Details of a Trusted Platform Module (TPM) event recording the measurement of a module version. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **bytearray** | A packed structure containing the module version.  | 

## Example

```python
from vmware_vi.models.host_tpm_version_event_details import HostTpmVersionEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmVersionEventDetails from a JSON string
host_tpm_version_event_details_instance = HostTpmVersionEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmVersionEventDetails.to_json()

# convert the object into a dict
host_tpm_version_event_details_dict = host_tpm_version_event_details_instance.to_dict()
# create an instance of HostTpmVersionEventDetails from a dict
host_tpm_version_event_details_form_dict = host_tpm_version_event_details.from_dict(host_tpm_version_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


