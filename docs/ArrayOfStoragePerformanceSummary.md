# ArrayOfStoragePerformanceSummary

A boxed array of *StoragePerformanceSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StoragePerformanceSummary]**](StoragePerformanceSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_performance_summary import ArrayOfStoragePerformanceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStoragePerformanceSummary from a JSON string
array_of_storage_performance_summary_instance = ArrayOfStoragePerformanceSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfStoragePerformanceSummary.to_json()

# convert the object into a dict
array_of_storage_performance_summary_dict = array_of_storage_performance_summary_instance.to_dict()
# create an instance of ArrayOfStoragePerformanceSummary from a dict
array_of_storage_performance_summary_form_dict = array_of_storage_performance_summary.from_dict(array_of_storage_performance_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


