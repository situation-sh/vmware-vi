# ArrayOfvslmVClockInfo

A boxed array of *vslmVClockInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VslmVClockInfo]**](VslmVClockInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_ofvslm_v_clock_info import ArrayOfvslmVClockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfvslmVClockInfo from a JSON string
array_ofvslm_v_clock_info_instance = ArrayOfvslmVClockInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfvslmVClockInfo.to_json()

# convert the object into a dict
array_ofvslm_v_clock_info_dict = array_ofvslm_v_clock_info_instance.to_dict()
# create an instance of ArrayOfvslmVClockInfo from a dict
array_ofvslm_v_clock_info_form_dict = array_ofvslm_v_clock_info.from_dict(array_ofvslm_v_clock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


