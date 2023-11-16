# RetrievePropertiesRequestType

The parameters of *PropertyCollector.RetrieveProperties*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_set** | [**List[PropertyFilterSpec]**](PropertyFilterSpec.md) | Specifies the properties to retrieve.  | 

## Example

```python
from vmware_vi.models.retrieve_properties_request_type import RetrievePropertiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievePropertiesRequestType from a JSON string
retrieve_properties_request_type_instance = RetrievePropertiesRequestType.from_json(json)
# print the JSON string representation of the object
print RetrievePropertiesRequestType.to_json()

# convert the object into a dict
retrieve_properties_request_type_dict = retrieve_properties_request_type_instance.to_dict()
# create an instance of RetrievePropertiesRequestType from a dict
retrieve_properties_request_type_form_dict = retrieve_properties_request_type.from_dict(retrieve_properties_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


