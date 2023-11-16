# ArrayOfDpuStatusInfo

A boxed array of *DpuStatusInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DpuStatusInfo]**](DpuStatusInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dpu_status_info import ArrayOfDpuStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDpuStatusInfo from a JSON string
array_of_dpu_status_info_instance = ArrayOfDpuStatusInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfDpuStatusInfo.to_json()

# convert the object into a dict
array_of_dpu_status_info_dict = array_of_dpu_status_info_instance.to_dict()
# create an instance of ArrayOfDpuStatusInfo from a dict
array_of_dpu_status_info_form_dict = array_of_dpu_status_info.from_dict(array_of_dpu_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


