# ArrayOfVirtualMachineQuestionInfo

A boxed array of *VirtualMachineQuestionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineQuestionInfo]**](VirtualMachineQuestionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_question_info import ArrayOfVirtualMachineQuestionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineQuestionInfo from a JSON string
array_of_virtual_machine_question_info_instance = ArrayOfVirtualMachineQuestionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineQuestionInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_question_info_dict = array_of_virtual_machine_question_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineQuestionInfo from a dict
array_of_virtual_machine_question_info_form_dict = array_of_virtual_machine_question_info.from_dict(array_of_virtual_machine_question_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


