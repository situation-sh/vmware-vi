# ArrayOfHostSriovInfo

A boxed array of *HostSriovInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSriovInfo]**](HostSriovInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sriov_info import ArrayOfHostSriovInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSriovInfo from a JSON string
array_of_host_sriov_info_instance = ArrayOfHostSriovInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSriovInfo.to_json()

# convert the object into a dict
array_of_host_sriov_info_dict = array_of_host_sriov_info_instance.to_dict()
# create an instance of ArrayOfHostSriovInfo from a dict
array_of_host_sriov_info_form_dict = array_of_host_sriov_info.from_dict(array_of_host_sriov_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


