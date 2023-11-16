# ArrayOfHostMultipathInfoPath

A boxed array of *HostMultipathInfoPath*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMultipathInfoPath]**](HostMultipathInfoPath.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_multipath_info_path import ArrayOfHostMultipathInfoPath

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMultipathInfoPath from a JSON string
array_of_host_multipath_info_path_instance = ArrayOfHostMultipathInfoPath.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMultipathInfoPath.to_json()

# convert the object into a dict
array_of_host_multipath_info_path_dict = array_of_host_multipath_info_path_instance.to_dict()
# create an instance of ArrayOfHostMultipathInfoPath from a dict
array_of_host_multipath_info_path_form_dict = array_of_host_multipath_info_path.from_dict(array_of_host_multipath_info_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


