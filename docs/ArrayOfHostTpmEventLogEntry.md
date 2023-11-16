# ArrayOfHostTpmEventLogEntry

A boxed array of *HostTpmEventLogEntry*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmEventLogEntry]**](HostTpmEventLogEntry.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_event_log_entry import ArrayOfHostTpmEventLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmEventLogEntry from a JSON string
array_of_host_tpm_event_log_entry_instance = ArrayOfHostTpmEventLogEntry.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmEventLogEntry.to_json()

# convert the object into a dict
array_of_host_tpm_event_log_entry_dict = array_of_host_tpm_event_log_entry_instance.to_dict()
# create an instance of ArrayOfHostTpmEventLogEntry from a dict
array_of_host_tpm_event_log_entry_form_dict = array_of_host_tpm_event_log_entry.from_dict(array_of_host_tpm_event_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


