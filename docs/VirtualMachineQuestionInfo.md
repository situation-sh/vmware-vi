# VirtualMachineQuestionInfo

This data object type describes the question that is currently blocking a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier with an opaque value that specifies the pending question.  | 
**text** | **str** | Text that describes the pending question.  | 
**choice** | [**ChoiceOption**](ChoiceOption.md) |  | 
**message** | [**List[VirtualMachineMessage]**](VirtualMachineMessage.md) | The message data for the individual messages that comprise the question.  Only available on servers that support localization.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_question_info import VirtualMachineQuestionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineQuestionInfo from a JSON string
virtual_machine_question_info_instance = VirtualMachineQuestionInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineQuestionInfo.to_json()

# convert the object into a dict
virtual_machine_question_info_dict = virtual_machine_question_info_instance.to_dict()
# create an instance of VirtualMachineQuestionInfo from a dict
virtual_machine_question_info_form_dict = virtual_machine_question_info.from_dict(virtual_machine_question_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


