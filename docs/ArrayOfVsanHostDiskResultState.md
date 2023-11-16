# ArrayOfVsanHostDiskResultState

A boxed array of *VsanHostDiskResultState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostDiskResultStateEnum]**](VsanHostDiskResultStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_disk_result_state import ArrayOfVsanHostDiskResultState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostDiskResultState from a JSON string
array_of_vsan_host_disk_result_state_instance = ArrayOfVsanHostDiskResultState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostDiskResultState.to_json()

# convert the object into a dict
array_of_vsan_host_disk_result_state_dict = array_of_vsan_host_disk_result_state_instance.to_dict()
# create an instance of ArrayOfVsanHostDiskResultState from a dict
array_of_vsan_host_disk_result_state_form_dict = array_of_vsan_host_disk_result_state.from_dict(array_of_vsan_host_disk_result_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


