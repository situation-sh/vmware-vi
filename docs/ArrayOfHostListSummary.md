# ArrayOfHostListSummary

A boxed array of *HostListSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostListSummary]**](HostListSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_list_summary import ArrayOfHostListSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostListSummary from a JSON string
array_of_host_list_summary_instance = ArrayOfHostListSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostListSummary.to_json()

# convert the object into a dict
array_of_host_list_summary_dict = array_of_host_list_summary_instance.to_dict()
# create an instance of ArrayOfHostListSummary from a dict
array_of_host_list_summary_form_dict = array_of_host_list_summary.from_dict(array_of_host_list_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


