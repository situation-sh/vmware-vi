# AnswerFileCreateSpec

Base class for host-specific answer file options.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validating** | **bool** | If \&quot;false\&quot;, then the answer file will be saved without being validated.  The default if not specified is \&quot;true\&quot;. This option should be used with caution, since the resulting answer file will not be checked for errors.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.answer_file_create_spec import AnswerFileCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFileCreateSpec from a JSON string
answer_file_create_spec_instance = AnswerFileCreateSpec.from_json(json)
# print the JSON string representation of the object
print AnswerFileCreateSpec.to_json()

# convert the object into a dict
answer_file_create_spec_dict = answer_file_create_spec_instance.to_dict()
# create an instance of AnswerFileCreateSpec from a dict
answer_file_create_spec_form_dict = answer_file_create_spec.from_dict(answer_file_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


