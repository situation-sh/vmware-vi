# CancelRetrievePropertiesExRequestType

The parameters of *PropertyCollector.CancelRetrievePropertiesEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | the token returned in the previous *RetrieveResult* returned on the same session by the same *PropertyCollector*.  | 

## Example

```python
from vmware_vi.models.cancel_retrieve_properties_ex_request_type import CancelRetrievePropertiesExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CancelRetrievePropertiesExRequestType from a JSON string
cancel_retrieve_properties_ex_request_type_instance = CancelRetrievePropertiesExRequestType.from_json(json)
# print the JSON string representation of the object
print CancelRetrievePropertiesExRequestType.to_json()

# convert the object into a dict
cancel_retrieve_properties_ex_request_type_dict = cancel_retrieve_properties_ex_request_type_instance.to_dict()
# create an instance of CancelRetrievePropertiesExRequestType from a dict
cancel_retrieve_properties_ex_request_type_form_dict = cancel_retrieve_properties_ex_request_type.from_dict(cancel_retrieve_properties_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


