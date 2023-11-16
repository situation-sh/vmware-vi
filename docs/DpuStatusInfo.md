# DpuStatusInfo

Data object describing the operational status of various DPU elements. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpu_id** | **str** | Uniquely identify this DPU.  Should be the VMware identifier which can be composed from pci and other identifying elements.  | 
**fru** | [**HostFru**](HostFru.md) |  | [optional] 
**sensors** | [**List[DpuStatusInfoOperationalInfo]**](DpuStatusInfoOperationalInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dpu_status_info import DpuStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DpuStatusInfo from a JSON string
dpu_status_info_instance = DpuStatusInfo.from_json(json)
# print the JSON string representation of the object
print DpuStatusInfo.to_json()

# convert the object into a dict
dpu_status_info_dict = dpu_status_info_instance.to_dict()
# create an instance of DpuStatusInfo from a dict
dpu_status_info_form_dict = dpu_status_info.from_dict(dpu_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


