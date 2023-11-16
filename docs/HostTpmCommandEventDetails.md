# HostTpmCommandEventDetails

Details of an Trusted Platform Module (TPM) event recording options entered manually on the command line prompt at boot time.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_line** | **str** | Boot options as entered on the command line prompt at boot time.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_tpm_command_event_details import HostTpmCommandEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmCommandEventDetails from a JSON string
host_tpm_command_event_details_instance = HostTpmCommandEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmCommandEventDetails.to_json()

# convert the object into a dict
host_tpm_command_event_details_dict = host_tpm_command_event_details_instance.to_dict()
# create an instance of HostTpmCommandEventDetails from a dict
host_tpm_command_event_details_form_dict = host_tpm_command_event_details.from_dict(host_tpm_command_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


