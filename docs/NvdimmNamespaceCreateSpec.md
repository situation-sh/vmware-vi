# NvdimmNamespaceCreateSpec

Deprecated as of vSphere 6.7u1, use PMemNamespaceCreateReq.  Arguments for creating a namespace.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_name** | **str** | Friendly name of the namespace to be created.  A friendly name can be provided by user to assosiate a name to the created namespace, but such a name is not mandatory and is empty string by default.  ***Since:*** vSphere API 6.7  | [optional] 
**block_size** | **int** | Size of block in the namespace.  For persistent region type, block size is one. For block region, block size represents one of the logical block sizes of 512, 4096 etc.  ***Since:*** vSphere API 6.7  | 
**block_count** | **int** | Number of blocks in the namespace.  For persistent region type, blockCount is the size of persistent region in bytes. For block region type, block count represent number of bytes per block size.  ***Since:*** vSphere API 6.7  | 
**type** | **str** | Type of the namespace to be created - block or persistent.  Must be one of the values in *NvdimmNamespaceType_enum*  ***Since:*** vSphere API 6.7  | 
**location_id** | **int** | This identifier is the interleave set ID if the namespace is being used in persistent mode.  If in block mode, this is a device handle.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_namespace_create_spec import NvdimmNamespaceCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmNamespaceCreateSpec from a JSON string
nvdimm_namespace_create_spec_instance = NvdimmNamespaceCreateSpec.from_json(json)
# print the JSON string representation of the object
print NvdimmNamespaceCreateSpec.to_json()

# convert the object into a dict
nvdimm_namespace_create_spec_dict = nvdimm_namespace_create_spec_instance.to_dict()
# create an instance of NvdimmNamespaceCreateSpec from a dict
nvdimm_namespace_create_spec_form_dict = nvdimm_namespace_create_spec.from_dict(nvdimm_namespace_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


