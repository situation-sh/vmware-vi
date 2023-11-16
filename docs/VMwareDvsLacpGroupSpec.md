# VMwareDvsLacpGroupSpec

This class defines the configuration of a Link Aggregation Control Protocol group.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lacp_group_config** | [**VMwareDvsLacpGroupConfig**](VMwareDvsLacpGroupConfig.md) |  | 
**operation** | **str** | Operation type, see *ConfigSpecOperation_enum* for valid values.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_lacp_group_spec import VMwareDvsLacpGroupSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsLacpGroupSpec from a JSON string
v_mware_dvs_lacp_group_spec_instance = VMwareDvsLacpGroupSpec.from_json(json)
# print the JSON string representation of the object
print VMwareDvsLacpGroupSpec.to_json()

# convert the object into a dict
v_mware_dvs_lacp_group_spec_dict = v_mware_dvs_lacp_group_spec_instance.to_dict()
# create an instance of VMwareDvsLacpGroupSpec from a dict
v_mware_dvs_lacp_group_spec_form_dict = v_mware_dvs_lacp_group_spec.from_dict(v_mware_dvs_lacp_group_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


