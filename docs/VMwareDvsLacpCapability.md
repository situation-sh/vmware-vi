# VMwareDvsLacpCapability

The feature capabilities of Link Aggregation Control Protocol supported by the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lacp_supported** | **bool** | Flag to indicate whether Link Aggregation Control Protocol is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | [optional] 
**multi_lacp_group_supported** | **bool** | Flag to indicate whether the vSphere Distributed Switch supports more than one Link Aggregation Control Protocol group to be configured.  It is suppported in vSphere Distributed Switch Version 5.5 or later.  ***Since:*** vSphere API 5.5  | [optional] 
**lacp_fast_mode_supported** | **bool** | Flag to indicate whether LACP Fast Mode is supported on the vSphere Distributed Switch.  LACP Fast Mode is supported in vSphere Distributed Switch Version 7.0 or later.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_lacp_capability import VMwareDvsLacpCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsLacpCapability from a JSON string
v_mware_dvs_lacp_capability_instance = VMwareDvsLacpCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDvsLacpCapability.to_json()

# convert the object into a dict
v_mware_dvs_lacp_capability_dict = v_mware_dvs_lacp_capability_instance.to_dict()
# create an instance of VMwareDvsLacpCapability from a dict
v_mware_dvs_lacp_capability_form_dict = v_mware_dvs_lacp_capability.from_dict(v_mware_dvs_lacp_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


