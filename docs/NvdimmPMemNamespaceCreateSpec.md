# NvdimmPMemNamespaceCreateSpec

Arguments for creating a persistent memory mode namespace  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_name** | **str** | Friendly name of the namespace to be created.  A friendly name can be provided by user to associate a name to the created namespace, but such a name is not mandatory and is empty string by default.  ***Since:*** vSphere API 6.7.1  | [optional] 
**size** | **int** | Size of the namespace in bytes.  ***Since:*** vSphere API 6.7.1  | 
**interleaveset_id** | **int** | The interleave set ID of the namespace.  ***Since:*** vSphere API 6.7.1  | 

## Example

```python
from vmware_vi.models.nvdimm_p_mem_namespace_create_spec import NvdimmPMemNamespaceCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmPMemNamespaceCreateSpec from a JSON string
nvdimm_p_mem_namespace_create_spec_instance = NvdimmPMemNamespaceCreateSpec.from_json(json)
# print the JSON string representation of the object
print NvdimmPMemNamespaceCreateSpec.to_json()

# convert the object into a dict
nvdimm_p_mem_namespace_create_spec_dict = nvdimm_p_mem_namespace_create_spec_instance.to_dict()
# create an instance of NvdimmPMemNamespaceCreateSpec from a dict
nvdimm_p_mem_namespace_create_spec_form_dict = nvdimm_p_mem_namespace_create_spec.from_dict(nvdimm_p_mem_namespace_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


