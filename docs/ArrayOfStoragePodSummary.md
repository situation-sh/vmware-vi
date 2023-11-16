# ArrayOfStoragePodSummary

A boxed array of *StoragePodSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StoragePodSummary]**](StoragePodSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_pod_summary import ArrayOfStoragePodSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStoragePodSummary from a JSON string
array_of_storage_pod_summary_instance = ArrayOfStoragePodSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfStoragePodSummary.to_json()

# convert the object into a dict
array_of_storage_pod_summary_dict = array_of_storage_pod_summary_instance.to_dict()
# create an instance of ArrayOfStoragePodSummary from a dict
array_of_storage_pod_summary_form_dict = array_of_storage_pod_summary.from_dict(array_of_storage_pod_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


