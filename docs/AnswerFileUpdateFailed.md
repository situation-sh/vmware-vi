# AnswerFileUpdateFailed

Could not update the answer file as it has invalid inputs.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**List[AnswerFileUpdateFailure]**](AnswerFileUpdateFailure.md) | Failures encountered during answer file update  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.answer_file_update_failed import AnswerFileUpdateFailed

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileUpdateFailed from a JSON string
answer_file_update_failed_instance = AnswerFileUpdateFailed.from_json(json)
# print the JSON string representation of the object
print AnswerFileUpdateFailed.to_json()

# convert the object into a dict
answer_file_update_failed_dict = answer_file_update_failed_instance.to_dict()
# create an instance of AnswerFileUpdateFailed from a dict
answer_file_update_failed_form_dict = answer_file_update_failed.from_dict(answer_file_update_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


