# NvdimmHealthInfo

\\\\brief NVDIMM health information  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_status** | **str** | Device health status.  ***Since:*** vSphere API 6.7  | 
**health_information** | **str** | Health status description.  ***Since:*** vSphere API 6.7  | 
**state_flag_info** | **List[str]** | State flag information.  This information is the cumulation of state flags of all the NVDIMM region state flags. It must be one or more of *NvdimmNvdimmHealthInfoState_enum*  ***Since:*** vSphere API 6.7  | [optional] 
**dimm_temperature** | **int** | Current Nvdimm temperature in degree Celsius.  ***Since:*** vSphere API 6.7  | 
**dimm_temperature_threshold** | **int** | Nvdimm temperature threshold.  Default value is 0, indicating threshold has not reached, if set to 1, reached threshold limit.  ***Since:*** vSphere API 6.7  | 
**spare_blocks_percentage** | **int** | Percentage of spare capavity as a percentage of factory configured space (valid range 0 to 100)  ***Since:*** vSphere API 6.7  | 
**spare_block_threshold** | **int** | Spare block threshold.  Default value is 0, indicating threshold has not reached, if set to 1, reached threshold limit.  ***Since:*** vSphere API 6.7  | 
**dimm_lifespan_percentage** | **int** | Lifespan of Nvdimm as percentage.  100% &#x3D; Warranted life span has reached.  ***Since:*** vSphere API 6.7  | 
**es_temperature** | **int** | Energy source current temperature in degree Celsius.  Default value is 0, indicating there is no energy source for these nvdimms.  ***Since:*** vSphere API 6.7  | [optional] 
**es_temperature_threshold** | **int** | Energy source temperature threshold.  Default value is 0, indicating threshold has not reached, if set to 1, reached threshold limit.  ***Since:*** vSphere API 6.7  | [optional] 
**es_lifespan_percentage** | **int** | Lifespan of Energy source as percentage.  100% &#x3D; Warranted life span has reached. Default value is 0, indicating there is no energy source.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.nvdimm_health_info import NvdimmHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmHealthInfo from a JSON string
nvdimm_health_info_instance = NvdimmHealthInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmHealthInfo.to_json()

# convert the object into a dict
nvdimm_health_info_dict = nvdimm_health_info_instance.to_dict()
# create an instance of NvdimmHealthInfo from a dict
nvdimm_health_info_form_dict = nvdimm_health_info.from_dict(nvdimm_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


