# NvdimmNamespaceDetails

Detailed information about a particular namespace.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Universally unique identifier assigned to namespace in string format  ***Since:*** vSphere API 6.7.1  | 
**friendly_name** | **str** | Human readable name of namespace  ***Since:*** vSphere API 6.7.1  | 
**size** | **int** | Size of namespace in bytes.  ***Since:*** vSphere API 6.7.1  | 
**type** | **str** | Type of the namespace to be created - block or persistent.  Must be one of the values in *NvdimmNamespaceType_enum*  ***Since:*** vSphere API 6.7.1  | 
**namespace_health_status** | **str** | Health status of DIMM(s) part of the namespace.  Must be one of the values of *NvdimmNamespaceDetailsHealthStatus_enum*  ***Since:*** vSphere API 6.7.1  | 
**interleaveset_id** | **int** | The interleave set ID of the namespace.  ***Since:*** vSphere API 6.7.1  | 
**state** | **str** | State of namespace.  Must be one of *NvdimmNamespaceDetailsState_enum*  ***Since:*** vSphere API 6.7.1  | 

## Example

```python
from vmware_vi.models.nvdimm_namespace_details import NvdimmNamespaceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmNamespaceDetails from a JSON string
nvdimm_namespace_details_instance = NvdimmNamespaceDetails.from_json(json)
# print the JSON string representation of the object
print NvdimmNamespaceDetails.to_json()

# convert the object into a dict
nvdimm_namespace_details_dict = nvdimm_namespace_details_instance.to_dict()
# create an instance of NvdimmNamespaceDetails from a dict
nvdimm_namespace_details_form_dict = nvdimm_namespace_details.from_dict(nvdimm_namespace_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


