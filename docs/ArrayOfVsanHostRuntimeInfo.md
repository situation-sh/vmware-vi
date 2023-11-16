# ArrayOfVsanHostRuntimeInfo

A boxed array of *VsanHostRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostRuntimeInfo]**](VsanHostRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_runtime_info import ArrayOfVsanHostRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostRuntimeInfo from a JSON string
array_of_vsan_host_runtime_info_instance = ArrayOfVsanHostRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostRuntimeInfo.to_json()

# convert the object into a dict
array_of_vsan_host_runtime_info_dict = array_of_vsan_host_runtime_info_instance.to_dict()
# create an instance of ArrayOfVsanHostRuntimeInfo from a dict
array_of_vsan_host_runtime_info_form_dict = array_of_vsan_host_runtime_info.from_dict(array_of_vsan_host_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


