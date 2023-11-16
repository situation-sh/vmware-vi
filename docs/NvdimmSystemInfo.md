# NvdimmSystemInfo

This data object represents Non-Volatile DIMMs host configuration.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**NvdimmSummary**](NvdimmSummary.md) |  | [optional] 
**dimms** | **List[int]** | List of NVDIMMs on the host.  NVDIMM list unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**dimm_info** | [**List[NvdimmDimmInfo]**](NvdimmDimmInfo.md) | List of DIMM information of all NVDIMMs on the host.  Dimm information is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**interleave_set** | **List[int]** | List of NVDIMM Interleave sets on the host.  Interleave set is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**i_set_info** | [**List[NvdimmInterleaveSetInfo]**](NvdimmInterleaveSetInfo.md) | List of information of all NVDIMM interleave sets on the host.  Interleave set information is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**namespace** | [**List[NvdimmGuid]**](NvdimmGuid.md) | List of NVDIMM namespaces on the host.  Namespace is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**ns_info** | [**List[NvdimmNamespaceInfo]**](NvdimmNamespaceInfo.md) | Deprecated as of vSphere 6.7u1, use nsDetails.  List of information of all NVDIMM namespaces on the host.  Namespace information is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7  | [optional] 
**ns_details** | [**List[NvdimmNamespaceDetails]**](NvdimmNamespaceDetails.md) | List of details of all NVDIMM namespaces on the host.  Namespace details is unset if the system does not support PMem feature.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.nvdimm_system_info import NvdimmSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmSystemInfo from a JSON string
nvdimm_system_info_instance = NvdimmSystemInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmSystemInfo.to_json()

# convert the object into a dict
nvdimm_system_info_dict = nvdimm_system_info_instance.to_dict()
# create an instance of NvdimmSystemInfo from a dict
nvdimm_system_info_form_dict = nvdimm_system_info.from_dict(nvdimm_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


