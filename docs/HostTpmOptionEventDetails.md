# HostTpmOptionEventDetails

Details of a Trusted Platform Module (TPM) event recording boot-time options.  The boot-time options set on the system are packaged into a file that is supplied to the kernel at boot time. The boot options may be a string of key=value pairs (possibly separated by a new line) or a blob of arbitrary data.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_file_name** | **str** | Name of the file containing the boot options.  ***Since:*** vSphere API 5.1  | 
**boot_options** | **List[int]** | Options set by the boot option package.  This array exposes the raw contents of the settings file (or files) that were passed to kernel during the boot up process, and, therefore, should be treated accordingly.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.host_tpm_option_event_details import HostTpmOptionEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmOptionEventDetails from a JSON string
host_tpm_option_event_details_instance = HostTpmOptionEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmOptionEventDetails.to_json()

# convert the object into a dict
host_tpm_option_event_details_dict = host_tpm_option_event_details_instance.to_dict()
# create an instance of HostTpmOptionEventDetails from a dict
host_tpm_option_event_details_form_dict = host_tpm_option_event_details.from_dict(host_tpm_option_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


