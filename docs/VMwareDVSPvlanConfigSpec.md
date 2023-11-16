# VMwareDVSPvlanConfigSpec

This class defines the configuration of a PVLAN map entry  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pvlan_entry** | [**VMwareDVSPvlanMapEntry**](VMwareDVSPvlanMapEntry.md) |  | 
**operation** | **str** | Operation type.  See *ConfigSpecOperation_enum* for valid values, except for the \&quot;edit\&quot; value, which is not supported.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_pvlan_config_spec import VMwareDVSPvlanConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSPvlanConfigSpec from a JSON string
v_mware_dvs_pvlan_config_spec_instance = VMwareDVSPvlanConfigSpec.from_json(json)
# print the JSON string representation of the object
print VMwareDVSPvlanConfigSpec.to_json()

# convert the object into a dict
v_mware_dvs_pvlan_config_spec_dict = v_mware_dvs_pvlan_config_spec_instance.to_dict()
# create an instance of VMwareDVSPvlanConfigSpec from a dict
v_mware_dvs_pvlan_config_spec_form_dict = v_mware_dvs_pvlan_config_spec.from_dict(v_mware_dvs_pvlan_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


