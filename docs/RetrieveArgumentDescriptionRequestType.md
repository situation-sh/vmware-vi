# RetrieveArgumentDescriptionRequestType

The parameters of *EventManager.RetrieveArgumentDescription*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** |  | 

## Example

```python
from vmware_vi.models.retrieve_argument_description_request_type import RetrieveArgumentDescriptionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveArgumentDescriptionRequestType from a JSON string
retrieve_argument_description_request_type_instance = RetrieveArgumentDescriptionRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveArgumentDescriptionRequestType.to_json()

# convert the object into a dict
retrieve_argument_description_request_type_dict = retrieve_argument_description_request_type_instance.to_dict()
# create an instance of RetrieveArgumentDescriptionRequestType from a dict
retrieve_argument_description_request_type_form_dict = retrieve_argument_description_request_type.from_dict(retrieve_argument_description_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


