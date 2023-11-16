# ArrayOfSessionManagerServiceRequestSpec

A boxed array of *SessionManagerServiceRequestSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SessionManagerServiceRequestSpec]**](SessionManagerServiceRequestSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_session_manager_service_request_spec import ArrayOfSessionManagerServiceRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSessionManagerServiceRequestSpec from a JSON string
array_of_session_manager_service_request_spec_instance = ArrayOfSessionManagerServiceRequestSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfSessionManagerServiceRequestSpec.to_json()

# convert the object into a dict
array_of_session_manager_service_request_spec_dict = array_of_session_manager_service_request_spec_instance.to_dict()
# create an instance of ArrayOfSessionManagerServiceRequestSpec from a dict
array_of_session_manager_service_request_spec_form_dict = array_of_session_manager_service_request_spec.from_dict(array_of_session_manager_service_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


