# QueryIoFilterInfoRequestType

The parameters of *IoFilterManager.QueryIoFilterInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comp_res** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_io_filter_info_request_type import QueryIoFilterInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryIoFilterInfoRequestType from a JSON string
query_io_filter_info_request_type_instance = QueryIoFilterInfoRequestType.from_json(json)
# print the JSON string representation of the object
print QueryIoFilterInfoRequestType.to_json()

# convert the object into a dict
query_io_filter_info_request_type_dict = query_io_filter_info_request_type_instance.to_dict()
# create an instance of QueryIoFilterInfoRequestType from a dict
query_io_filter_info_request_type_form_dict = query_io_filter_info_request_type.from_dict(query_io_filter_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


