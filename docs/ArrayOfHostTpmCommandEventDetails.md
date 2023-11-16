# ArrayOfHostTpmCommandEventDetails

A boxed array of *HostTpmCommandEventDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmCommandEventDetails]**](HostTpmCommandEventDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_command_event_details import ArrayOfHostTpmCommandEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmCommandEventDetails from a JSON string
array_of_host_tpm_command_event_details_instance = ArrayOfHostTpmCommandEventDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmCommandEventDetails.to_json()

# convert the object into a dict
array_of_host_tpm_command_event_details_dict = array_of_host_tpm_command_event_details_instance.to_dict()
# create an instance of ArrayOfHostTpmCommandEventDetails from a dict
array_of_host_tpm_command_event_details_form_dict = array_of_host_tpm_command_event_details.from_dict(array_of_host_tpm_command_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


