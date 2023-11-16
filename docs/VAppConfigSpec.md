# VAppConfigSpec

Configuration of a vApp  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_config** | [**List[VAppEntityConfigInfo]**](VAppEntityConfigInfo.md) | Configuration of sub-entities (virtual machine or vApp container).  Reconfigure privilege: See EntityConfigInfo  ***Since:*** vSphere API 4.0  | [optional] 
**annotation** | **str** | Description for the vApp.  Reconfigure privilege: VApp.Rename.  ***Since:*** vSphere API 4.0  | [optional] 
**instance_uuid** | **str** | vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal string.  This identifier is used by vCenter to uniquely identify all vApp instances in the Virtual Infrastructure environment.  Normally, this property is not set by a client, allowing the Virtual Infrastructure environment to assign or change it when VirtualCenter detects an identifier conflict between vApps.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.1  | [optional] 
**managed_by** | [**ManagedByInfo**](ManagedByInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_app_config_spec import VAppConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VAppConfigSpec from a JSON string
v_app_config_spec_instance = VAppConfigSpec.from_json(json)
# print the JSON string representation of the object
print VAppConfigSpec.to_json()

# convert the object into a dict
v_app_config_spec_dict = v_app_config_spec_instance.to_dict()
# create an instance of VAppConfigSpec from a dict
v_app_config_spec_form_dict = v_app_config_spec.from_dict(v_app_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


