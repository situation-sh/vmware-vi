# ContinueRetrievePropertiesExRequestType

The parameters of *PropertyCollector.ContinueRetrievePropertiesEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | the token returned in the previous *RetrieveResult* returned on the same session by the same *PropertyCollector*.  | 

## Example

```python
from vmware_vi.models.continue_retrieve_properties_ex_request_type import ContinueRetrievePropertiesExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ContinueRetrievePropertiesExRequestType from a JSON string
continue_retrieve_properties_ex_request_type_instance = ContinueRetrievePropertiesExRequestType.from_json(json)
# print the JSON string representation of the object
print ContinueRetrievePropertiesExRequestType.to_json()

# convert the object into a dict
continue_retrieve_properties_ex_request_type_dict = continue_retrieve_properties_ex_request_type_instance.to_dict()
# create an instance of ContinueRetrievePropertiesExRequestType from a dict
continue_retrieve_properties_ex_request_type_form_dict = continue_retrieve_properties_ex_request_type.from_dict(continue_retrieve_properties_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


