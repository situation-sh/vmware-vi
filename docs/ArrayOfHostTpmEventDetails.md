# ArrayOfHostTpmEventDetails

A boxed array of *HostTpmEventDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmEventDetails]**](HostTpmEventDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_event_details import ArrayOfHostTpmEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmEventDetails from a JSON string
array_of_host_tpm_event_details_instance = ArrayOfHostTpmEventDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmEventDetails.to_json()

# convert the object into a dict
array_of_host_tpm_event_details_dict = array_of_host_tpm_event_details_instance.to_dict()
# create an instance of ArrayOfHostTpmEventDetails from a dict
array_of_host_tpm_event_details_form_dict = array_of_host_tpm_event_details.from_dict(array_of_host_tpm_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


