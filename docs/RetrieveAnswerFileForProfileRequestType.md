# RetrieveAnswerFileForProfileRequestType

The parameters of *HostProfileManager.RetrieveAnswerFileForProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**apply_profile** | [**HostApplyProfile**](HostApplyProfile.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_answer_file_for_profile_request_type import RetrieveAnswerFileForProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerFileForProfileRequestType from a JSON string
retrieve_answer_file_for_profile_request_type_instance = RetrieveAnswerFileForProfileRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveAnswerFileForProfileRequestType.to_json()

# convert the object into a dict
retrieve_answer_file_for_profile_request_type_dict = retrieve_answer_file_for_profile_request_type_instance.to_dict()
# create an instance of RetrieveAnswerFileForProfileRequestType from a dict
retrieve_answer_file_for_profile_request_type_form_dict = retrieve_answer_file_for_profile_request_type.from_dict(retrieve_answer_file_for_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


