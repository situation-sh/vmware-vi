# CheckAnswerFileStatusRequestType

The parameters of *HostProfileManager.CheckAnswerFileStatus_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Set of hosts for which the answer file status will be checked.  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.check_answer_file_status_request_type import CheckAnswerFileStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAnswerFileStatusRequestType from a JSON string
check_answer_file_status_request_type_instance = CheckAnswerFileStatusRequestType.from_json(json)
# print the JSON string representation of the object
print CheckAnswerFileStatusRequestType.to_json()

# convert the object into a dict
check_answer_file_status_request_type_dict = check_answer_file_status_request_type_instance.to_dict()
# create an instance of CheckAnswerFileStatusRequestType from a dict
check_answer_file_status_request_type_form_dict = check_answer_file_status_request_type.from_dict(check_answer_file_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


