# CreateFilterRequestType

The parameters of *PropertyCollector.CreateFilter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**PropertyFilterSpec**](PropertyFilterSpec.md) |  | 
**partial_updates** | **bool** | Flag to specify whether a change to a nested property should report only the nested change or the entire specified property value. If the value is true, a change should report only the nested property. If the value is false, a change should report the enclosing property named in the filter.  | 

## Example

```python
from vmware_vi.models.create_filter_request_type import CreateFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFilterRequestType from a JSON string
create_filter_request_type_instance = CreateFilterRequestType.from_json(json)
# print the JSON string representation of the object
print CreateFilterRequestType.to_json()

# convert the object into a dict
create_filter_request_type_dict = create_filter_request_type_instance.to_dict()
# create an instance of CreateFilterRequestType from a dict
create_filter_request_type_form_dict = create_filter_request_type.from_dict(create_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


