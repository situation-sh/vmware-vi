# NvdimmRegionInfo

\\\\brief NVDIMM region information.  This represents a region which is a part of NVDIMM.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** | NVDIMM region ID  ***Since:*** vSphere API 6.7  | 
**set_id** | **int** | Interleave set ID.  Interleave set to which this region belongs. A value of 0 indicates that this region is not a part of any interleave set.  ***Since:*** vSphere API 6.7  | 
**range_type** | **str** | Type of region.  Must be one of the values of *NvdimmRangeType_enum*  ***Since:*** vSphere API 6.7  | 
**start_addr** | **int** | Region start address.  This represents the address within the NVDIMM to which this NVDIMM region belongs (Dimm physical address). If *NvdimmRegionInfo.setId* is 0, this field is not valid.  ***Since:*** vSphere API 6.7  | 
**size** | **int** | Size of region in bytes.  If this region is part of interleave set (represented by non zero *NvdimmRegionInfo.setId*) and the region is interleaved across multiple dimms (represented by more that one element in *NvdimmInterleaveSetInfo.deviceList* for assosiated set id *NvdimmRegionInfo.setId*), this size represents part of the interleave set size - (total interleave set size / number of dimms in *NvdimmInterleaveSetInfo.deviceList*). Example: If Interleave set with set id 5, has a size of 2TB and has 2 NVDIMMs contributing to it (size of *NvdimmInterleaveSetInfo.deviceList* is 2), then this size parameter is 2TB/2 &#x3D; 1TB. If *NvdimmRegionInfo.setId* is 0, this field is not valid.  ***Since:*** vSphere API 6.7  | 
**offset** | **int** | Offset of nvdimm within interleave set.  This represents offset with respect to base address in *NvdimmInterleaveSetInfo.baseAddress*. If *NvdimmRegionInfo.setId* is 0, this field is not valid.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_region_info import NvdimmRegionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmRegionInfo from a JSON string
nvdimm_region_info_instance = NvdimmRegionInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmRegionInfo.to_json()

# convert the object into a dict
nvdimm_region_info_dict = nvdimm_region_info_instance.to_dict()
# create an instance of NvdimmRegionInfo from a dict
nvdimm_region_info_form_dict = nvdimm_region_info.from_dict(nvdimm_region_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


