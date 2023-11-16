# VAppConfigInfo

Configuration of a vApp container.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_config** | [**List[VAppEntityConfigInfo]**](VAppEntityConfigInfo.md) | Configuration of sub-entities (virtual machine or vApp).  ***Since:*** vSphere API 4.0  | [optional] 
**annotation** | **str** | Description for the vApp.  ***Since:*** vSphere API 4.0  | 
**instance_uuid** | **str** | vCenter-specific 128-bit UUID of a vApp, represented as a hexademical string.  This identifier is used by vCenter to uniquely identify all vApp instances.  ***Since:*** vSphere API 4.1  | [optional] 
**managed_by** | [**ManagedByInfo**](ManagedByInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_app_config_info import VAppConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VAppConfigInfo from a JSON string
v_app_config_info_instance = VAppConfigInfo.from_json(json)
# print the JSON string representation of the object
print VAppConfigInfo.to_json()

# convert the object into a dict
v_app_config_info_dict = v_app_config_info_instance.to_dict()
# create an instance of VAppConfigInfo from a dict
v_app_config_info_form_dict = v_app_config_info.from_dict(v_app_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


