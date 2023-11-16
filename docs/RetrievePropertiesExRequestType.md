# RetrievePropertiesExRequestType

The parameters of *PropertyCollector.RetrievePropertiesEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_set** | [**List[PropertyFilterSpec]**](PropertyFilterSpec.md) | Specifies the properties to retrieve.  | 
**options** | [**RetrieveOptions**](RetrieveOptions.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_properties_ex_request_type import RetrievePropertiesExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievePropertiesExRequestType from a JSON string
retrieve_properties_ex_request_type_instance = RetrievePropertiesExRequestType.from_json(json)
# print the JSON string representation of the object
print RetrievePropertiesExRequestType.to_json()

# convert the object into a dict
retrieve_properties_ex_request_type_dict = retrieve_properties_ex_request_type_instance.to_dict()
# create an instance of RetrievePropertiesExRequestType from a dict
retrieve_properties_ex_request_type_form_dict = retrieve_properties_ex_request_type.from_dict(retrieve_properties_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


