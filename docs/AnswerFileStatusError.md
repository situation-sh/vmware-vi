# AnswerFileStatusError

The *AnswerFileStatusError* data object describes an answer file error and identifies the profile or policy option with which the error is associated.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input_path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | 
**err_msg** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.answer_file_status_error import AnswerFileStatusError

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileStatusError from a JSON string
answer_file_status_error_instance = AnswerFileStatusError.from_json(json)
# print the JSON string representation of the object
print AnswerFileStatusError.to_json()

# convert the object into a dict
answer_file_status_error_dict = answer_file_status_error_instance.to_dict()
# create an instance of AnswerFileStatusError from a dict
answer_file_status_error_form_dict = answer_file_status_error.from_dict(answer_file_status_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


