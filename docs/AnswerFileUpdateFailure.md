# AnswerFileUpdateFailure

DataObject which represents the errors that occurred when an answer file update was performed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input_path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | 
**err_msg** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.answer_file_update_failure import AnswerFileUpdateFailure

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileUpdateFailure from a JSON string
answer_file_update_failure_instance = AnswerFileUpdateFailure.from_json(json)
# print the JSON string representation of the object
print AnswerFileUpdateFailure.to_json()

# convert the object into a dict
answer_file_update_failure_dict = answer_file_update_failure_instance.to_dict()
# create an instance of AnswerFileUpdateFailure from a dict
answer_file_update_failure_form_dict = answer_file_update_failure.from_dict(answer_file_update_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


