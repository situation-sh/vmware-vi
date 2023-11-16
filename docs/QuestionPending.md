# QuestionPending

Thrown when an operation cannot be performed on a virtual machine because it has a pending question requiring user input.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text of the question from the virtual machine.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.question_pending import QuestionPending

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionPending from a JSON string
question_pending_instance = QuestionPending.from_json(json)
# print the JSON string representation of the object
print QuestionPending.to_json()

# convert the object into a dict
question_pending_dict = question_pending_instance.to_dict()
# create an instance of QuestionPending from a dict
question_pending_form_dict = question_pending.from_dict(question_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


