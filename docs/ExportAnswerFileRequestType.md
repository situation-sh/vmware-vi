# ExportAnswerFileRequestType

The parameters of *HostProfileManager.ExportAnswerFile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.export_answer_file_request_type import ExportAnswerFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExportAnswerFileRequestType from a JSON string
export_answer_file_request_type_instance = ExportAnswerFileRequestType.from_json(json)
# print the JSON string representation of the object
print ExportAnswerFileRequestType.to_json()

# convert the object into a dict
export_answer_file_request_type_dict = export_answer_file_request_type_instance.to_dict()
# create an instance of ExportAnswerFileRequestType from a dict
export_answer_file_request_type_form_dict = export_answer_file_request_type.from_dict(export_answer_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


