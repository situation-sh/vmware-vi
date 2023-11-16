# ArrayOfHostIoFilterInfo

A boxed array of *HostIoFilterInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIoFilterInfo]**](HostIoFilterInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_io_filter_info import ArrayOfHostIoFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIoFilterInfo from a JSON string
array_of_host_io_filter_info_instance = ArrayOfHostIoFilterInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIoFilterInfo.to_json()

# convert the object into a dict
array_of_host_io_filter_info_dict = array_of_host_io_filter_info_instance.to_dict()
# create an instance of ArrayOfHostIoFilterInfo from a dict
array_of_host_io_filter_info_form_dict = array_of_host_io_filter_info.from_dict(array_of_host_io_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


