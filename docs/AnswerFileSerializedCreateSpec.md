# AnswerFileSerializedCreateSpec

The *AnswerFileSerializedCreateSpec* data object contains a serialized string representation of host-specific data for an answer file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_file_config_string** | **str** | Host-specific user input.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.answer_file_serialized_create_spec import AnswerFileSerializedCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileSerializedCreateSpec from a JSON string
answer_file_serialized_create_spec_instance = AnswerFileSerializedCreateSpec.from_json(json)
# print the JSON string representation of the object
print AnswerFileSerializedCreateSpec.to_json()

# convert the object into a dict
answer_file_serialized_create_spec_dict = answer_file_serialized_create_spec_instance.to_dict()
# create an instance of AnswerFileSerializedCreateSpec from a dict
answer_file_serialized_create_spec_form_dict = answer_file_serialized_create_spec.from_dict(answer_file_serialized_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


