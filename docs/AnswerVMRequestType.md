# AnswerVMRequestType

The parameters of *VirtualMachine.AnswerVM*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_id** | **str** | The value from QuestionInfo.id that identifies the question to answer.  | 
**answer_choice** | **str** | The contents of the QuestionInfo.choice.value array element that identifies the desired answer.  | 

## Example

```python
from vmware_vi.models.answer_vm_request_type import AnswerVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerVMRequestType from a JSON string
answer_vm_request_type_instance = AnswerVMRequestType.from_json(json)
# print the JSON string representation of the object
print AnswerVMRequestType.to_json()

# convert the object into a dict
answer_vm_request_type_dict = answer_vm_request_type_instance.to_dict()
# create an instance of AnswerVMRequestType from a dict
answer_vm_request_type_form_dict = answer_vm_request_type.from_dict(answer_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


