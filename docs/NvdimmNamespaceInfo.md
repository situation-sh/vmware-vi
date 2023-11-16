# NvdimmNamespaceInfo

Deprecated as of vSphere 6.7u1, use NamespaceDetails.  Detailed information about a particular namespace.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Universally unique identifier assigned to namespace in string format  ***Since:*** vSphere API 6.7  | 
**friendly_name** | **str** | Friendly name of namespace  ***Since:*** vSphere API 6.7  | 
**block_size** | **int** | Size of logical block size.  For persistent region type, block size is one. For block region, block size represents one of the logical block sizes of 512, 4096 etc.  ***Since:*** vSphere API 6.7  | 
**block_count** | **int** | Number of blocks in the namespace.  For persistent region type, blockCount is the size of persistent region in bytes. For block region type, block count represent number of bytes per block size.  ***Since:*** vSphere API 6.7  | 
**type** | **str** | Type of the namespace to be created - block or persistent.  Must be one of the values in *NvdimmNamespaceType_enum*  ***Since:*** vSphere API 6.7  | 
**namespace_health_status** | **str** | Health status of DIMM(s) part of the namespace.  Must be one of the values of *NvdimmNamespaceHealthStatus_enum*  ***Since:*** vSphere API 6.7  | 
**location_id** | **int** | This identifier is the interleave set ID if this namespace is being used in persistent mode.  If in block mode, this is a nvdimm device handle.  ***Since:*** vSphere API 6.7  | 
**state** | **str** | State of namespace.  Must be one of *NvdimmNamespaceState_enum*  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_namespace_info import NvdimmNamespaceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmNamespaceInfo from a JSON string
nvdimm_namespace_info_instance = NvdimmNamespaceInfo.from_json(json)
# print the JSON string representation of the object
print NvdimmNamespaceInfo.to_json()

# convert the object into a dict
nvdimm_namespace_info_dict = nvdimm_namespace_info_instance.to_dict()
# create an instance of NvdimmNamespaceInfo from a dict
nvdimm_namespace_info_form_dict = nvdimm_namespace_info.from_dict(nvdimm_namespace_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


