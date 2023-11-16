# ArrayOfPodStorageDrsEntry

A boxed array of *PodStorageDrsEntry*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PodStorageDrsEntry]**](PodStorageDrsEntry.md) |  | 

## Example

```python
from vmware_vi.models.array_of_pod_storage_drs_entry import ArrayOfPodStorageDrsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPodStorageDrsEntry from a JSON string
array_of_pod_storage_drs_entry_instance = ArrayOfPodStorageDrsEntry.from_json(json)
# print the JSON string representation of the object
print ArrayOfPodStorageDrsEntry.to_json()

# convert the object into a dict
array_of_pod_storage_drs_entry_dict = array_of_pod_storage_drs_entry_instance.to_dict()
# create an instance of ArrayOfPodStorageDrsEntry from a dict
array_of_pod_storage_drs_entry_form_dict = array_of_pod_storage_drs_entry.from_dict(array_of_pod_storage_drs_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


