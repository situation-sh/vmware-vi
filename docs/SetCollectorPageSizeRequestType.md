# SetCollectorPageSizeRequestType

The parameters of *HistoryCollector.SetCollectorPageSize*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** | The maximum number of items in the page.  | 

## Example

```python
from vmware_vi.models.set_collector_page_size_request_type import SetCollectorPageSizeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetCollectorPageSizeRequestType from a JSON string
set_collector_page_size_request_type_instance = SetCollectorPageSizeRequestType.from_json(json)
# print the JSON string representation of the object
print SetCollectorPageSizeRequestType.to_json()

# convert the object into a dict
set_collector_page_size_request_type_dict = set_collector_page_size_request_type_instance.to_dict()
# create an instance of SetCollectorPageSizeRequestType from a dict
set_collector_page_size_request_type_form_dict = set_collector_page_size_request_type.from_dict(set_collector_page_size_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


