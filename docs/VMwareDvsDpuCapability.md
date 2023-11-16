# VMwareDvsDpuCapability

The feature capabilities of Dpu Features supported by the vSphere Distributed Switch. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_offload_supported** | **bool** | Flag to indicate whether network offloading is supported on the vSphere Distributed Switch.  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_dpu_capability import VMwareDvsDpuCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsDpuCapability from a JSON string
v_mware_dvs_dpu_capability_instance = VMwareDvsDpuCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDvsDpuCapability.to_json()

# convert the object into a dict
v_mware_dvs_dpu_capability_dict = v_mware_dvs_dpu_capability_instance.to_dict()
# create an instance of VMwareDvsDpuCapability from a dict
v_mware_dvs_dpu_capability_form_dict = v_mware_dvs_dpu_capability.from_dict(v_mware_dvs_dpu_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


