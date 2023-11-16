# HostTpmNvTagEventDetails

Details of an Trusted Platform Module (TPM) event recording TPM NVRAM tag.  ***Since:*** vSphere API 7.0.2.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_tpm_nv_tag_event_details import HostTpmNvTagEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmNvTagEventDetails from a JSON string
host_tpm_nv_tag_event_details_instance = HostTpmNvTagEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmNvTagEventDetails.to_json()

# convert the object into a dict
host_tpm_nv_tag_event_details_dict = host_tpm_nv_tag_event_details_instance.to_dict()
# create an instance of HostTpmNvTagEventDetails from a dict
host_tpm_nv_tag_event_details_form_dict = host_tpm_nv_tag_event_details.from_dict(host_tpm_nv_tag_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


