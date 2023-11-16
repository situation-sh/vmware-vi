# AnswerFileOptionsCreateSpec

The *AnswerFileOptionsCreateSpec* data object contains host-specific user input for an answer file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input** | [**List[ProfileDeferredPolicyOptionParameter]**](ProfileDeferredPolicyOptionParameter.md) | List of parameters that contain host-specific data.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.answer_file_options_create_spec import AnswerFileOptionsCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileOptionsCreateSpec from a JSON string
answer_file_options_create_spec_instance = AnswerFileOptionsCreateSpec.from_json(json)
# print the JSON string representation of the object
print AnswerFileOptionsCreateSpec.to_json()

# convert the object into a dict
answer_file_options_create_spec_dict = answer_file_options_create_spec_instance.to_dict()
# create an instance of AnswerFileOptionsCreateSpec from a dict
answer_file_options_create_spec_form_dict = answer_file_options_create_spec.from_dict(answer_file_options_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


