# UpdateDVSLacpGroupConfigRequestType

The parameters of *VmwareDistributedVirtualSwitch.UpdateDVSLacpGroupConfig_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lacp_group_spec** | [**List[VMwareDvsLacpGroupSpec]**](VMwareDvsLacpGroupSpec.md) | The Link Aggregation Control Protocol groups to be configured.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.update_dvs_lacp_group_config_request_type import UpdateDVSLacpGroupConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDVSLacpGroupConfigRequestType from a JSON string
update_dvs_lacp_group_config_request_type_instance = UpdateDVSLacpGroupConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDVSLacpGroupConfigRequestType.to_json()

# convert the object into a dict
update_dvs_lacp_group_config_request_type_dict = update_dvs_lacp_group_config_request_type_instance.to_dict()
# create an instance of UpdateDVSLacpGroupConfigRequestType from a dict
update_dvs_lacp_group_config_request_type_form_dict = update_dvs_lacp_group_config_request_type.from_dict(update_dvs_lacp_group_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


