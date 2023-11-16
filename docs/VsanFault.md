# VsanFault

Base exception class for VSAN-specific faults raised for host or cluster operations.  See also *HostVsanSystem*, *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vsan_fault import VsanFault

# TODO update the JSON string below
json = "{}"
# create an instance of VsanFault from a JSON string
vsan_fault_instance = VsanFault.from_json(json)
# print the JSON string representation of the object
print VsanFault.to_json()

# convert the object into a dict
vsan_fault_dict = vsan_fault_instance.to_dict()
# create an instance of VsanFault from a dict
vsan_fault_form_dict = vsan_fault.from_dict(vsan_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


