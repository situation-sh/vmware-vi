# ArrayOfHostTpmNvTagEventDetails

A boxed array of *HostTpmNvTagEventDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmNvTagEventDetails]**](HostTpmNvTagEventDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_nv_tag_event_details import ArrayOfHostTpmNvTagEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmNvTagEventDetails from a JSON string
array_of_host_tpm_nv_tag_event_details_instance = ArrayOfHostTpmNvTagEventDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmNvTagEventDetails.to_json()

# convert the object into a dict
array_of_host_tpm_nv_tag_event_details_dict = array_of_host_tpm_nv_tag_event_details_instance.to_dict()
# create an instance of ArrayOfHostTpmNvTagEventDetails from a dict
array_of_host_tpm_nv_tag_event_details_form_dict = array_of_host_tpm_nv_tag_event_details.from_dict(array_of_host_tpm_nv_tag_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


