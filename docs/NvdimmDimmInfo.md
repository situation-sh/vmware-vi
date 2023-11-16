# NvdimmDimmInfo

Get detailed information of a nvdimm  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimm_handle** | **int** | Unique device identifier  ***Since:*** vSphere API 6.7  | 
**health_info** | [**NvdimmHealthInfo**](NvdimmHealthInfo.md) |  | 
**total_capacity** | **int** | Total capacity of NVDIMM in bytes  ***Since:*** vSphere API 6.7  | 
**persistent_capacity** | **int** | Total persistent capacity in DIMM (in bytes)  ***Since:*** vSphere API 6.7  | 
**available_persistent_capacity** | **int** | Persistent Capacity in DIMM currently not allocated  ***Since:*** vSphere API 6.7  | 
**volatile_capacity** | **int** | Total volatile capacity in DIMM (in bytes)  ***Since:*** vSphere API 6.7  | 
**available_volatile_capacity** | **int** | Volatile capacity in DIMM currently not allocated  ***Since:*** vSphere API 6.7  | 
**block_capacity** | **int** | Total block capacity in DIMM (in bytes)  ***Since:*** vSphere API 6.7  | 
**region_info** | [**List[NvdimmRegionInfo]**](NvdimmRegionInfo.md) | NVDIMM region information.  List of regions in the NVDIMM. These regions may or maynot be a part of an interleave set.  ***Since:*** vSphere API 6.7  | [optional] 
**representation_string** | **str** | NVDIMM Representation string which is a sequence of numbers to uniquely identify the DIMM.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_dimm_info import NvdimmDimmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmDimmInfo from a JSON string
nvdimm_dimm_info_instance = NvdimmDimmInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmDimmInfo.to_json()

# convert the object into a dict
nvdimm_dimm_info_dict = nvdimm_dimm_info_instance.to_dict()
# create an instance of NvdimmDimmInfo from a dict
nvdimm_dimm_info_form_dict = nvdimm_dimm_info.from_dict(nvdimm_dimm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


