# AnswerFileStatusResult

The *AnswerFileStatusResult* data object shows the validity of the answer file associated with a host.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_time** | **datetime** | Time that the answer file status was determined.  ***Since:*** vSphere API 5.0  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | **str** | Status of the answer file.  See *HostProfileManagerAnswerFileStatus_enum* for valid values.  ***Since:*** vSphere API 5.0  | 
**error** | [**List[AnswerFileStatusError]**](AnswerFileStatusError.md) | If &lt;code&gt;status&lt;/code&gt; is &lt;code&gt;invalid&lt;/code&gt;, this property contains a list of status error objects.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.answer_file_status_result import AnswerFileStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileStatusResult from a JSON string
answer_file_status_result_instance = AnswerFileStatusResult.from_json(json)
# print the JSON string representation of the object
print AnswerFileStatusResult.to_json()

# convert the object into a dict
answer_file_status_result_dict = answer_file_status_result_instance.to_dict()
# create an instance of AnswerFileStatusResult from a dict
answer_file_status_result_form_dict = answer_file_status_result.from_dict(answer_file_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


