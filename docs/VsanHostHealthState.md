# VsanHostHealthState

A boxed *VsanHostHealthState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VsanHostHealthStateEnum**](VsanHostHealthStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.vsan_host_health_state import VsanHostHealthState

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostHealthState from a JSON string
vsan_host_health_state_instance = VsanHostHealthState.from_json(json)
# print the JSON string representation of the object
print VsanHostHealthState.to_json()

# convert the object into a dict
vsan_host_health_state_dict = vsan_host_health_state_instance.to_dict()
# create an instance of VsanHostHealthState from a dict
vsan_host_health_state_form_dict = vsan_host_health_state.from_dict(vsan_host_health_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


