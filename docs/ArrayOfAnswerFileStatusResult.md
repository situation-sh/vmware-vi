# ArrayOfAnswerFileStatusResult

A boxed array of *AnswerFileStatusResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AnswerFileStatusResult]**](AnswerFileStatusResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_answer_file_status_result import ArrayOfAnswerFileStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAnswerFileStatusResult from a JSON string
array_of_answer_file_status_result_instance = ArrayOfAnswerFileStatusResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfAnswerFileStatusResult.to_json()

# convert the object into a dict
array_of_answer_file_status_result_dict = array_of_answer_file_status_result_instance.to_dict()
# create an instance of ArrayOfAnswerFileStatusResult from a dict
array_of_answer_file_status_result_form_dict = array_of_answer_file_status_result.from_dict(array_of_answer_file_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


