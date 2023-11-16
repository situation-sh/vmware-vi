# QueryAnswerFileStatusRequestType

The parameters of *HostProfileManager.QueryAnswerFileStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The hosts the answer file is associated with.  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.query_answer_file_status_request_type import QueryAnswerFileStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAnswerFileStatusRequestType from a JSON string
query_answer_file_status_request_type_instance = QueryAnswerFileStatusRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAnswerFileStatusRequestType.to_json()

# convert the object into a dict
query_answer_file_status_request_type_dict = query_answer_file_status_request_type_instance.to_dict()
# create an instance of QueryAnswerFileStatusRequestType from a dict
query_answer_file_status_request_type_form_dict = query_answer_file_status_request_type.from_dict(query_answer_file_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


