# VsanHostDiskResultState

A boxed *VsanHostDiskResultState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VsanHostDiskResultStateEnum**](VsanHostDiskResultStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.vsan_host_disk_result_state import VsanHostDiskResultState

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDiskResultState from a JSON string
vsan_host_disk_result_state_instance = VsanHostDiskResultState.from_json(json)
# print the JSON string representation of the object
print VsanHostDiskResultState.to_json()

# convert the object into a dict
vsan_host_disk_result_state_dict = vsan_host_disk_result_state_instance.to_dict()
# create an instance of VsanHostDiskResultState from a dict
vsan_host_disk_result_state_form_dict = vsan_host_disk_result_state.from_dict(vsan_host_disk_result_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


