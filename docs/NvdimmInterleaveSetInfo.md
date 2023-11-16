# NvdimmInterleaveSetInfo

Characteristics of an interleave set of a NVDIMM  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_id** | **int** | Unique set ID  ***Since:*** vSphere API 6.7  | 
**range_type** | **str** | Volatile or persistent interleave set.  Must be one of the values of *NvdimmRangeType_enum*  ***Since:*** vSphere API 6.7  | 
**base_address** | **int** | Start address of range  ***Since:*** vSphere API 6.7  | 
**size** | **int** | Length of range in bytes  ***Since:*** vSphere API 6.7  | 
**available_size** | **int** | Capacity currently not allocated to namespace in bytes  ***Since:*** vSphere API 6.7  | 
**device_list** | **List[int]** | List of nvdimms contributing to this interleave set  ***Since:*** vSphere API 6.7  | [optional] 
**state** | **str** | State of interleave set.  Must be one of the values in *NvdimmInterleaveSetState_enum*  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_interleave_set_info import NvdimmInterleaveSetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmInterleaveSetInfo from a JSON string
nvdimm_interleave_set_info_instance = NvdimmInterleaveSetInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmInterleaveSetInfo.to_json()

# convert the object into a dict
nvdimm_interleave_set_info_dict = nvdimm_interleave_set_info_instance.to_dict()
# create an instance of NvdimmInterleaveSetInfo from a dict
nvdimm_interleave_set_info_form_dict = nvdimm_interleave_set_info.from_dict(nvdimm_interleave_set_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


