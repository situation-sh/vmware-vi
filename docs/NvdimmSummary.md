# NvdimmSummary

\\\\brief Get summary of nvdimm  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_dimms** | **int** | Number of NVDIMMs in the system  ***Since:*** vSphere API 6.7  | 
**health_status** | **str** | Summary of health status of all NVDIMMs in the system.  ***Since:*** vSphere API 6.7  | 
**total_capacity** | **int** | Total capacity of all NVDIMMs in bytes  ***Since:*** vSphere API 6.7  | 
**persistent_capacity** | **int** | Persistent region capacity in bytes  ***Since:*** vSphere API 6.7  | 
**block_capacity** | **int** | Block region capacity in bytes  ***Since:*** vSphere API 6.7  | 
**available_capacity** | **int** | Capacity not covered by namespace in bytes  ***Since:*** vSphere API 6.7  | 
**num_interleavesets** | **int** | Total number of interleave sets in the system  ***Since:*** vSphere API 6.7  | 
**num_namespaces** | **int** | Total number of namespaces in the system  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_summary import NvdimmSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmSummary from a JSON string
nvdimm_summary_instance = NvdimmSummary.from_json(json)
# print the JSON string representation of the object
print NvdimmSummary.to_json()

# convert the object into a dict
nvdimm_summary_dict = nvdimm_summary_instance.to_dict()
# create an instance of NvdimmSummary from a dict
nvdimm_summary_form_dict = nvdimm_summary.from_dict(nvdimm_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


