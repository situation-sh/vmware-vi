# NoSubjectName

This exception is thrown when an extension has attempted to use certificate-based authentication but the extension has been registered without a subject name.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_subject_name import NoSubjectName

# TODO update the JSON string below
json = "{}"
# create an instance of NoSubjectName from a JSON string
no_subject_name_instance = NoSubjectName.from_json(json)
# print the JSON string representation of the object
print NoSubjectName.to_json()

# convert the object into a dict
no_subject_name_dict = no_subject_name_instance.to_dict()
# create an instance of NoSubjectName from a dict
no_subject_name_form_dict = no_subject_name.from_dict(no_subject_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


