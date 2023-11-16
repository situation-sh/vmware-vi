# ArrayOfBatchResult

A boxed array of *BatchResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BatchResult]**](BatchResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_batch_result import ArrayOfBatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBatchResult from a JSON string
array_of_batch_result_instance = ArrayOfBatchResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfBatchResult.to_json()

# convert the object into a dict
array_of_batch_result_dict = array_of_batch_result_instance.to_dict()
# create an instance of ArrayOfBatchResult from a dict
array_of_batch_result_form_dict = array_of_batch_result.from_dict(array_of_batch_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


