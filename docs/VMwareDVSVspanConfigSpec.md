# VMwareDVSVspanConfigSpec

This class defines the configuration of a Distributed Port Mirroring session.  A Distributed Port Mirroring session  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session** | [**VMwareVspanSession**](VMwareVspanSession.md) |  | 
**operation** | **str** | Operation type, see *ConfigSpecOperation_enum* for valid values.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_vspan_config_spec import VMwareDVSVspanConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSVspanConfigSpec from a JSON string
v_mware_dvs_vspan_config_spec_instance = VMwareDVSVspanConfigSpec.from_json(json)
# print the JSON string representation of the object
print VMwareDVSVspanConfigSpec.to_json()

# convert the object into a dict
v_mware_dvs_vspan_config_spec_dict = v_mware_dvs_vspan_config_spec_instance.to_dict()
# create an instance of VMwareDVSVspanConfigSpec from a dict
v_mware_dvs_vspan_config_spec_form_dict = v_mware_dvs_vspan_config_spec.from_dict(v_mware_dvs_vspan_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


