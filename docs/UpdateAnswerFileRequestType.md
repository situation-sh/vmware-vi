# UpdateAnswerFileRequestType

The parameters of *HostProfileManager.UpdateAnswerFile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**config_spec** | [**AnswerFileCreateSpec**](AnswerFileCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_answer_file_request_type import UpdateAnswerFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnswerFileRequestType from a JSON string
update_answer_file_request_type_instance = UpdateAnswerFileRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateAnswerFileRequestType.to_json()

# convert the object into a dict
update_answer_file_request_type_dict = update_answer_file_request_type_instance.to_dict()
# create an instance of UpdateAnswerFileRequestType from a dict
update_answer_file_request_type_form_dict = update_answer_file_request_type.from_dict(update_answer_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


